# lesson 2
#
# This lesson is about the python 'list' container.  A list is like a shopping list where you put one item
# on each line of a sheet of paper.  The items are in the order that they were added or declared and you can
# examine each of them.  You can put numbers (floats or integers) or strings or even "other things" into a list.
# we'll cover what "other things" means later.
#
# here's a simple list (leave this uncommented, the code snippets below won't work without it):

shopping_list = ["milk", "eggs", "bread"]

# you can print out the whole list:
# print("the shopping list is", shopping_list)



# a 'for' loop is a looping structure like a 'while' loop but with some key differences:
# a while loop tests something each time it passes through the loop. like this (I'm assuming you're familiar with
# while loops.):
# i = 0
# while i < len(shopping_list):
#   print("I need to get", shopping_list[i])
#   i += 1

# A for loop has a variable, the thing after 'for', which takes on each value in a list.
# In this case 'item' will take on each value in 'shopping_list'.  This is much easier than
# using a while loop.  With computers 'easy' means better, less likely to break.
#
# for item in shopping_list:
#     print("I need to get", item)

# That is called "iterating" over the items in the list.

# Here's another way to print out what you need to get:
#
# all_items = ""
# for item in shopping_list:
#     if all_items == "":
#         all_items = item
#     else:
#         all_items = all_items + ", " + item
#
# print("I need to get", all_items)
#

# you can append to a list like this:

# shopping_list.append("yogurt")
#
# print("The new list is", shopping_list)

# let's put the code for joining the list into "all_items" into a function, I'm just copying it from above:
#


# def print_items(my_list):
#     all_items = ""
#     for item in shopping_list:
#         if all_items == "":
#             all_items = item
#         else:
#             all_items = all_items + ", " + item
#
#     print("I need to get", all_items)
#
# print_items(shopping_list)


# a list can also contain numbers:

# prime_list = [1, 3, 5, 7, 11, 13, 17, 19]
#
# sum_of_primes = 0
# for prime in prime_list:
#     sum_of_primes += prime
#
# print("the sum of the first", len(prime_list), "primes is", sum_of_primes)


# Now write a function that multiplies all of the primes in prime_list together and prints out the
# result.





