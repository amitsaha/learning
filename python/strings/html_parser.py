# Parse HTML and make sure that the tags are well formed
# http://docs.python.org/2/library/htmlparser.html
from HTMLParser import HTMLParser

# tags
tags = []

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print "Encountered a start tag:", tag
        tags.append(tag)
    def handle_endtag(self, tag):
        #print "Encountered an end tag :", tag
        if tags and tags[-1] == tag:
            tags.pop()
        else:
            raise Exception('Invalid HTML')
    def handle_data(self, data):
        print "Encountered some data  :", data

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed('<head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')
assert not tags
