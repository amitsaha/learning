# reverse a number

def reverse(number):
    rev = 0
    while number > 0:
        rev = rev*10 + number%10
        number = number/10

    print rev

reverse(1551)
reverse(1550)
