Attributes are characteristics associated with a type. Methods are: Functions associated with a type. (Remember, a method defines what you do with an object.)



You want to find more information about the integer (int) class. What's the best way to do this? Use the command help(int)
(Using the help command can be useful for finding quick documentation about the methods in a class.)


Want to give this a go? Fill in the blanks in the code to make it print a poem.


class Flower:
  color = 'unknown'

rose = Flower()
rose.color = "red"

violet = Flower()
violet.color = "blue"

this_pun_is_for_you = Flower()


Here is your output:
Roses are red,
violets are blue,
<submission.Flower object at 0x7fecc4258940>



1.
Question 1
Let’s test your knowledge of using dot notation to access methods and attributes in an object. Let’s say we have a class called Birds. Birds has two attributes: color and number. Birds also has a method called count() that counts the number of birds (adds a value to number). Which of the following lines of code will correctly print the number of birds? Keep in mind, the number of birds is 0 until they are counted!

1 / 1 point



bluejay.count()

print(bluejay.number)




Correct
Nice job! We must first call the count() method, which will populate the number attribute, allowing us to print number and receive a correct response.



2.
Question 2
Creating new instances of class objects can be a great way to keep track of values using attributes associated with the object. The values of these attributes can be easily changed at the object level.  The following code illustrates a famous quote by George Bernard Shaw, using objects to represent people. Fill in the blanks to make the code satisfy the behavior described in the quote. 

1 / 1 point

# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()


Correct
Awesome! You’re getting used to using instances of class
objects and assigning them attributes!



3.
Question 3
The City class has the following attributes: name, country (where the city is located), elevation (measured in meters), and population (approximate, according to recent statistics). Fill in the blanks of the max_elevation_city function to return the name of the city and its country (separated by a comma), when comparing the 3 defined instances for a specified minimal population. For example, calling the function for a minimum population of 1 million: max_elevation_city(1000000) should return "Sofia, Bulgaria". 

1 / 1 point

# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()


Correct
Way to go! You're getting comfortable with the idea of class
objects and what they can do!



4.
Question 4
What makes an object different from a class?

1 / 1 point


An object is a specific instance of a class


Correct
Awesome! Objects are an encapsulation of variables and functions into a single entity.



5.
Question 5
We have two pieces of furniture: a brown wood table and a red leather couch. Fill in the blanks following the creation of each Furniture class instance, so that the describe_furniture function can format a sentence that describes these pieces as follows: "This piece of furniture is made of {color} {material}"

1 / 1 point

class Furniture:
	color = ""
	material = ""

table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"


Correct
Right on! You're working well with classes, objects, and
instances!

