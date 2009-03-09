#!/usr/bin/env python

import re

class UrlFormat:
    def clean(self, url):
        filename = url
        
        filename = re.sub('^http','',filename)
        filename = re.sub('^s', '', filename)      
        filename = re.sub("^%3A//", "", filename)
        filename = re.sub("^://", "", filename)
        filename = re.sub("^:/", "", filename)
        filename = re.sub("javascript:", "", filename)
        filename = re.sub("\+\+", "", filename)
        filename = re.sub("<script>(.*?)</script>", "", filename)
        filename = re.sub("/$", "", filename) # directories are treated as files.
         
        return filename;
    
    def standardise(self, url):
        
        filename = re.sub("/$", "", url) # directories are treated as files

        if re.match("^http://", filename) == None:
           filename = "http://" + filename
        return filename
    
    def removeXSS(self, url):
        
        filename = url
        filename = re.sub("<script", "", filename)
        filename = re.sub("document.cookie", "", filename)
        filename = re.sub(">", "", filename)
        filename = re.sub("<", "", filename)
        filename = re.sub("&gt;", "", filename)
        filename = re.sub("&lt;", "", filename)
        filename = re.sub(";", "", filename)
        filename = re.sub("\+src=", "", filename)
        
        return filename
    
    def createDigest(self, url):
        filename = self.unquote(url)
        filename = self.standardise(filename)
        
        return md5.new(filename).hexdigest()
    
    def unquote(self, url):
        
        url = urllib.unquote_plus(url).decode("utf-8")
        return re.sub(" ", "+", url)

