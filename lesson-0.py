# Lesson 0:  Write a program that prints "hello world".

# You probably noticed is that this is not lesson 1, it's lesson 0.  Why lesson zero, well in
# computers things start with zero, not one.

# A couple of details before we get going, at various times I'll suggest that you "run" the program.  To do that you
# can use the right mouse button to pop up a menu and select the "run lesson-0.py" item about 2/3's of the way down.
# After the first time you've run a file you can re-run that file using the green triangle/arrow in the upper right
# corner.


# The first thing we are going to do is the legendary first program done in many programming languages: "Hello world."
# it's pretty easy:

print("Hello World.")

# There, that was easy.
# There are two important concepts in this, strings and the print() function.
# the print() function writes the value of whatever is inside the parenthesis to
# standard output, "standard output" is a fancy name for the screen that you see.
#
# The second concept is a string, a string is a sequence of characters, characters are letters, numbers and symbols.
# Strings are surrounded by quotes: "", without that the words would be treated as variables and you'd get an error.

# the '#' tells python that the rest of the line is a comment, you've probably noticed that this line and all of the
# instructions also have these things.  Uncomment the line below and see what happens.  To uncomment it means to
# delete the '# ' at the beginning of the line.

# print(hello world)

# what happened?  did you see the red?  That means that python does not like it and that it won't run.  If you try
# to run it you will get an error (or 3!).



a = "this is a string"
# this is also a string, NOT a number, or more specifically an integer.  When you add strings together you
# connect them end-to-end, that's called concatinating.   To add them together you would use b + b.
# you cannot "divide" strings b/b has no meaning in when b contains a string and will generate an error
b = "2"

# this is the integer 2 and that's a lot different from the string "2".  You can add, subtract, multiply and
# divide integers. integers are whole numbers!  there is not fractional part.  if you assign 2.9 to an integer
# you get 2, note that you get 2 and not 3, it doesn't round the number to the nearest integer, it discards
# or truncates the fractional part.
c = 2

# uncomment this line and run it, see if it does what you think it will do
# print("this is a string")

# or you can do this, printing the variable that contains the value "this is a string"
# uncomment this line and run it, see if it does what you think it will do

# what do you think this will do?  uncomment the line and run it.
# print(a)

# what do you think this will do?  uncomment the line and run it.
# print("a")

# what do you think this will do?  uncomment the line and run it.
# print(a + a)

# what do you think this will do?  uncomment the line and run it.
# print("a + a")


# what do you think this will do?  uncomment the line and run it.
# print(b + b)

# what do you think this will do?  uncomment the line and run it.
# print(c + c)

# think about the difference between b + b and c + c


# now write a little program (probably one or two lines) that will print out "hello world"
