
import re

page_reqs = re.compile(r'GET [/[a-z,_,-]*\d*]*/[[a-z,_,-]*\d*.[a-z]*]*', flags = re.IGNORECASE)
#date_time = re.compile(r'[/d/d/[


def readlog():
    with open('apachelog.log','r') as f:
        for line in f:
            if line:
                fields = line.split()
                client, http_response, content_size = fields[0], fields[-2], fields[-1]
                print client, page_reqs.findall(line), http_response, content_size

readlog()        
