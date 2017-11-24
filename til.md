# Today I learned

Desirable as a:

- Hosted Web app
- Searchable, individual linked notes

For now, though.


### Manual entered notes:

Content-Disposition: Proposed as a means for the origin server to suggest a default file name 
(http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html)


In Vim, use 'n' for forward search and 'N' for backward search


`find -iname` to ignore the case when searching for files


When using "top", use "c" to toggle between process name and the command line


If your tests has docstrings, nose will display the string instead of
the default function/method name:http://bit.ly/1VfJnfr


puppet's nginx resource module's `vhost_cfg_prepend` can be used to enter arbitrary configuration. For example, for parameters not defined by the module such as `large_client_header_buffers`


when you do a `git commit --amend`, you are creating a new commit with a new SHA. HEAD then points to the new SHA instead of the old one.


To upload a file simulating form upload via `httpie`, `http -f POST example.com/jobs name='John Smith' cv@~/Documents/cv.pdf`

Learned about [X-Forwarded-Proto](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-Proto) header. With curl use: `curl -H "X-Forwarded-Proto: https" ..`


`MultiDict`: http://werkzeug.pocoo.org/docs/0.10/datastructures/#werkzeug.datastructures.MultiDict


Demo of a Flask app to handle file uploads: https://github.com/amitsaha/learning/tree/master/Python/flask-webapp/file_upload


Learned about mysql's ``default-group-suffix`` option: https://dev.mysql.com/doc/refman/5.0/en/option-file-options.html#option_general_defaults-group-suffix


Started using `The silver searcher` today (https://github.com/ggreer/the_silver_searcher) and it's faster than ack!


puppet - Copy all files in a directory: https://docs.puppetlabs.com/guides/techniques.html#how-can-i-manage-whole-directories-of-files-without-explicitly-listing-the-files


nginx rewrite rule: ^/foo/bar$ /foo/bar/ permanent will permanently redirect /foo/bar to /foo/bar/. See http://nginx.org/en/docs/http/ngx_http_rewrite_module.html 


The command ``chown`` also accepts user IDs/group IDs instead of names.

My XFS root file system on Fedora was showing up as 100% full when i used `df`, but when I was viewing disk usage via `ncdu` I could see that it was hardly 15% full..Searching a bit, I used `xfs_fsr /dev/mapper/fedora_syd--asaha--d-root  -v` and all's good again. To learn more: http://linux.die.net/man/8/xfs_fsr


Today, I learned about how BBC in 1950 fooled people into believing that Sphagetti grows on trees: http://nowiknow.com/the-spaghetti-tree-hoax/ 


I learned about [`autospeccing`](https://docs.python.org/3/library/unittest.mock.html#autospeccing) when mocking objects in Python.


I learned that CPython caches integer objects: http://codeyarns.com/2012/05/01/integer-caching-in-python/


Converting a string date time to epoch seconds: http://stackoverflow.com/questions/9637838/convert-string-date-to-timestamp-in-python


Create a URL with query parameters: 
```
>>> urlparse.urljoin('http://foo.bar','foo?%s' % urllib.urlencode({'project_id':1, 'file_id':2}))
'http://foo.bar/foo?project_id=1&file_id=2'
```


delete-selection mode in Emacs: http://stackoverflow.com/questions/2627289/how-to-replace-a-region-in-emacs-with-yank-buffer-contents


Create a new environment in [conda](http://conda.pydata.org/docs/index.html) using ``conda create -n testinfra python=2.7`` and then activate it using ``source activate testinfra`` and deactivate it using ``source deactivate``. List all environments using:``conda info --envs``.


Learned about the ``maybe`` pattern (https://en.wikibooks.org/wiki/Haskell/Understanding_monads/Maybe) and a Python implementation (https://github.com/ekampf/pymaybe). Here is an example:
```
from pymaybe import maybe

class Number():
    def __init__(self, value=None):
        self.value = value

n1 = Number(1)
n2 = Number(2)
n3 = None

print([maybe(x).value.or_else(0) for x in [n1, n2, n3]])
print([x.value if getattr(x, 'value', None) else 0 for x in [n1, n2, n3]])
```


use ``(setq-default show-trailing-whitespace t)`` to show trailing white space via Trent.

How to assert a mock object not being called? http://stackoverflow.com/questions/12187122/assert-a-function-method-was-not-called-using-mock


Uploading a file via ``httpie``: http --form POST <blah> filedata=@~/scientific23.png 


I have usually used git rebase -i to squash commits, but I think git reset --soft is less magical: http://stackoverflow.com/a/5201642/59634


Python: To check if a mocked object has been called, ``self.assertTrue(mocked_object.called)``.


List of MySQL user accounts: ``SELECT User FROM mysql.user;``


Learned about the N+1 selects "problem" in ORMs from http://openmymind.net/scaling-viki/. Here is a stack overflow question/answer: http://stackoverflow.com/questions/97197/what-is-the-n1-selects-issue and learned that SQLAlchemy (Python ORM) addresses this (http://www.sqlalchemy.org/features.html)


*Problem: Find duplicate files in the file system*

First solution:

0. Initialize a hash table
1. Read each file, calculate a hash value
2. Does the hash value exist in the hash table? If yes, you have a duplicate, else
3. Put it in the hash table as key, with the value being the file name
4. Repeat

Second solution:

Instead of reading entire files, use a "finger printing based technique". Percpetual hashing seems to be very popular for images and multimedia files. For text files, use something like simhash.


Nice paper from Akamai: http://www.sigcomm.org/sites/default/files/ccr/papers/2015/July/0000000-0000009.pdf . One of the things they discuss is how they use bloom filters to not cache objects which will be accessed only once.


You can pass options such as  "--since 1 week ago" to git log to see logs since 1 week and such.


Learned about Linux task stats: https://www.kernel.org/doc/Documentation/accounting/taskstats.txt


Use `netstat -nputwc` to show a continuously  updating network connections on Linux


CPU steal time: http://blog.scoutapp.com/articles/2013/07/25/understanding-cpu-steal-time-when-should-you-be-worried

To sync entire directories via `aws` CLI: `aws s3 sync`

