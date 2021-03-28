#test program for python to parse and execute

import os, sys


def fact(a):
 """
 function to compute the factorial of a number.
 Inputs:
    a: int, a number for which to compute the factorial
 Outputs:
    a: int, the factorial of the input a
 """
 if a > 100:
  # if a number is given that's too high, raise error. max recursion depth is something like 1000 anyway I think but you'd get integer overflow before that
  raise Exception("number too high: {0}".format(a))
 if a > 1:
  # if a > 1, then we need to go again, multiply current number by the factorial of the previous number
  a *= fact(a - 1)
 # if a == 1, then we've iterated all numbers and can return the final number
 return a

# get the given number from the commandline arguments, argv.
number = sys.argv[-1] # [-1] means the last element of the list, in this case will be equiv to argv[1], as argv[0] by convention is the name of the program

# assign the total of the fact() function to varname 'total'
total = fact(float(number))

# print the result
print("you entered {0}, factorial of that is {1}".format(number, total))
