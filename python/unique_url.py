'''
You have a file with a large number of URLs, find the first unique URL

PS: The entire file is too big to be brought into memory.
'''

from collections import OrderedDict

# this approach cannot work for large files since we do not
# have enough memory to store the large file
def find_unique_url(file):
    urls = OrderedDict()
    with open(file) as f:
        line_no = 0
        for url in f:
            line_no += 1
            if url in urls:
                urls.pop(url)
            else:
                urls[url] = line_no
    return urls.keys()[0], urls[urls.keys()[0]]

# use multiple ordered dicts
def find_unique_url_multi_dict(file):
    current_dict = OrderedDict()
    dicts = [current_dict]

    with open(file) as f:
        line_no = 0
        for url in f:
            line_no += 1
            if len(current_dict) > 100:
                current_dict = OrderedDict()
                dicts.append(current_dict)
            if url in current_dict:
                current_dict.pop(url)
            else:
                current_dict[url] = line_no

    while dicts:
        d = dicts.pop(0)
        for k, v in d.iteritems():
            not_found = True
            for d1 in dicts:
                if k not in d1:
                    continue
                else:
                    not_found = False
                    break
            if not_found:
                return k, v

print(find_unique_url('urls.txt'))
print(find_unique_url_multi_dict('urls.txt'))
