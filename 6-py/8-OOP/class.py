import random

# class can be understood as a self-created data type.
class Student:
# Designed by convention: 1. __init__ means to initialise the data of an object from the class. It can be used to defined the initialisation method.
# 2. The constructor call will store the data inside the object that has just been instantiated.
# 3. self is always a parameter to indicate that the current object is accesssed
    def __init__(self, name, house):
        if not name:
            raise ValueError("Empty Name")
        if house not in ('Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'):
            raise ValueError("Invalide House")
# self.xxx is an instance variable/attribute created inside of the particular instance, with different values in each object. Also, it can only be defined inside __init__.
# In this case, it will store the variable-name inside of the instance variable.
        self.name = name
        # notice no '_' added here, deliberate so that the setter is called even in initialisation stage.
        # it's possible to implement the same error checking inside the init method as well and add the '_'.
        self.house = house

    # The str method can be used to define a string to be passed to functions when an object from this class is called.
    def __str__(self):
        return f"{self.name} is from {self.house}"

# This syntax(decorator) decorates the 'house' function, the function will be called everytime the instance varaible is being accessed.
# Property is a variable that provides access to its value through a getter method. This allows control of how the value of the property is accessed and modified.
    @property
    # Getter function
    def house(self):
        # '_' added to differentiate the instance variable and the function. Note: instance variable is self._house, and the setter can be bypassed by directly calling that.
        return self._house

# Setter function, everytime the instance variable, '.house' is accessed (including inside of the init method), this setter function will be called.
# This prevents incorrect change to the value, implementing error checking in init will only be carried out during initialisation stage.
    @house.setter
    def house(self, house):
        if house not in ('Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'):
            raise ValueError("Invalide House")
        self._house = house

# Take for example, this is a class variable, which remains the same for all objects inside of the class, unlike a instance variable.
    houses = ('Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin')

    # This decorator defines a method of the whole class(class method), all the previous methods with access to self are instance methods.
    @classmethod
    # Pass in cls for class itself.
    def get(cls):
        name = input("Name: ")
        house = random.choice(cls.houses)
        # Same as the constructor call below, using Student(name, house) works too. The syntax is to create an object of the current cls
        return cls(name, house)

    @classmethod
    def sort(cls, name, house):
        print(name + ' is sorted to ' + house)

def main():

    condition = input('New student? (Y/N): ')
    if condition == 'N':
        try:
            name = input("Name: ")
            house = input("House: ")
            # This is a constructor call, which creates(instantiates) an object(instance) named 'student' of the specific class, the constructor will automatically call the init method.
            student = Student(name, house)
            print(student.name + ' is from ' + student.house)
        except ValueError:
            quit()
    else:
        try:
            # cls method can be called without instantiating a class object itself.
            student = Student.get()
            Student.sort(student.name, student.house)
        except ValueError:
            quit()

main()

# if an instance variable starts with '_' it's the convention used by programmers that this is a 'private' instance variable. This is also known as encapsulation in OOP.
