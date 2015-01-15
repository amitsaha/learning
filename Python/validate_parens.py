# Find if a string has valid parenthesis
# The program understands, (), {}, []
# Time complexity: O(n)
# Space: O(n)

def isvalid(s):
    parens = {
        '(':')',
        '{':'}',
        '[':']'
    }
    stack = []

    for c in s:
        if c in parens.keys() or c in parens.values():
            # if stack is empty
            if not stack:
                if c in parens.keys():
                    stack.append(c)
                else:
                    # if stack is empty and the first paren
                    # we encounter is a closed paren
                    return 'Invalid'
                    break
            else:
                if c in parens.keys():
                    # if we encounter a open paren, we must have another open
                    # paren at the stack top
                    if stack[-1] in parens.values():
                        return 'Invalid'
                        break
                    stack.append(c)
                elif c in parens.values():
                    # the paren this is closing must be the corresponding
                    # open paren at the stack top
                    if parens[stack[-1]] != c:
                        return 'Invalid'
                        break
                    stack.pop()
    else:
        if not stack:
            return 'Valid'
        else:
            return 'Invalid. Stack {0}'.format(stack)

# test strings
for test_string in ['abc',
                    '(abc)',
                    '(abc',
                    '{[abc]}',
                    '{{}}',
                    '[{}])',
                    '[abc][aded]{cde}()',
                    '([{}])',
                    ]:
    print test_string, ':', isvalid(test_string)






