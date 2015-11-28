-- http://learnyouahaskell.com/starting-out

-- A function with a single argument
doubleMe x = x*2

-- A function with two arguments, which calls the previous function
doubleUs x y = doubleMe x + doubleMe y

-- A function with a conditional
doubleSmallNumber x = if x > 100 then x else doubleMe x

-- function without arguments
something = "Something!"

-- Simple list
aList = [1,2,3,4]

-- Adding a list to another
bList = 1:2:3:aList

-- Get the 5th element from bList using bList !! 4
item = bList !! 4

-- Get the length of a list using length bList
len = length bList

-- reverse a list
reversedbList = reverse bList

-- extract N elements from the beginning of a list using take function
takeNfrombList n = take n bList

-- Miscelanneous functions for lists: maximum, minimum, sum, product

-- Check if an element is in a list
checkIf x = elem x bList

-- Ranges in list
-- Example 1: [1..20] will create a list of the numbers 1 to 20
-- Example 2: [1,3..20] will create a list, 1,3,5,7..19
-- Example 3: [1,3..] will create an infinite list, take first 50 odd numbers, just do take 50 [1,3..]

-- List comprehensions

