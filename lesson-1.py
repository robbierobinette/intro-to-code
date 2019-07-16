# This lesson will cover some mathematical operators in python.  These operators will be needed for the next lesson.
#
# uncomment this line and run it:
# print(7 / 3)
# what did it print out?  Was that what you expected?
#
# re-comment the line above and then uncomment the line below and see what happens.
# print(7 // 3)
#
# was that what you expected?  The reason that these answers are different is that in python '/' is the "floating point"
# division operator.  '//' is the integer division operator.  In floating point division it converts each number to a
# floating point number (something that can have a fractional part) and then does the division.
# Integer division divides two numbers using "whole number math" (known as integers in computer science).  when you
# divide 7 by 3 using whole numbers you get 2 and 1/3.  Since integers can't contain fractional parts the fraction is
# discarded and you end up with just 2.  Note that any fractional part is discarded, not rounded.  if you try to
# put 0.99 into an integer you get 0, not 1!
#
# Now for a new operator:  %, this is pronounced 'mod' or 'modulus'.  it is the 'remainder' after integer division:
# uncomment this line and run it:
# print (7 % 3)
#
# what did you get?  is that what you expected?
# now write a function takes a dividend and a divisor and prints the result as a fraction (not a decimal)
# so, 7 (dividend) divided by 3 (divisor) would yield "2 + 1/3"
#
# here is the framework for the function:  (uncomment it and fill it in)
# the word 'pass' is in the function because when you declare a function you have to have
# some code within it or python thinks it's an error.  'pass' is just some code that does
# nothing so that the function isn't completely empty.

# def divide(dividend, divisor):
#     pass
#
# uncomment this to call the function you just wrote.
# divide(7, 3)





