'''
Print all anagrams of the input word.

The anagrams are built from the /usr/share/dict/words on my
Linux system. A local copy is here. Sample output:

> python find_anagrams.py
Enter a word: conserve
['conserve', 'converse']


'''
from collections import defaultdict

# create a dictionary with the default value being an empty list
table = defaultdict(list)

# This function will create a table like this:
# ..

# aceiinnoorssttv ['conservationist', 'conversationist']
# ..
# ..
def build_table():
    with open('usr_share_dict_words.txt') as f:
        for line in f:
            line = line.rstrip('\n')
            table[''.join(sorted(line))].append(line)

# build the table
build_table()
word = raw_input('Enter a word: ')
# Look this word up in the above table
print table[''.join(sorted(word))]
