class Wizard:
    def __init__(self, name, magic):
        self.name = name
        self.magic = magic

    # Operator overload, this defines the operator '+' to be an addition of the 'magic' instance attribute between two object
    def __add__(self, other):
        total_magicpower = self.magic + other.magic
        return total_magicpower

    def __sub__(self, other):
        diff_magicpower = self.magic - other.magic
        return diff_magicpower

# This will make Student class the sub-class of the Wizard Class, inheriting the attributes and functions of the super-class.
class Student(Wizard):
    def __init__(self, name, magic, house):
        # Calling the super-class's init method, passing in name and magic.
        super().__init__(name, magic)
        self.house = house

    def __add__(self, other):
        if self.house == other.house:
            total_magicpower = self.magic + other.magic + 10
        else:
            total_magicpower = self.magic + other.magic
        return total_magicpower

def main():
    enemy = Wizard('someguy', 40)

    student1 = Student('Harry', 15, 'Gryffindor')
    student2 = Student('Hermione', 20, 'Gryffindor')

    # __add__ method is override in the Student class, an OOP concept called Polymorphism.
    student_power = student1 + student2

    # Student class has also inherited __sub__ method from the Wizard class, allowing '-' operator to be used.
    diff_in_power = student1 - enemy
    if diff_in_power < 0:
        print('Harry lost to the enemy')
    else:
        print('Harry won')
        quit()

    diff_in_power = student2 - enemy
    if diff_in_power < 0:
        print('Hermione also lost to the enemy')
    else:
        print('Hermione won')
        quit()

    if student_power - enemy.magic < 0:
        print('They fought together but still lost')
    else:
        print('They fought together and beat the enemy')

main()

