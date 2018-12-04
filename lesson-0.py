# Lesson 0:  Write a program that prints "hello world".

# You probably noticed is that this is not lesson 1, it's lesson 0.  Why lesson zero, well in
# computers things start with zero, not one.

# A couple of details before we get going, at various times I'll suggest that you "run" the program.  To do that you
# can use the right mouse button (or control-click on a trackpad) to pop up a menu and select the "run lesson-0.py"
# item about 2/3's of the way down. After the first time you've run a file you can re-run that file using the green
# triangle/arrow in the upper right corner.


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

# print(Hello world.)

# what happened?  did you see the red?  That means that python does not like it and that it won't run.  If you try
# to run it you will get an error (or 3!).

# you need to use the quotes to tell python that it's a string and not something else.  Go ahead and comment out that
# line above with the red underlines, (I call that ketchup, if you've got ketchup it won't run.)

# The next concept is a variable.  You can think of a variable as a named spot you can put something, kind of like
# a chest in minecraft but you can only put one thing in it.
# The lines below use a variable to do the same thing as at the beginning. print() looks at the value of the variable
# it is passed and will print that.

# uncomment the lines below and see what happens when you run this.  (Make sure you have fixed the ketchup above.)

a = "Hello World."  # leave this line because you'll need it below
# print(a)

# did it print out "Hello world."?  did it do it twice?  Why twice?  You can comment out the earlier stuff as you
# go so that it doesn't get run again.  Hint, putting a '#' at the beginning of a line will comment that line out.

# A few more things about strings:  Strings can contain letters, numbers, spaces and punctuation.  A string
# that contains only numbers is NOT a number, it's just a string with some numbers in it. When you add strings
# together you connect them end-to-end, that's called concatenating.   To add them together you would use b + b.
# you cannot "divide" strings b/b has no meaning in when b contains a string and will generate an error.
# let's practice a bit:

# uncomment these lines to see what happens
b = "2"
# print(b + b)

# this is the integer 2 and that's a lot different from the string "2".  You can add, subtract, multiply and
# divide integers. integers are whole numbers!  there is not fractional part.  if you assign 2.9 to an integer
# you get 2, note that you get 2 and not 3, it doesn't round the number to the nearest integer, it discards
# or truncates the fractional part.
c = 2
# print(c + c)

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


# try this!!!
h = "Hello"
w = "world"

print(h + " " + w + ".")

# ok, now write a little program (probably one or two lines) that will print out "hello world"
# maybe try a couple of variations, using string concatenation.
