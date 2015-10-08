#Today I learned

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
