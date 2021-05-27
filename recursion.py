1.
Question 1
What is recursion used for?

1 / 1 point


Recursion lets us tackle complex problems by reducing the problem to a simpler one.


Correct
You nailed it! By reducing the problem to a smaller one each time a recursive function is called, we can tackle complex problems in simple steps.

2.
Question 2
Which of these activities are good use cases for recursive programs? Check all that apply.

1 / 1 point

Going through a file system collecting information related to directories and files.

Correct
Right on! Because directories can contain subdirectories that can contain more subdirectories, going through these contents is a good use case for a recursive program.


Managing permissions assigned to groups inside a company, when each group can contain both subgroups and users.

Correct
You got it! As the groups can contain both groups and users, this is the kind of problem that is a great use case for a recursive solution.



3.
Question 3
Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. Note: base is assumed to be a positive number. Tip: for functions that return a boolean value, you can return the result of a comparison.

1 / 1 point

def is_power_of(number,base):
    if number == base:
        return True
    elif number < base:
        return False
    return is_power_of(number / base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

Correct
Nice job! You've made the code check for powers of numbers
by reducing the problem to a smaller one.

4.
Question 4
The count_users function recursively counts the amount of users that belong to a group in the company system, by going through each of the members of a group and if one of them is a group, recursively calling the function and counting the members. But it has a bug! Can you spot the problem and fix it?

1 / 1 point

def count_users(group):
  count = 0
  for member in get_members(group):
    count += 1
    if is_group(member):
      count += count_users(member)-1
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18

Correct
Well done, you! You spotted the problem that was causing
groups to be counted when we only wanted to count users!


5.
Question 5
Implement the sum_positive_numbers function, as a recursive function that returns the sum of all positive numbers between the number n received and 1. For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.

1 / 1 point

def sum_positive_numbers(n):
  if n <= 1:
      return n
  return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

Correct
Here is your output:
6
15

Great work! You've really nailed writing recursive
functions!



Question
The function sum_positive_numbers should return the sum of all positive numbers between the number n received and 1. For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15. Fill in the gaps to make this work:


def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n - 1)

print(sum_positive_numbers(3)) # Should be 6


Here is your output:
6
15

Whoohoo! You've just written your first recursive function.
Well done!


#Question
Which of the following scenarios would benefit the most from using a recursive function to solve the problem?

You need to create a family tree, showing several generations of your ancestors, with all of their children.

Correct
Great job! You're getting the concept of recursion and when it's a better solution than the traditional looping techniques.



#Additional Recursion Sources
#Additional Recursion Sources
In the past videos, we visited the basic concepts of recursive functions.

A recursive function must include a recursive case and base case. The recursive case calls the function again, with a different value. The base case returns a value without calling the same function.

A recursive function will usually have this structure:


def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)


For more information on recursion, check out these resources:

Wikipedia Recursion page
See what happens when you Search Google for Recursion




