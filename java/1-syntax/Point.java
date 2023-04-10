public class Point // extends (classname) : this will inherit from the super-class, its public methods and public instance variable(private to be accessed with public methods).
{
    // Instance variable, private indicates that the value of the variable can only be changed with methods within this class. (Encapsulation)
    // There are keywords like protected as well and also the default(package-private).
    private int x;
    private int y;
// Define a setter method to allow modification of instance variable, define a getter to allow reading of instance variable.

    // Constructor, named the same as the class. Default constructor, no parameter is passed.
    public Point (){
        this.x = 0;
        this.y = 0;
    }
    // Standard constructor, this is a concept of functional overloading: more than one method of the same name are declared with differing parameters. (Python does not support)
    // Overriding in polymophism is sub-class having the same method name and same parameters as the super-class but different implementation, different from overloading.
    public Point (int init_x, int init_y){
        x = init_x;
        y = init_y;
    }

    // Instance methods, getter method. 'public' allows calling of this method outside of the class. This getter method will allow other classes to access the private instance variable.
    public int get_x() { return x; }
    public int get_y() { return y; }
    // Passing in one parameter, an object of Point class.
    public double displacement(Point other){
        // 'this' keyword access the current object(the object calling the method), equivalent to 'self' keyword in Python OOP.
        int d_x = this.x - other.get_x();
        int d_y = this.y - other.get_y();
        return Math.sqrt(d_x * d_x + d_y * d_y);
    }
    // Setter, can implement error checks like in Python.
    public void set_x(int new_x){ this.x = new_x; }
    public void set_y(int new_y){ this.y = new_y; }

// Static methods can be called directly on the class itself, without creating an object instance of the class, it belongs to a class, rather than to any particular object instance.
// Equivalent to @classmethod in Python OOP.
    // 'main' is a special static method which acts as the execution point of the code.
    public static void main(String[] args){
        // When using 'new', data is created in the heap similar to malloc() in C, ie. the data will not be cleared when function calls return.
        // the variable p1/p2 are references(pointers) that points to the object instantiated (same as Python). However, no pointer operations can be carried out in Java.
        Point p1 = new Point(1, 2);
        Point p2 = new Point(3, 4);
/*
System class has a static variable(equivalent to class variables in Python OOP) of the PrintStream class.

'out' is an static variable of the System class, implemented by calling the PrintStream class constructor. It is implemented in the System class because
it represents the standard output stream, a system-level concept. This demostrates a concept of abstraction, hiding complex implementations while presenting simple interface to the user.

println() is an instance method of PrintStream class. Hence, this is essentially accessing an instance of PrintStream class and calling a method on it.
*/
        System.out.println(p1.displacement(p2));
    }
}

/*
Java compiler rules: 

All super-class will extend from Obejct class, when defining constructor, the compiler will always put super() before any initialisation.
For eg. the sub-class constructor will call the object() constructor first before calling super() constructor and finally initialisation the sub-class variables.

Sub-class type can be referenced by the super-class type variable.
In polymorphism, the compiler will only look at the reference to look for the method, eg. ClassA var = ClassB(p), calling var.methods compiler will look at ClassA for the method.
If no such method is found, compiler will throw an error, if found the code will be compiled.
However, in runtime, the interpretor can understand that ClassB is the object type, the .methods will be called from ClassB instead.
Casting can solve the problem, use syntax like ( (ClassB)var ).methods to indicate that the method is from the sub-class.
*/

// In Java, there are keywords: abstract, final, to describe classes and interfaces to describe methods when it comes to polymorphism.