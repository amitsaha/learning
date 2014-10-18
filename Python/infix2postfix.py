import sys

infix_exp = sys.argv[1]

stack = list()
operators = {'*':1,
             '-':0,
             '/':1,
             '+':0,
             '(':-1,
             }

for term in infix_exp:
    if term not in operators:
        print term,
    else:
        if stack:
            op = stack[-1]
            while operators[op] >= operators[term]:
                op = stack.pop()
                print op,
                if stack:
                    op = stack[-1]
                else:
                    break
        stack.append(term)

# pop until the stack is empty
while stack:
    print stack.pop(),
