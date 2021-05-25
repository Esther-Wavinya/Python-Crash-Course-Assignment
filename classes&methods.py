What Is a Method?


Calling methods on objects executes functions that operate on attributes of a specific instance of the class. This means that calling a method on a list, for example, only modifies that instance of a list, and not all lists globally. We can define methods within a class by creating functions inside the class definition. These instance methods can take a parameter called self which represents the instance the method is being executed on. This will allow you to access attributes of the instance using dot notation, like self.name, which will access the name attribute of that specific instance of the class object. When you have variables that contain different values for different instances, these are called instance variables.





Create a Dog class with dog_years based on the Piglet class shown before (one human year is about 7 dog years).


class Dog:
  years = 0
  def dog_years(self):
    return self.years * 7
fido=Dog()
fido.years=3
print(fido.dog_years())


Here is your output:
21

Awesome! You've now learned about writing your own methods!




 
 In this code, there's a Person class that has an attribute name, which gets set when constructing the object. Fill in the blanks so that
  1) when an instance of the class is created, the attribute gets set correctly, and 
  2) when the greeting() method is called, the greeting states the assigned name.


class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name) 

# Create a new instance with a name of your choice
some_person = Person("xyz") 
# Call the greeting method


Here is your output:
hi, my name is xyz

Right on! You have successfully learned to assign attributes
to instances of class objects!


#Special Methods
Instead of creating classes with empty or default values, we can set these values when we create the instance. This ensures that we don't miss an important value and avoids a lot of unnecessary lines of code. To do this, we use a special method called a constructor. Below is an example of an Apple class with a constructor method defined.


>>> class Apple:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor


When you call the name of a class, the constructor of that class is called. This constructor method is always named __init__. You might remember that special methods start and end with two underscore characters. In our example above, the constructor method takes the self variable, which represents the instance, as well as color and flavor parameters. These parameters are then used by the constructor method to set the values for the current instance. So we can now create a new instance of the Apple class and set the color and flavor values all in go:


>>> jonagold = Apple("red", "sweet")
>>> print(jonagold.color)
Red


In addition to the __init__ constructor special method, there is also the __str__ special method. This method allows us to define how an instance of an object will be printed when it’s passed to the print() function. If an object doesn’t have this special method defined, it will wind up using the default representation, which will print the position of the object in memory. Not super useful. Here is our Apple class, with the __str__ method added:


>>> class Apple:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor
...     def __str__(self):
...         return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
...


Now, when we pass an Apple object to the print function, we get a nice formatted string:



>>> jonagold = Apple("red", "sweet")
>>> print(jonagold)
This apple is red and its flavor is sweet
This apple is red and its flavor is sweet

It's good practice to think about how your class might be used and to define a __str__ method when creating objects that you may want to print later.



Remember our Person class from the last video? Let’s add a docstring to the greeting method. How about, “Outputs a message with the name of the person”.


class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    '''Outputs a message with the name of the person'''
    print("Hello! My name is {name}.".format(name=self.name)) 

help(Person)


Here is your output:
Help on class Person in module submission:

class Person(builtins.object)
 |  Methods defined here:
 |  
 |  __init__(self, name)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  greeting(self)
 |      Outputs a message with the name of the person
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)


Excellent! You’ve mastered the art of providing info using
docstrings!



#Documenting with Strings

The Python help function can be super helpful for easily pulling up documentation for classes and methods. We can call the help function on one of our classes, which will return some basic info about the methods defined in our class:


>>> class Apple:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor
...     def __str__(self):
...         return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
... 
>>> help(Apple)
Help on class Apple in module __main__:


We can add documentation to our own classes, methods, and functions using docstrings. A docstring is a short text explanation of what something does. You can add a docstring to a method, function, or class by first defining it, then adding a description inside triple quotes. Let's take the example of this function:


>>> def to_seconds(hours, minutes, seconds):
...     """Returns the amount of seconds in the given hours, minutes and seconds."""
...     return hours*3600+minutes*60+seconds
... 


We have our function called to_seconds on the first line, followed by the docstring which is indented to the right and wrapped in triple quotes. Last up is the function body. Now, when we call the help function on our to_seconds function, we get a handy description of what the function does:


>>> help(to_seconds)
Help on function to_seconds in module __main__:

to_seconds(hours, minutes, seconds)
    Returns the amount of seconds in the given hours, minutes and seconds.


Docstrings are super useful for documenting our custom classes, methods, and functions, but also when working with new libraries or functions. You'll be extremely grateful for docstrings when you have to work with code that someone else wrote!








#Classes and Methods Cheat Sheet (Optional)
#Classes and Methods Cheat Sheet
In the past few videos, we’ve seen how to define classes and methods in Python. Here, you’ll find a run-down of everything we’ve covered, so you can refer to it whenever you need a refresher.

Defining classes and methods

class ClassName:
    def method_name(self, other_parameters):
        body_of_method


Classes and Instances
Classes define the behavior of all instances of a specific class.
Each variable of a specific class is an instance or object.
Objects can have attributes, which store information about the object.
You can make objects do work by calling their methods.
The first parameter of the methods (self) represents the current instance.
Methods are just like functions, but they can only be used through a class.


Special methods
Special methods start and end with __.
Special methods have specific names, like __init__ for the constructor or __str__ for the conversion to string.
Documenting classes, methods and functions
You can add documentation to classes, methods, and functions by using docstrings right after the definition. Like this:


class ClassName:
    """Documentation for the class."""
    def method_name(self, other_parameters):
        """Documentation for the method."""
        body_of_method
        
def function_name(parameters):
    """Documentation for the function."""
    body_of_function



