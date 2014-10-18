import sys
import filecmp
#http://docs.python.org/2/library/filecmp.html#module-filecmp

dc = filecmp.dircmp(sys.argv[1], sys.argv[2])
#print dc.report()
print 'Files/subdir only in {0}: {1}'.format(sys.argv[1], dc.left_list)
print 'Files/subdir only in {0}: {1}'.format(sys.argv[2], dc.right_list)
