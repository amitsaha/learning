import difflib

class Repository:
    
    def __init__(self, fname=None):
        if not fname:
            fname = '/usr/share/dict/words'
        with open(fname) as f:
            self.repository = [x.rstrip('\n') for x in f.readlines()]
            
def find_close_matches(r, w, count=3):
    return difflib.get_close_matches(w, r.repository, count)

if __name__ == '__main__':
    r = Repository()
    w = raw_input('Your word please: ')
    if len(w.split()) != 1:
        sys.exit('please enter a word only')
    try:
        count = int(raw_input('Number of matches: '))
    except ValueError:
        sys.exit('Enter a number please')
    
    
    print find_close_matches(r, w, count)
