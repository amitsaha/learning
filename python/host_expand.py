#We have a system that manages hosts. Currently, it requires host names to be explicitly listed, which is cumbersome when you have thousands of hosts.

#We would like to simplify the host name input to use a bracket notation that allows a set of hosts to be defined. E.g.

#app[1,3].prod would translate to app1.prod, app3.prod
#app[1,5,6].prod would translate to app1.prod, app5.prod, app6.prod
#Write a function that would translate the host name with bracket notation to the full set of hosts.

# test cases
#app[1,5,10].prod
#app[1,2,4]-kafka-kafka2.prod
#a-pp[1,2,4]-kafka-kafka2.prod
# a-pp[1,2,4]-kafka-kafka2.prod1.prod
# a-pp[1,2,98]-kafka-kafka2.prod1.prod

# O(n) + O(n1) + O(n2) = O(n)
def hosts_list(bracket_host_name):
  """ Returns the full list of hosts specified by bracket_host_name """
  
  hostnums = []
  seen = False
  
   hostnames = ''
   domain = ''
   seen = False
   # O(n)
   for t in bracket_host_name:
       if t == ']':
            seen = True          
      
       # O(1) assuming I use lists
       if not seen:
           hostnames += t
       else:
           domain += t        
 
  # O(n1)
  hostname = hostnames.split('[')[0] 
  # O(n1) + O(1) + O(n1)
  hostnums = hostnames.split('[')[1].rstrip(']').split(',')  
  # construct the explicit hostnames
  # O(n2)
  hostnames = [''.join([hostname, n, ,'.', domain]) for n in hostnums]
      
  return hostnames 


# pat = re.compile(r'[\d+,\,*]')
# >>> pat.findall('[1,2]')
# ['1', ',', '2']#


