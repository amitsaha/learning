"""
URL shortening recipe
http://stackoverflow.com/a/742047
"""

import string
alphabet = string.ascii_letters + string.digits

def db_id_to_string(id):
    """ 
    Map DB id to alphabet indices
    """
    base = len(alphabet)
    
    indices = []
    while id > 0:
        indices.append(id % base)
        id = id / base
    indices.reverse()
    return ''.join([alphabet[i] for i in indices])

def string_to_db_id(string):
    """
    Map string back to DB id
    """
    indices = [alphabet.find(c) for c in string]
    pos = len(indices) - 1
    id = 0
    for i in indices:
      id += i*len(alphabet)**pos
      pos -= 1
    return id

# Test
for i in range(0, 10**6):
    assert string_to_db_id(db_id_to_string(i)) == i

                                        
