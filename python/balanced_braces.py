'''
Given a file consisting of {'s and }'s find it the file is balanced or not
'''

#first approach, sequential
def check_balance(file):
    counter = 0
    with open(file) as f:
        while True:
            c = f.read(1)
            if c:
                if c == '{':
                    counter += 1
                if c == '}':
                    counter -= 1
            else:
                break
            if counter < 0:
                return 'Imbalanced'
    if counter == 0:
        return 'Balanced'
    else:
        return 'Imbalanced'

# parallelize such that the file is really large and has
# to be processed on multiple computers


print check_balance('braces_1.txt')
print check_balance('braces_2.txt')

            
            
