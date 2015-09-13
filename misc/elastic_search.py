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
        

index = '/index-name'
method = '/_search'
payload = json.dumps(query)

res = requests.get(es + index + method, data=payload)
pprint.pprint(res.json())
