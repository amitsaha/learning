'''
Merge N sorted files into 1 sorted file
Based on http://stackoverflow.com/questions/5055909/algorithm-for-n-way-merge
'''

def merge(*args):
    # final merged file
    final = open('final_sorted.dat', 'w')
    # file objects
    fobjs = [open(f) for f in args]
    while True:
        cur_pos = [fobj.tell() for fobj in fobjs]
        least = [(i, fobj.readline().strip('\n')) for i, fobj in enumerate(fobjs) if fobj]
        least = filter(lambda x:x[1], least)
        # Insert the smallest of these in the final list
        least.sort(key=lambda x: float(x[1]))
        if least:
            f_num, elem = least[0]
            final.write(str(elem)+'\n')
            # reset the file pointers for the other files
            # which did not have the smallest
            [fobj.seek(cur_pos[i]) for i, fobj in enumerate(fobjs) if i!=f_num]
        else:
            break

    final.close()

# test data
merge('test1.dat', 'test2.dat', 'test3.dat')
with open('final_sorted.dat') as f:
    print ''.join(f.readlines())
