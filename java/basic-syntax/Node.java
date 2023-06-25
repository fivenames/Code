public class Node{
    protected int val;
    private Node next;
    
    public Node(){
        this.val = 0;
        this.next = null;
    }
    public Node(int set, Node ptr){
        this.val = set;
        this.next = ptr;
    }

    public Node get_next(){
        return this.next;
    }

    public void set_next(Node ptr){
        this.next = ptr;
    }
}
/*
Java compiler rules: 
All super-class will extend from Obejct class, when defining constructor, the compiler will always put super() before any initialisation.
For eg. the sub-class constructor will call the object() constructor first before calling super() constructor and finally initialisation the sub-class variables.
*/
