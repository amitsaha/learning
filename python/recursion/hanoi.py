peg1 = [1,2,4,5]
peg2 = []
tmp = []

def move(peg1, peg2):
    peg2.append(peg1.pop())

def hanoi(n, peg1, peg2, tmp):
    if n == 1:
        move(peg1, peg2)
        return
    hanoi(n-1, peg1, tmp, peg2)
    hanoi(1, peg1, peg2, tmp)
    hanoi(n-1, tmp, peg2, peg1)

hanoi(len(peg1), peg1, peg2, tmp)
print peg1
print peg2
