#!/usr/bin/env python

import wsgiref.handlers;

import Model
import Url

import re
import os
import unicodedata
import simplejson
import urllib
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db as gdb
from google.appengine.api import users
from yos.boss import ysearch
from yos.yql import db, udfs

class Result:
    def __init__(self, title, abstract, site, url):
        self.title = title
        self.abstract = abstract
        self.url = url
        self.site = site
        self.id = re.sub("\.","", site)

    
class ResultJsonEncoder(simplejson.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Result):
            return {"title": obj.title, "abstract": obj.abstract, "url" : obj.url, "site": obj.site, "id": obj.id}
        return simplejson.JSONEncoder.default(self, obj)
    

class Queries:
    def PopularTopics(self, page):
        query = Model.TopicSearch.all()
        query.order("-topicCount")
        return query.fetch(limit = 100, offset = (page - 1) * 100)
    
    def PopularTopics(self, page):
        query = Model.TopicSearch.all()
        query.order("-topicCount")
        query.filter("type =", "Safe")
        return query.fetch(limit = 100, offset = (page - 1) * 100)
    
    def PopularUnclassifiedTopics(self, page):
        query = Model.TopicSearch.all()
        query.filter("type =", "Unclassified")
        query.order("-topicCount")
        return query.fetch(limit = 100, offset = (page - 1) * 100)

class SubjectSearch(webapp.RequestHandler):
    'Searches for the top sites in a topic'
    def get(self, topic = "", subject=""):        
        #Use the query string parameters if present.
        topic = self.request.get("topic", topic)
        
        formatter = Url.UrlFormat()
        topic = formatter.removeXSS(topic)
        
        if topic == "" or topic is None:
            topic = "Paul Kinlan"
            
        topic = urllib.unquote_plus(topic)
               
        subject = self.request.get("subject", subject)
        
        if subject == "" or subject is None:
            subject = topic

        subject = urllib.unquote_plus(subject)

        topicSearch = Model.TopicSearch.gql("WHERE topic = :1", topic.lower()).get()
        
        if topicSearch is None:
            topicSearch = Model.TopicSearch(topic = topic.lower())
            
        topicSearch.topicCount = topicSearch.topicCount + 1
        topicSearch.put()
        
        subjectSearch = Model.SubjectSearch.gql("WHERE subject = :1", subject.lower()).get()
        if subjectSearch is None:
            subjectSearch = Model.SubjectSearch(subject = subject.lower())
            
        if subjectSearch.sitesData is None:
            tn = db.create(name="tn", data=ysearch.search(subject, vertical="web", count=10, more={"filter": "-porn", "type": "html"}))
            subjectSearch.sitesData = tn.dumps()
        else:
            tn = db.create(name = "tn", data = db.simplejson.loads(subjectSearch.sitesData))
        
        subjectSearch.subjectCount = subjectSearch.subjectCount + 1
        
        subjectSearch.put()
        
        subjectTopicSearch = Model.TopicSubjectSearch.gql("WHERE topic = :1 AND subject = :2", topicSearch, subjectSearch).get()
        if subjectTopicSearch is None:
            subjectTopicSearch = Model.TopicSubjectSearch(topic = topicSearch, subject = subjectSearch)
            
        subjectTopicSearch.count = subjectTopicSearch.count + 1
        subjectTopicSearch.put()        
                
        results = { 0 : [], 1: []}
        urls = {}
        column = 0
        for row in tn.rows:            
            url = row["tn$url"]
            match = re.match("http://([^/]*)", url)
            if match is not None:
                domain = match.group(1)
                title =  un_unicode_string(row["tn$title"])
                abstract = un_unicode_string(row["tn$abstract"])
                result = Result(title, abstract, domain, url)
                urls[domain] = result
                
        for result in urls:
            results[column % 2].append(urls[result])
            column = column + 1
        
        path = os.path.join(os.path.dirname(__file__), 'results.tmpl')
        
        self.response.out.write(template.render(path, {'decoded_query': topic, "decoded_subject": subject, 'type': topicSearch.type, 'query': topic, 'subject': subject , 'urls1': results[0], 'urls2': results[1]}))

