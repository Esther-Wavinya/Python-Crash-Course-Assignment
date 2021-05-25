The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following: 	
1) Add an entry for Epilogue on page 39. 	
2) Change the page number for Chapter 3 to 24. 	
3) Display the new dictionary contents. 	
4) Display True if there is Chapter 
5, False if there isn't.

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents?
print("Chapter 5" in toc) # Is there a Chapter 5?



Now, it's your turn! Have a go at iterating over a dictionary!

 Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember that the items method returns a tuple of key, value for each element in the dictionary.

 cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for beast, feature in cool_beasts.items():
    print("{} have {}".format(beast, feature))


    Here is your output:
octopuses have tentacles
dolphins have fins
rhinos have horns



In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be a list containing multiple values. Here we have a dictionary called "wardrobe" with items of clothing and their colors. Fill in the blanks to print a line for each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.


wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for cloth in wardrobe:
    for color in wardrobe[cloth]:
        print("{} {}".format(color, cloth))


        Here is your output:
red shirt
blue shirt
white shirt
blue jeans
black jeans



1.
Question 1
The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).

1 / 1 point


def email_list(domains):
	emails = []
	for domain, users in domains.items():
	  for user in users:
	    emails.append(user+'@'+domain)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))




2.
Question 2
The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 

1 / 1 point

def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group,users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
        # Now add the group to the the list of
          # groups for this user, creating the entry
          # in the dictionary if necessary
          user_groups[user] = user_groups.get(user,[]) + [group]


Correct
You're now creating dictionaries out of
other dictionaries!




3.
Question 3
The dict.update method updates one dictionary with the items coming from the other dictionary, so that existing entries are replaced and new entries are added. What is the content of the dictionary “wardrobe“ at the end of the following code?


wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)

1 / 1 point


{'shirt': ['red', 'blue', 'white'], 'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}



Correct
Correct! The dict.update method updates the dictionary (wardrobe) with the items coming from the other dictionary (new_items), adding new entries and replacing existing entries.




4.
Question 4
 What’s a major advantage of using dictionaries over lists?

1 / 1 point


It’s quicker and easier to find a specific element in a dictionary

Correct
Right on! Because of their unordered nature and use of key value pairs, searching a dictionary takes the same amount of time no matter how many elements it contains



5.
Question 5
The add_prices function returns the total price of all of the groceries in the  dictionary. Fill in the blanks to complete this function.

1 / 1 point

def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for items in basket.values():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += items
	# Limit the return value to 2 decimal places


Correct
Dictionaries are a helpful way to store
information, and access it easily when it's needed



