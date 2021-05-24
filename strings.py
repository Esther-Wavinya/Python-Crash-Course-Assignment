Modify the double_word function so that it returns the same word repeated twice, followed by the length of the new doubled word. For example, double_word("hello") should return hellohello10.


def double_word(word):
    return word * 2 + str(len(word * 2))


print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0


Want to give it a go yourself? Be my guest! Modify the first_and_last function so that it returns True if the first letter of the string is the same as the last letter of the string, False if they’re different. Remember that you can access characters using message[0] or message[-1].
Be careful how you handle the empty string, which should return True since nothing is equal to nothing.


def first_and_last(message):
    if len(message) == 0:
        return True
    elif message[0] == message[-1]:
        return True
    else:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))


Try using the index method yourself now!


Using the index method, find out the position of "x" in "supercalifragilisticexpialidocious".


word = "supercalifragilisticexpialidocious"
word.index("x")
print()


Want to try some string methods yourself? Give it a go!


Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received, in upper case. For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.


def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS



Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam". For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".


def student_grade(name, grade):
	return ("{} received {}% on the exam" .format(name, grade))

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))



1.
Question 1
The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.

1 / 1 point

def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for string in input_string.lower():
        # Add any non-blank letters to the 
        # end of one string, and to the front
        # of the other string. 
        if string.replace(" ",""):
            new_string = string + new_string
            reverse_string = string + reverse_string
            
    # Compare the strings
    if new_string[::-1]==reverse_string:
        return True
    return False
print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True



2.
Question 2
Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".

1 / 1 point

def convert_distance(miles):
    km = miles * 1.6 
    result = "{} miles equals {:.1f} km".format(miles,km)
    return result


print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km



3.
Question 3
If we have a string variable named Weather = "Rainfall", which of the following will print the substring or all characters before the "f"?

1 / 1 point


print(Weather[:4])




4.
Question 4
Fill in the gaps in the nametag function so that it uses the format method to return first_name and the first initial of last_name followed by a period. For example, nametag("Jane", "Smith") should return "Jane S."

1 / 1 point

def nametag(first_name, last_name):
  
    return "{} {last_name}.".format(first_name, last_name=last_name[0])



print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 




5.
Question 5
The replace_ending function replaces the old string in a sentence with the new string, but only if the sentence ends with the old string. If there is more than one occurrence of the old string in the sentence, only the one at the end is replaced, not all of them. For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc. The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made). 

1 / 1 point

def replace_ending(sentence, old, new):
  # Check if the old string is at the end of the sentence 
    if sentence.endswith(old):
    # Using i as the slicing index, combine the part
    # of the sentence up to the matched string at the 
    # end with the new string
        i=len(sentence) 
        l=len(old)
        new_sentence = sentence[0:i-l] + new
        return new_sentence

    # Return the original sentence if there is no match 
    return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"









