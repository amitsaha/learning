*Table of contents*

- [Infrastructure/Platform/Workflow](#infraworkflow)
- [Web/APIs/Network Services](#webapis)
- [Programming Languages](#programming-languages)
- [Data Science/Optimization/Machine Learning/Evolutionary Algorithms](#data-scienceoptimizationmachine-learningevolutionary-algorithms)
- [Talks](#talks)


## Infrastructure/Platform/Workflow

Ansible

- http://www.ansible.com/home

AWS

### Deployments

- https://www.thoughtworks.com/insights/blog/implementing-blue-green-deployments-aws


### Tools

- https://github.com/awslabs/aws-shell
- https://github.com/Azure/draft

### Lambda

- https://www.expeditedssl.com/aws-lambda-in-plain-english

### IAM roles/policies

- https://medium.com/netflix-techblog/introducing-aardvark-and-repokid-53b081bf3a7e

### S3

- https://www.expeditedssl.com/aws-s3-in-plain-english
- https://www.expeditedssl.com/aws-s3-buckets-of-objects

### Generic

- http://highscalability.com/blog/2016/1/11/a-beginners-guide-to-scaling-to-11-million-users-on-amazons.html

Command line

- 20 Linux System Monitoring Tools Every SysAdmin Should Know: http://www.cyberciti.biz/tips/top-linux-monitoring-tools.html
- The art of command line: https://github.com/jlevy/the-art-of-command-line
- cheat: https://github.com/chrisallenlane/
- explainshell: https://github.com/idank/explainshell
- Encrypt and Decrypt files using pgp: http://www.cyberciti.biz/tips/linux-how-to-encrypt-and-decrypt-files-with-a-password.html

Databases

- Readings in Database Systems: http://www.redbook.io/
- http://tech.noredink.com/post/133347435578/optimizing-mysql-for-high-concurrency-on-amazon
- A beginners guide to SQL: http://www.sohamkamani.com/blog/2016/07/07/a-beginners-guide-to-sql/


Elastic Search and others

- Setup and installation: https://www.elastic.co/guide/en/elasticsearch/reference/1.4/setup.html
- https://www.elastic.co/blog/what-is-an-elasticsearch-index
- https://github.com/elastic/elasticsearch-definitive-guide
- Tribe node: https://www.elastic.co/blog/tribe-node
- Running elasticsearch in production: http://blogs.justenougharchitecture.com/running-elasticsearch-in-production/
- Logstash input plugins: https://www.elastic.co/guide/en/logstash/current/plugins-inputs-file.html
- https://www.elastic.co/products/beats
- Inverted index: https://www.elastic.co/guide/en/elasticsearch/guide/current/inverted-index.html
- Making text searchable: https://www.elastic.co/guide/en/elasticsearch/guide/current/making-text-searchable.html
- Distributed search execution: https://www.elastic.co/guide/en/elasticsearch/guide/current/distributed-search.html
- Analyzer: https://www.elastic.co/guide/en/elasticsearch/guide/current/analysis-intro.html
- Inside a shard: https://www.elastic.co/guide/en/elasticsearch/guide/current/inside-a-shard.html
- Transactions in Elastic search: https://blog.codecentric.de/en/2014/10/transactions-elasticsearch/
- Good terminology guide: Running elasticsearch in production: http://blogs.justenougharchitecture.com/running-elasticsearch-in-production/
- Leader election: https://www.elastic.co/blog/found-leader-election-in-general


Consul (Service discovery, DNS, balancing)

- http://www.consul.io/intro/
- Tuning haproxy: https://blog.codeship.com/performance-tuning-haproxy/?utm_source=webopsweekly&utm_medium=email

Git

- Git subtree: http://blogs.atlassian.com/2013/05/alternatives-to-git-submodule-git-subtree/
- Exclude a directory from git diff: http://stackoverflow.com/questions/4380945/exclude-a-directory-from-git-diff
- Git garbage collection: http://think-like-a-git.net/sections/graphs-and-git/garbage-collection.html
- Gc and Pruning: http://alblue.bandlem.com/2011/11/git-tip-of-week-gc-and-pruning-this.html
- Git - Maintenance and data recovery: https://git-scm.com/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery
- Git is a purely functional data structure: http://www.jayway.com/2013/03/03/git-is-a-purely-functional-data-structure/

Vagrant

- https://www.vagrantup.com/

Linux

- Linux performance analysis in 60 seconds: http://techblog.netflix.com/2015/11/linux-performance-analysis-in-60s.html?m=0
- Experiments with the Linux disk cache: http://www.linuxatemyram.com/play.html
- Files are Hard: http://danluu.com/file-consistency/
- entr: http://entrproject.org/

Linux Containers/Sandboxing/VMs

- https://www.docker.com/
- Docker machine: https://docs.docker.com/machine/
- Docker compose: https://docs.docker.com/compose/
- DNS for docker: https://github.com/tonistiigi/dnsdock
- libvirt Sandbox: http://sandbox.libvirt.org/download/
- Docker toolbox: https://www.docker.com/toolbox

nginx

- How nginx processes a request: http://nginx.org/en/docs/http/request_processing.html
- http://nginx.org/en/docs/http/ngx_http_rewrite_module.html
- nginx load balancing: http://nginx.org/en/docs/http/load_balancing.html
- http://www.unixmen.com/install-lemp-server-nginx-mariadb-and-php-on-fedora-22/
- https://www.digitalocean.com/community/tutorials/how-to-set-up-multiple-ssl-certificates-on-one-ip-with-nginx-on-ubuntu-12-04


SSH

- How to disable host key checking? http://linuxcommando.blogspot.com.au/2008/10/how-to-disable-ssh-host-key-checking.html
- Permissions for .ssh: http://superuser.com/questions/215504/permissions-on-private-key-in-ssh-folder


Status updates

- https://cachethq.io/

Managing Infrastructure

- Terraform: terraform.io

httpie

- https://github.com/jkbrzt/httpie
- By deafault httpie encodes stuff as strings, but if the data type is to be preserved, use ``:=``

Miscellaneous

- Bash alias with parameters: http://stackoverflow.com/questions/7131670/make-bash-alias-that-takes-parameter
- ``arc`` (CLI for phabricator): https://secure.phabricator.com/book/phabricator/article/arcanist/
- ``arc`` updating an existing patch: https://phab.enlightenment.org/w/arcanist/#update-an-existing-patch
- ``JSONView`` Firefox plugin for pretty viewing JSON (https://addons.mozilla.org/en-us/firefox/addon/jsonview/)
- The magic of consistent hashing: http://www.paperplanes.de/2011/12/9/the-magic-of-consistent-hashing.html
- Deploying GitHub pages via TravisCI: https://gist.github.com/domenic/ec8b0fc8ab45f39403dd
- Basic Infrastructure Patterns: http://www.scriptcrafty.com/basic-infrastructure-patterns/
- What's in a build tool? http://www.lihaoyi.com/post/WhatsinaBuildTool.html
- How to deploy software? https://zachholman.com/posts/deploying-software
- Linux task stats: https://www.kernel.org/doc/Documentation/accounting/taskstats.txt
- Logging: https://sematext.com/blog/2016/09/13/logstash-alternatives/


Jenkins

- jenkins-job-builder: http://jenkins-job-builder.readthedocs.org/
- Jenkins job DSL plugin: https://github.com/jenkinsci/job-dsl-plugin

Puppet

- Courseware learning VM: https://github.com/puppetlabs/courseware-lvm
- Puppet cookbook: http://www.puppetcookbook.com/
- Puppet nginx: https://github.com/jfryman/puppet-nginx
- Module fundamentals: https://docs.puppetlabs.com/puppet/latest/reference/modules_fundamentals.html
- Designing Puppet – Roles and Profiles: http://www.craigdunn.org/2012/05/239/
- Node classification - Roles and profiles: http://puppetlunch.com/puppet/roles-and-profiles.html

Vault (Secret management)

- https://www.vaultproject.io/intro/getting-started/acl.html

Infrastructure testing

- Serverspec: http://serverspec.org/tutorial.html
- testinfra: https://testinfra.readthedocs.org/
- A brief introduction to server testing with serverspec: https://www.debian-administration.org/article/703/A_brief_introduction_to_server-testing_with_serverspec
- aws-spec: https://github.com/serverworks/aws-spec
- goss: https://github.com/aelsabbahy/goss

Task queues

- http://www.rabbitmq.com/tutorials/amqp-concepts.html

## Web/REST APIs

- JSON API - http://jsonapi.org/
- Web API design - Crafting interfaces that developers love: http://apigee.com/about/resources/ebooks/web-api-design
- Designing for Performance: http://designingforperformance.com/
- REST and long running jobs: http://farazdagi.com/blog/2014/rest-long-running-jobs/
- Testing services without running tests: https://blog.twitter.com/2015/diffy-testing-services-without-writing-tests
- Webhook server: http://avoidwork.github.io/rozu/
- Gzip compression: http://betterexplained.com/articles/how-to-optimize-your-site-with-gzip-compression/
- Facebook guidlines for making multiple requests: https://developers.facebook.com/docs/graph-api/making-multiple-requests
- HTTP Basic vs HTTP digest auth: http://mark-kirby.co.uk/2013/how-to-authenticate-apis-http-basic-vs-http-digest/
- Controlling crawling and Indexing: https://developers.google.com/webmasters/control-crawl-index/
- Mobile redirection with nginx: https://jyunderwood.com/2012/08/23/mobile-redirection-with-nginx/
- Cloud based SMTP Server - SendGrid: https://sendgrid.com/
- Amazon SES: https://aws.amazon.com/ses/
- Service Workers: http://www.html5rocks.com/en/tutorials/service-worker/introduction/
- UpUp.js: https://www.talater.com/upup/getting-started-with-offline-first.html
- http snippet generator: https://github.com/Mashape/httpsnippet
- REST API with Python and Flask: https://speakerdeck.com/miguelgrinberg/creating-a-rest-api-with-python-and-flask-pydx-2015
- API Gateway: https://getkong.org/about/
- JSON decode benchmarking: http://blog.ionelmc.ro/2015/11/22/memory-use-and-speed-of-json-parsers/
- GRPC/protobuf/swagger: https://coreos.com/blog/gRPC-protobufs-swagger.html
- Load testing: https://serialized.net/2017/06/load-testing-with-vegeta-and-python/

### HTTP/2.0

- HTTP/2: https://www.nginx.com/wp-content/uploads/2015/09/NGINX_HTTP2_White_Paper_v4.pdf
- HTTP/2 for Python: https://github.com/lukasa/hyper
- C: https://nghttp2.org/documentation/index.html
- Golang support should be coming up in 1.6: https://godoc.org/golang.org/x/net/http2
- Tools for debugging/testing/using Http/2: https://blog.cloudflare.com/tools-for-debugging-testing-and-using-http-2/


### CORS

- CORS: https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS
- CORS server side: https://developer.mozilla.org/en-US/docs/Web/HTTP/Server-Side_Access_Control
- https://www.nczonline.net/blog/2010/05/25/cross-domain-ajax-with-cross-origin-resource-sharing/
- http://enable-cors.org/index.html

### Network services across multiple languages

- https://thrift.apache.org/
- thrift-tools: Inspecting thrift traffic - https://github.com/pinterest/thrift-tools
- Python implementation of thrift: https://github.com/eleme/thriftpy
- zerorpc: http://www.zerorpc.io/
- gRPC: http://www.grpc.io/

### GraphQL

- http://graphql.org
- https://facebook.github.io/graphql/
- https://github.com/chentsulin/awesome-graphql
- Exploring Graphql: https://www.youtube.com/watch?v=WQLzZf34FJ8
- https://code.facebook.com/posts/1691455094417024/graphql-a-data-query-language/
- Basic API with GraphQL: http://davidandsuzi.com/writing-a-basic-api-with-graphql/
- GraphQL schema and server wrapping: https://github.com/graphql/swapi-graphql

### Microservices architecture

- https://azure.microsoft.com/en-us/blog/design-patterns-for-microservices/

### Network programming

- https://blog.cloudflare.com/how-to-receive-a-million-packets/

## Programming Languages

C

- libmill: https://github.com/sustrik/libmill
- Build Your Own Lisp: 
http://www.buildyourownlisp.com
- hwloc: https://github.com/open-mpi/hwloc
- libcello: http://libcello.org/
- nanomsg: http://nanomsg.org/documentation.html
- tcpmux: https://github.com/sustrik/tcpmux
- zeromq: http://zeromq.org/
- cwrap: https://lwn.net/Articles/594863/, https://cwrap.org/
- Making robust software: http://www.verticalsysadmin.com/making_robust_software/
- https://www.iar.com/support/resources/articles/advanced-preprocessor-tips-and-tricks/
- Modern C: http://icube-icps.unistra.fr/img_auth.php/d/db/ModernC.pdf
- libsigsegv: https://www.gnu.org/software/libsigsegv/

Clojure

- Clojure for the brave and true: http://www.braveclojure.com/

clojurescript

- https://github.com/clojure/clojurescript/wiki/Quick-Start
- https://github.com/bhauman/lein-figwheel

C++

Elm

- Elm by example: http://elm-by-example.org/
- Real world Elm - Part 1: http://engineering.truqu.com/2015/08/19/real-world-elm-part-1.html
- Real World Elm - Part 2: http://engineering.truqu.com/2015/09/25/real-world-elm-part-2.html

Elixir

- http://elixir-lang.org/getting-started/introduction.html
- Elixir by example: https://github.com/jeregrine/elixir-by-example


Golang

- How to write Go code: https://golang.org/doc/code.html
- Effective Go: 
https://golang.org/doc/effective_go.html
- The Little Go Book: http://openmymind.net/The-Little-Go-Book/
- Working with files in Go: http://devdungeon.com/content/working-files-go
- Testing in Go series: https://smartystreets.com/blog/tags/testing-in-go-series
- TLS with Go: https://ericchiang.github.io/tls/go/https/2015/06/21/go-tls.html
- Awesome go: https://github.com/avelino/awesome-go/blob/master/README.md
- Golang Amazon: https://github.com/mitchellh/goamz, http://stackoverflow.com/questions/22867013/golang-connecting-to-s3
- afero: A universal filesystem library: https://blog.gopheracademy.com/advent-2015/afero-a-universal-filesystem-library/
- Bleve: Full text search/indexing library - http://www.blevesearch.com/
- https://github.com/emluque/dscache


JavaScript

- Moment.js: http://momentjs.com/ (Dates)
- Node.js tutorial: https://www.airpair.com/javascript/node-js-tutorial
- Eloquent JavaScript: http://eloquentjavascript.net/
- algebra.js: https://github.com/nicolewhite/algebra.js
- linear-algebra: https://github.com/hiddentao/linear-algebra
- Numeric JS: http://www.numericjs.com/
- Scoping and Hoisting: http://www.adequatelygood.com/JavaScript-Scoping-and-Hoisting.html and https://www.interviewcake.com/question/js-scope
- nodemon: https://github.com/remy/nodemon
- ES6 promises: https://ponyfoo.com/articles/es6-promises-in-depth
- JS promises: http://www.html5rocks.com/en/tutorials/es6/promises/#toc-chaining
- JavaScript promises: http://www.toptal.com/javascript/javascript-promises

Julia

- Static analysis: http://aosabook.org/en/500L/static-analysis.html
- Methods in Julia: http://julia.readthedocs.org/en/latest/manual/methods/
- Julia introspects: http://blog.leahhanson.us/julia-introspects.html
- Julia web stack: http://juliawebstack.org/

Lua

- Programming in Lua: http://www.lua.org/pil/contents.html
- Lua for programmers series: http://nova-fusion.com/2012/08/27/lua-for-programmers-part-1/
- http://learnxinyminutes.com/docs/lua/

PHP

- Comparison operators: http://php.net/manual/en/language.operators.comparison.php
- Get the type of a variable: http://php.net/manual/en/function.gettype.php
- var_dump: http://php.net/manual/en/function.var-dump.php
- var_export: http://php.net/manual/en/function.var-export.php
- count: http://php.net/manual/en/function.count.php
- print_r: print information about a variable, call with "true" to return the stuff.
- print_r versus var_dump: http://stackoverflow.com/questions/3406171/php-var-dump-vs-print-r
- Extending Exception: http://php.net/manual/en/language.exceptions.extending.php
- Incrementing/Decrementing operators: http://php.net/manual/en/language.operators.increment.php
- Slim Framework: http://www.slimframework.com/
- REST API for legacy PHP projects: http://www.toptal.com/php/building-rest-api-for-legacy-php-projects
- in_array: http://php.net/manual/en/function.in-array.php
- https://serversforhackers.com/video/php-fpm-multiple-resource-pools

Python

- marshmallow: Simplified Object Serialization - https://marshmallow.readthedocs.org/en/latest/
- Flask-RESTful: https://flask-restful.readthedocs.org/en/0.3.3/
- setuptools develop mode (also see, pip edtiable mode): http://stackoverflow.com/questions/19048732/python-setup-py-develop-vs-install
- Testing Flask applications: http://flask.pocoo.org/docs/0.10/testing/#testing-flask-applications
- Intermediate Python: https://github.com/yasoob/intermediatePython
- Data validation: https://github.com/alecthomas/voluptuous
- webargs: https://webargs.readthedocs.org/en/latest/
- dateutil: https://github.com/dateutil/dateutil/
- arrow: http://crsmithdev.com/arrow/
- Delorean: http://delorean.readthedocs.org/en/latest/
- Python job scheduling for humans: https://github.com/dbader/schedule
- Multiple dispatch in Python: http://multiple-dispatch.readthedocs.org/en/latest/index.html
- Concurrent I/O: https://curio.readthedocs.org/en/latest/tutorial.html
- RapidJSON: https://github.com/kenrobbins/python-rapidjson
- Working with binary data in Python: http://www.devdungeon.com/content/working-binary-data-python
- Pi3D: https://pi3d.github.io/html/ReadMe.html
- Folium: https://github.com/python-visualization/folium
- TinyDb: http://tinydb.readthedocs.org/en/latest/getting-started.html
- Profiling Python in production: https://nylas.com/blog/performance
- pipreqs: https://github.com/bndr/pipreqs
- https://github.com/Damnever/pigar
- https://github.com/DenisCarriere/geocoder
- https://julien.danjou.info/blog/2015/python-retrying
- Flask + Swagger: https://github.com/rochacbruno/flasgger
- Microservices framework: http://nameko.readthedocs.org/en/stable/#
- https://github.com/joerick/cibuildwheel


Rust

- [Why Rust?](http://www.oreilly.com/programming/free/why-rust.csp)
- [The Rust Programming Language Book](https://doc.rust-lang.org/nightly/book/)
- [On Rust's memory management](http://blog.zgtm.de/1)
- [Rust university course)[http://homepage.cs.uiowa.edu/~achampion/teaching/plc/lectures.shtml]

Scala

- Scala school: https://twitter.github.io/scala_school/

Swift language

- [Getting started](https://swift.org/getting-started/)
- [Swift at IBM](https://developer.ibm.com/swift/)

## Data Science/Optimization/Machine Learning/Evolutionary Algorithms

-  A few things to know about machine learning: https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf
-  Introduction to Decision trees: http://www.treeplan.com/chapters/introduction-to-decision-trees.pdf
-  Probabilistic programming and Bayesian methods for Hackers: http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/
-  A/B testing with Hierarchical models in Python: http://blog.dominodatalab.com/ab-testing-with-hierarchical-models-in-python/?utm_source=Python+Weekly+Newsletter&utm_campaign=147f4fa16a-Python_Weekly_Issue_205_August_20_2015&utm_medium=email&utm_term=0_9e26887fc5-147f4fa16a-312663333
-  Practical data mining with Python: https://dzone.com/refcardz/data-mining-discovering-and
-  Maching learning for developers: http://xyclade.github.io/MachineLearning/
-  PROBABILISTIC DATA STRUCTURES FOR WEB ANALYTICS AND DATA MINING: https://highlyscalable.wordpress.com/2012/05/01/probabilistic-structures-web-analytics-data-mining/
-  Pattern: https://github.com/clips/pattern
-  Neural networks and Deep learning: http://neuralnetworksanddeeplearning.com/
-  A course in machine learning: http://ciml.info/




## Kubernetes

- [Kubernetes on AWS workshop](https://github.com/arun-gupta/kubernetes-aws-workshop/blob/master/readme.adoc)

