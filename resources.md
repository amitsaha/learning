## Infrastructure/Platform/Workflow/Service Discovery

Ansible

- http://www.ansible.com/home

Elastic Search

- https://github.com/elastic/elasticsearch-definitive-guide
- Search results: https://www.elastic.co/guide/en/elasticsearch/reference/current/_the_search_api.html
- Supports different protocols besides HTTP
- Test script:

```
import requests
import json
import pprint

es = 'http://hostt:9200/'
query = '''
{'fields': ['field1', 'field2',],
 'filter': {'bool': {'must': [{'terms': {'field1': [1,
                                                   2]}},
                              {'bool': {'should': [{'term': {'field2': 'p'}},
                                                   {'bool': {'must': [{'term': {'field3': 'interesting'}},
                                                                     ]
                                                             }
                                                   }
                                                  ]
                                        }
                              }
                            ]
                    }
         }
'from': 0,
'query': {'match_all': {}},
'size': 100,
'search_type: 'scan',
}
        
'''
index = '/index-name'
method = '/_search'
payload = json.dumps(query)

res = requests.get(es + index + method, data=payload)
pprint.pprint(res.json())
```

Consul (Service discovery, DNS, Load balancing)

- http://www.consul.io/intro/

Git

- Git subtree: http://blogs.atlassian.com/2013/05/alternatives-to-git-submodule-git-subtree/
- Exclude a directory from git diff: http://stackoverflow.com/questions/4380945/exclude-a-directory-from-git-diff

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


Vault (Secret management)

- https://www.vaultproject.io/intro/getting-started/acl.html

Infrastructure testing

- Serverspec: http://serverspec.org/tutorial.html
- testinfra: https://testinfra.readthedocs.org/



## Web/APIs

- JSON API - http://jsonapi.org/
- Web API design - Crafting interfaces that developers love: http://apigee.com/about/resources/ebooks/web-api-design
- Designing for Performance: http://designingforperformance.com/

## Programming Languages

C

C++

Go

- The Little Go Book: http://openmymind.net/The-Little-Go-Book/
- An Introduction to Programming in Go: https://www.golang-book.com/books/intro
- TLS with Go: https://ericchiang.github.io/tls/go/https/2015/06/21/go-tls.html
- Docker based tool for go: https://github.com/treeder/go

Javascript

- Moment.js: http://momentjs.com/ (Dates)

PHP

- Comparison operators: http://php.net/manual/en/language.operators.comparison.php
- Get the type of a variable: http://php.net/manual/en/function.gettype.php
- var_dump: http://php.net/manual/en/function.var-dump.php
- var_export: http://php.net/manual/en/function.var-export.php
- count: http://php.net/manual/en/function.count.php
- Docs: http://php.net/manual/en/

Python

- marshmallow: Simplified Object Serialization - https://marshmallow.readthedocs.org/en/latest/
- Flask-RESTful: https://flask-restful.readthedocs.org/en/0.3.3/
- setuptools develop mode (also see, pip edtiable mode): http://stackoverflow.com/questions/19048732/python-setup-py-develop-vs-install
- Testing Flask applications: http://flask.pocoo.org/docs/0.10/testing/#testing-flask-applications
- Intermediate Python: https://github.com/yasoob/intermediatePython


## Data Science/Optimization/Machine Learning/Evolutionary Algorithms

-  A few things to know about machine learning: https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf
-  Introduction to Decision trees: http://www.treeplan.com/chapters/introduction-to-decision-trees.pdf
-  Probabilistic programming and Bayesian methods for Hackers: http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/
-  A/B testing with Hierarchical models in Python: http://blog.dominodatalab.com/ab-testing-with-hierarchical-models-in-python/?utm_source=Python+Weekly+Newsletter&utm_campaign=147f4fa16a-Python_Weekly_Issue_205_August_20_2015&utm_medium=email&utm_term=0_9e26887fc5-147f4fa16a-312663333


