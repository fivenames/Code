public abstract class Graph{
    private int numNodes;
    private int numEdges;

    public Graph(){
        this.numNodes = 0;
        this.numEdges = 0;
    }

    public int getNumNodes(){
        return this.numNodes;
    }
    public int getNumEdges(){
        return this.numEdges;
    }

    public void addnumNode(){
        this.numNodes++;
    }
    public void addnumEdges(int num){
        this.numEdges = this.numEdges + num;
    }

    public abstract void addNode();
    public abstract void addEdge(int i, int j);
}