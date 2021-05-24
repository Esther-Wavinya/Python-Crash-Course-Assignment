Using the "split" string method from the preceding lesson, complete the get_word function to return the {n}th word from a passed sentence. For example, get_word("This is a lesson about lists", 4) should return "lesson", which is the 4th word in this sentence. Hint: remember that list indexes start at 0, not 1.


def get_word(sentence, n):
       # Only proceed if n is not more than the number of words
       sentence = sentence.split(" ")
       if n <= len(sentence) and n>0:
        return(sentence[n-1])  
       else:
           return ""
print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing



The skip_elements function returns a list containing every other element from an input list, starting with the first element. Complete this function to do that, using the for loop to iterate through the input list.


def skip_elements(elements):
        # Initialize variables
        new_list = []
        i = 0

        # Iterate through the list
        for words in elements:

            # Does this element belong in the resulting list?
            if i <= len(elements):
                # Add this element to the resulting list
                new_list.append(elements[i])
            # Increment i
                i += 2

        return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []




Let's use tuples to store information about a file: its name, its type and its size in bytes. Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places. 


def file_size(file_info):
  	itsname, itstype, itssize= file_info
	return("{:.2f}".format(itssize / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21




Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is on an even position or an odd position.


def skip_elements(elements):
    # code goes here
    element = []
    for i, e in enumerate(elements):
        if i % 2 == 0:
            element.append(e)
    return element

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']



The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. Fill in the blanks in the function, using list comprehension. Hint: remember that list and range counters start at 0 and end at the limit minus 1.


def odd_numbers(n):
  	return [x for x in range(0, n+1) if x%2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []


1.
Question 1
Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

1 / 1 point

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [word.replace("hpp","h") if word.endswith("hpp") else word for word in filenames ]
 

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]



2.
Question 2
Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.

1 / 1 point


def pig_latin(text):
  say = []
  # Separate the text into words
  words = text.split(" ")
  for word in words:
    # Create the pig latin word and add it to the list
    say.append(word[1:]+word[0]+'ay')
    # Turn the list back into a phrase
  return " ".join(x for x in say)
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"



3.
Question 3
The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
For example: 
640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"
Fill in the blanks to make the code convert a permission in octal format into a string format.

1 / 1 point


def octal_to_string(octal):
 result = ""
 value_letters = [(4,"r"),(2,"w"),(1,"x")]
 # Iterate over each of the digits in octal
 for i in [int(n) for n in str(octal)]:
    # Check for each of the permissions values
    for value, letter in value_letters:
        if i >= value:
            result += letter
            i -= value



4.
Question 4
Tuples and lists are very similar types of sequences. What is the main thing that makes a tuple different from a list?

1 / 1 point



A tuple is immutable



Correct
Awesome! Unlike lists, tuples are immutable, meaning they can't be changed.

5.
Question 5
The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.

1 / 1 point


def group_list(group, users):

  members =", ".join(users) 

  return(" {}: {}".format(group, members))

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"





6.
Question 6
The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that. 

1 / 1 point


def guest_list(guests):
	count = 0
	if count < 3:
		for guest in guests:
			name, age, job = guest
			print("{} is {} years old and works as {}".format(name, age, job))
			count = count + 1
guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])





