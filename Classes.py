# Basic Structure for a class
class MyClass(object): # name of class usually starts with a capital and the parents object for our class is object. 
    # functions contained within classes are called that class' methods. 
    def __init__(self #, argument1, argument2):
        # add   self.argument = argument   for any additional arguments that are passed when u call the class. these also need to be included in the init method.
    random_variable = "stuff"
    def random_method(self):
        print (pass)

myfirstclass = MyClass(argument1, argument2) # creates a new object which is an instance of that class.
myfirstclass.random_method() #calls that class' method.
print myfirstclass.random_variable #calls that class' member variable

class MyChildClass(MyClass): # creates a class that is a child to MyClass and has access to that class' data and methods.
    #only needs an init() method if new info is needed that arent used in parent class.


