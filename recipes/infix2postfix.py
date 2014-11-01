'''
Convert an infix expression to postfix expression
'''

op_priority = {'+':1,
               '-':1,
               '*':2,
               '/': 2}

def has_highprio(op1, op2):
    return op_priority[op1] > op_priority[op2]
    
def infix2prefix(expr):
    
    op_stack = []
    postfix_expr = []
    operators = ['+', '-', '*', '/']

    for c in expr:
        if c not in operators:
            postfix_expr.append(c)
        else:
            while True:
                if not op_stack:
                    op_stack.append(c)
                    break
                else:
                    top_op = op_stack[-1]
                    if has_highprio(top_op, c):
                        postfix_expr.append(op_stack.pop())
                    else:
                        op_stack.append(c)
                        break
    # empty the operator stack
    while op_stack:
        postfix_expr.append(op_stack.pop())
    print ''.join(postfix_expr)

infix2prefix('a+b')
infix2prefix('a+b*c')
infix2prefix('a+b*c/d')
infix2prefix('a+b*c-d')
infix2prefix('3+4*2/(1-5)')
