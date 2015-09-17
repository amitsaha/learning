import re
text = 'a text with an embedded hyperlink <a href="http://www.google.com">this text</a>. And another link <a href="http://www.gogle.com">some text</a>'

hyperlink_finder = re.compile(r'<a href="http://[a-z,.]*">')

for link  in hyperlink_finder.findall(text):
    print link
