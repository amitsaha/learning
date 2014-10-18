import sys
import copy

class dirent:

    def __init__(self, entry, path_so_far=None):
        if entry != '*':
            self.entry = entry
        else:
            
        self.next = None
    
    def insert(self, entry):
        root = self
        path_so_far = []
        while 1:
            if root:
                if root.next:
                    if isinstance(root.entry, list):
                        path_so_far.extend(root.entry)
                    else:
                        path_so_far.append(root.entry)
                    root = root.next
                else:
                    break

        root.next = dirent(entry)
    
    def walk(self):
        root = copy.copy(self)
        while root:
            print root.entry
            root = root.next
            

def ls(path):
    root = dirent('/')
    for dent in path.split('/'):
        if dent:
            root.insert(dent)
    root.walk()

ls(sys.argv[1])
