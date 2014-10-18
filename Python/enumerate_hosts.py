"""
host[1-10].example.com => host1.example.com, host2.example.com,..
app[1,5,10].prod => app1.prod, app5,prod, app10.prod..
"""

def inst_enumerate(hosts):
    start = hosts.find('[')
    end = hosts.find(']')

    host_numstring = hosts[start+1:end]

    # handle range ([1-10])
    if '-' in host_numstring:
        host_nums = host_numstring.split('-')
        host_nums = range(int(host_nums[0]), int(host_nums[1])+1)
    # handle ind. host ids ([1, 10, 12])
    elif ',' in host_numstring:
        host_nums = [int(n) for n in host_numstring.split(',')]
    # handle single
    else:
        host_nums = [int(host_numstring)]

    for host_id in host_nums:
        print '%s%d%s'% (hosts[:start], host_id, hosts[end+1:])

for test_string in ['host[1].prod',
                    'host[1-10].example.com',
                    'app[1,5,10].prod',
                    'app[1,2,4]-kafka-kafka2.prod',
                    'a-pp[1,2,4]-kafka-kafka2.prod1.prod']:
    inst_enumerate(test_string)


