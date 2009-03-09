#!/usr/bin/env python

from google.appengine.ext import db as gdb

class TopicSearch(gdb.Model):
    'A Search object is a record of a search that has been performed.  Currently just stores the text and the vertical result.'
    topic = gdb.StringProperty(required = True)
    firstQueryDateTime = gdb.DateTimeProperty(auto_now_add = True)
    topicCount = gdb.IntegerProperty(default = 0)
    type = gdb.StringProperty(default = 'Unclassified', choices = [None, 'Safe', 'Unclassified', 'Porn', 'Spam', 'Hate', 'Gambling', 'Hacking', 'Drugs', 'Pharma'])

class SubjectSearch(gdb.Model):
    'You Search for a Topic inside a Subject'
    subject = gdb.StringProperty(required = True)
    firstQueryDateTime = gdb.DateTimeProperty(auto_now_add = True)
    sitesData = gdb.TextProperty() # A cache of the XML/JSON
    subjectCount = gdb.IntegerProperty(default = 0)
    type = gdb.StringProperty(default = 'Unclassified', choices = [None, 'Safe', 'Unclassified', 'Porn', 'Spam', 'Hate'])

class TopicSubjectSearch(gdb.Model):
    topic = gdb.ReferenceProperty(TopicSearch)
    subject = gdb.ReferenceProperty(SubjectSearch)
    count = gdb.IntegerProperty(default = 0)
    type = gdb.StringProperty(default = 'Unclassified', choices = [None, 'Safe', 'Unclassified', 'Porn', 'Spam', 'Hate'])
    topicName = gdb.StringProperty()
    subjectName = gdb.StringProperty()

class Domain(gdb.Model):
    'A domain is a Domain name that has will be parsed for title information'
    url = gdb.StringProperty(required = True)
    urlCreateTime = gdb.DateTimeProperty(auto_now_add = True)
    recieved = gdb.BooleanProperty(default = False)
    recievedCreateDateTime = gdb.DateTimeProperty()
    title = gdb.StringProperty()