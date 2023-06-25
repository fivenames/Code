// This will inherit from the super-class, its public methods and public instance variable(private to be accessed with public methods).
public class ListNode extends Node{
    private int listSize;

    public ListNode(int val, ListNode ptr, int size){
        super(val, ptr);
        this.listSize = size;
    }

    public static void main(String[] args){
        ListNode list = new ListNode(0, null, 4);
        Node ptr = list;

        for(int i = 1; i < list.listSize; i++){
            ptr.set_next(new ListNode(i, null, 0));
            ptr = ptr.get_next();
        }

        ptr = list;
        for(int i = 0; i < list.listSize; i++){
            System.out.println(ptr.val);
            ptr = ptr.get_next();
        }
    }
}

/*
Sub-class type can be referenced by the super-class type variable.
In polymorphism, the compiler will only look at the reference to look for the method, eg. ClassA var = ClassB(p), calling var.methods compiler will look at ClassA for the method.
If no such method is found, compiler will throw an error, if found the code will be compiled.
However, in runtime, the interpretor can understand that ClassB is the object type, the .methods will be called from ClassB instead.
Casting can solve the problem, use syntax like ( (ClassB)var ).methods to indicate that the method is from the sub-class.
*/

// In Java, there are keywords: abstract, final, to describe classes and interfaces(use implements keyword for inheriting classes) to describe methods when it comes to polymorphism.