class SiteSubSearch(webapp.RequestHandler):
    def get(self, site = "", terms = "", subject = ""):
        tn = db.create("tn", data = ysearch.search(terms + " " + subject + " site:" + site, count = 4, more={"filter": "-porn", "type": "html"}))
        results = []
        for row in tn.rows:
            url = row["tn$url"]
            match = re.match("http://([^/]*)", url)
            if match is not None:
                title =  un_unicode_string(row["tn$title"])
                abstract = un_unicode_string(row["tn$abstract"])
                result = Result(title, abstract, match.group(1), url)
                results.append(result)
        
        encoder = ResultJsonEncoder()

        self.response.out.write(encoder.encode(results))
        
class PopularAdmin(webapp.RequestHandler):
    def get(self, action = ""):
        
        #Check to see if the user is logged in.
        user = users.get_current_user()
        if user:
            page = int(action)
            popular = Queries()
            path = os.path.join(os.path.dirname(__file__), 'TopicAdmin.html')
            
            prev = page - 1
            next = page + 1
            
            if page == 1:
                prev = 1
                
            self.response.out.write(template.render(path, {"user": user.email, "page": page, "items" : popular.PopularUnclassifiedTopics(page) }))
    
        else:
            greeting = ("<a href=\"%s\">Sign in or register</a>." + users.create_login_url("/"))
            self.response.out.write(greeting)
      
    def post(self, action = ""):
        'Handles when the values are submitted so that the correct adverts can be managed'
        path = os.path.join(os.path.dirname(__file__), 'TopicAdmin.html')
        page = int(action)
        
        for argument in self.request.arguments():
            value = self.request.get(argument)
            
            if value == "Unclassified":
                continue
            
            topic = Model.TopicSearch.gql("WHERE topic = :1", argument).get()
            
            if topic != None:
                topic.type = value
                topic.put()
            else:
                self.response.out.write(argument)
        
        page = 1
        popular = Queries()
        user = users.get_current_user()
        self.response.out.write(template.render(path, {"user": user.email, "page": page,"items" : popular.PopularUnclassifiedTopics(page) }))
        

class Popular(webapp.RequestHandler):
    def get(self, action = ""):
        
        #Check to see if the user is logged in.
        page = int(action)
        popular = Queries()
        path = os.path.join(os.path.dirname(__file__), 'TopicPopular.html')
            
        prev = page - 1
        next = page + 1
            
        if page == 1:
            prev = 1
                
        self.response.out.write(template.render(path, {"page": page, "items" : popular.PopularUnclassifiedTopics(page) }))

class Index(webapp.RequestHandler):
    def get(self, action = ""):
        popTopics = Model.TopicSearch.gql("WHERE type = 'Safe' ORDER BY topicCount DESC").fetch(5)
        popTopicSubjects = Model.TopicSubjectSearch.gql("ORDER BY count DESC").fetch(5)
        undiscoveredTopics = Model.TopicSearch.gql("ORDER BY topicCount ASC").fetch(5)
        undiscoveredTopicSubjects = Model.TopicSubjectSearch.gql("ORDER BY count ASC").fetch(5)
        
        path = os.path.join(os.path.dirname(__file__), 'index.html')        
        self.response.out.write(template.render(path, { "popTopics": popTopics, "popSearches": popTopicSubjects, "undiscoveredTopics": undiscoveredTopics, "undiscoveredSearches": undiscoveredTopicSubjects  }))

def un_unicode_string(string):
    'strip unicode characters'   
    return unicodedata.normalize('NFKD', unicode(string)).encode('ASCII', 'ignore')

def main():
    application = webapp.WSGIApplication([("/popular/(\d+)", Popular), ("/_popular/(\d+)", PopularAdmin), ("/Site/(.*)/(.*)/(.*)", SiteSubSearch), ("/(.*)/(.*)", SubjectSearch), ("/(index.html)*", Index) ,("/(.*)", SubjectSearch) ,("/query", SubjectSearch)], debug=False)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()