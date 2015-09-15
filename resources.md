*Table of contents*

- [Infrastructure/Platform/Workflow](#infraworkflow)
- [Web/APIs](#webapis)
- [Programming Languages](#programming-languages)
- [Data Science/Optimization/Machine Learning/Evolutionary Algorithms](#data-scienceoptimizationmachine-learningevolutionary-algorithms)
- [Talks](#talks)


## Infrastructure/Platform/Workflow

Ansible

- http://www.ansible.com/home

Elastic Search

- https://github.com/elastic/elasticsearch-definitive-guide
- Search results: https://www.elastic.co/guide/en/elasticsearch/reference/current/_the_search_api.html
- Supports different protocols besides HTTP

Consul (Service discovery, DNS, Load balancing)

- http://www.consul.io/intro/

Git

- Git subtree: http://blogs.atlassian.com/2013/05/alternatives-to-git-submodule-git-subtree/
- Exclude a directory from git diff: http://stackoverflow.com/questions/4380945/exclude-a-directory-from-git-diff
- Git garbage collection: http://think-like-a-git.net/sections/graphs-and-git/garbage-collection.html
- Gc and Pruning: http://alblue.bandlem.com/2011/11/git-tip-of-week-gc-and-pruning-this.html
- Git - Maintenance and data recovery: https://git-scm.com/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery
- Git is a purely functional data structure: http://www.jayway.com/2013/03/03/git-is-a-purely-functional-data-structure/

Vagrant

- https://www.vagrantup.com/

Linux Containers/Sandboxing/VMs

- https://www.docker.com/
- Docker machine: https://docs.docker.com/machine/
- Docker compose: https://docs.docker.com/compose/
- DNS for docker: https://github.com/tonistiigi/dnsdock
- libvirt Sandbox: http://sandbox.libvirt.org/download/
- Docker toolbox: https://www.docker.com/toolbox

SSH

- How to disable host key checking? http://linuxcommando.blogspot.com.au/2008/10/how-to-disable-ssh-host-key-checking.html
- Permissions for .ssh: http://superuser.com/questions/215504/permissions-on-private-key-in-ssh-folder

httpie

- https://github.com/jkbrzt/httpie
- By deafault httpie encodes stuff as strings, but if the data type is to be preserved, use ``:=``

Miscellaneous

- Bash alias with parameters: http://stackoverflow.com/questions/7131670/make-bash-alias-that-takes-parameter
- ``arc`` (CLI for phabricator): https://secure.phabricator.com/book/phabricator/article/arcanist/
- ``arc`` updating an existing patch: https://phab.enlightenment.org/w/arcanist/#update-an-existing-patch
- ``JSONView`` Firefox plugin for pretty viewing JSON (https://addons.mozilla.org/en-us/firefox/addon/jsonview/)
- The magic of consistent hashing: http://www.paperplanes.de/2011/12/9/the-magic-of-consistent-hashing.html

Jenkins

- jenkins-job-builder: http://jenkins-job-builder.readthedocs.org/
- Jenkins job DSL plugin: https://github.com/jenkinsci/job-dsl-plugin

Puppet

- Courseware learning VM: https://github.com/puppetlabs/courseware-lvm
- Puppet cookbook: http://www.puppetcookbook.com/
- Puppet nginx: https://github.com/jfryman/puppet-nginx


Vault (Secret management)

- https://www.vaultproject.io/intro/getting-started/acl.html

Infrastructure testing

- Serverspec: http://serverspec.org/tutorial.html
- testinfra: https://testinfra.readthedocs.org/



## Web/APIs

- JSON API - http://jsonapi.org/
- Web API design - Crafting interfaces that developers love: http://apigee.com/about/resources/ebooks/web-api-design
- Designing for Performance: http://designingforperformance.com/
- REST and long running jobs: http://farazdagi.com/blog/2014/rest-long-running-jobs/
- Testing services without running tests: https://blog.twitter.com/2015/diffy-testing-services-without-writing-tests
- Webhook server: http://avoidwork.github.io/rozu/
- Gzip compression: http://betterexplained.com/articles/how-to-optimize-your-site-with-gzip-compression/
- thrift-tools: Inspecting thrift traffic - https://github.com/pinterest/thrift-tools


## Programming Languages

C

C++

Golang

- The Little Go Book: http://openmymind.net/The-Little-Go-Book/
- An Introduction to Programming in Go: https://www.golang-book.com/books/intro
- TLS with Go: https://ericchiang.github.io/tls/go/https/2015/06/21/go-tls.html
- Docker based tool for go: https://github.com/treeder/go
- Awesome go: https://github.com/avelino/awesome-go/blob/master/README.md
- How to write Go code: https://golang.org/doc/code.html
- Go Books: https://github.com/dariubs/GoBooks
- Learning Go: http://www.miek.nl/go/
- Golang Channels Tutorial: http://guzalexander.com/2013/12/06/golang-channels-tutorial.html

Javascript

- Moment.js: http://momentjs.com/ (Dates)

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

Python

- marshmallow: Simplified Object Serialization - https://marshmallow.readthedocs.org/en/latest/
- Flask-RESTful: https://flask-restful.readthedocs.org/en/0.3.3/
- setuptools develop mode (also see, pip edtiable mode): http://stackoverflow.com/questions/19048732/python-setup-py-develop-vs-install
- Testing Flask applications: http://flask.pocoo.org/docs/0.10/testing/#testing-flask-applications
- Intermediate Python: https://github.com/yasoob/intermediatePython
- Data validation: https://github.com/alecthomas/voluptuous
- Intermediate Python: https://github.com/yasoob/intermediatePython/blob/master/README.md
- Python implementation of thrift: https://github.com/eleme/thriftpy


## Data Science/Optimization/Machine Learning/Evolutionary Algorithms

-  A few things to know about machine learning: https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf
-  Introduction to Decision trees: http://www.treeplan.com/chapters/introduction-to-decision-trees.pdf
-  Probabilistic programming and Bayesian methods for Hackers: http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/
-  A/B testing with Hierarchical models in Python: http://blog.dominodatalab.com/ab-testing-with-hierarchical-models-in-python/?utm_source=Python+Weekly+Newsletter&utm_campaign=147f4fa16a-Python_Weekly_Issue_205_August_20_2015&utm_medium=email&utm_term=0_9e26887fc5-147f4fa16a-312663333


### Talks

Concurrency is not Parallellism: http://blog.golang.org/concurrency-is-not-parallelism

- World is not object oriented, it's parallel
- Concurrency: composition of independently executing things, managing a lot of stuff going on together, interacting
- Parallel: simultaneous execution of things, related or not, doing things in parallel
- Concurrency: structure, parallelism: execution
- Concurrency: structure a thing, may be you can parallelize, goal is not parallelism (3:00)
- Concurrency: structure a program into pieces and communicate between them

