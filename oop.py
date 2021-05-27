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




#Object-Oriented Programming Defined
In object-oriented programming, concepts are modeled as classes and objects. An idea is defined using a class, and an instance of this class is called an object. Almost everything in Python is an object, including strings, lists, dictionaries, and numbers. When we create a list in Python, we’re creating an object which is an instance of the list class, which represents the concept of a list. Classes also have attributes and methods associated with them. Attributes are the characteristics of the class, while methods are functions that are part of the class.



#Classes and Objects in Detail
We can use the type() function to figure out what class a variable or value belongs to. For example, type(" ") tells us that this is a string class. The only attribute in this case is the string value, but there are a bunch of methods associated with the class. We've seen the upper() method, which returns the string in all uppercase, as well as isnumeric() which returns a boolean telling us whether or not the string is a number. You can use the dir() function to print all the attributes and methods of an object. Each string is an instance of the string class, having the same methods of the parent class. Since the content of the string is different, the methods will return different values. You can also use the help() function on an object, which will return the documentation for the corresponding class. This will show all the methods for the class, along with parameters the methods receive, types of return values, and a description of the methods.




#Defining Classes (Optional)
We can create and define our classes in Python similar to how we define functions. We start with the class keyword, followed by the name of our class and a colon. Python style guidelines recommend class names to start with a capital letter. After the class definition line is the class body, indented to the right. Inside the class body, we can define attributes for the class.

Let's take our Apple class example:


>>> class Apple:
...     color = ""
...     flavor = ""
... 
We can create a new instance of our new class by assigning it to a variable. This is done by calling the class name as if it were a function. We can set the attributes of our class instance by accessing them using dot notation. Dot notation can be used to set or retrieve object attributes, as well as call methods associated with the class.


>>> jonagold = Apple()
>>> jonagold.color = "red"
>>> jonagold.flavor = "sweet"


We created an Apple instance called jonagold, and set the color and flavor attributes for this Apple object. We can create another instance of an Apple and set different attributes to differentiate between two different varieties of apples.



>>> golden = Apple()
>>> golden.color = "Yellow"
>>> golden.flavor = "Soft"


We now have another Apple object called golden that also has color and flavor attributes. But these attributes have different values.

