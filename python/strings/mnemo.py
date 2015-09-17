import itertools

M = {2: 'ABC',
     3: 'DEF',
     4: 'GHI',
     5: 'JKL',
     6: 'MNO',
     7: 'PQRS',
     8: 'TUV',
     9: 'WXYZ'
     }

a = raw_input('Enter a number: ')
possible_combinations = [M.get(int(digit), digit) for digit in a]
print possible_combinations
for comb in itertools.product(*possible_combinations):
    print ''.join(comb)
    

