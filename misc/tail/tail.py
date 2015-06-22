import sys
import os
def tail(lines_to_read, fname):

    if fname != 'stdin':
        fsize = os.stat(fname).st_size
        num_bytes = 2
        with open(fname) as f:
            data = []
            while True:
                # we have read the entire file
                # and if we still don't have the number of lines asked for
                # exit
                if num_bytes > fsize:
                    break
                f.seek(fsize-num_bytes)
                c = f.read(1)
                data.append(c)
                num_bytes += 1
                if data.count('\n') >= lines_to_read:
                    break
        data = ''.join(data[::-1])        
    else:
        data = ''.join(sys.stdin.readlines()[-lines_to_read:])
    return data

# test
output = tail(10, 'tail.py')
assert output.count('\n') == 10
output = tail(1, 'tail.py')
assert output.count('\n') == 1
# Attempt reading more number of lines than
# exists in the file
output = tail(100, 'tail.py')
assert output.count('\n') == 38

#cat tail.py | python tail.py
print(tail(10, 'stdin'))

