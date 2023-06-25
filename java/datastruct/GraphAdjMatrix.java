public class GraphAdjMatrix extends Graph{
    // Adjacency Matrix is a way of implementing Graphs, the 2-dimensional array will contain the number of edges between 2 given node: i and j.
    // This approach is suitable for dense graphs where the number of edges is close to the maximum possible number of edges.
    // It provides constant-time lookup for edge existence, efficient in determining whether there is an edge between two vertices. 
    // However, it is inefficient in adding/removing vertices due to the need to resizing the matrix.

    // Alternative way is to implement Adjacency List, which uses a Map to map each node to a List of its neighbours.

    private int[][] adjMatrix;

    public GraphAdjMatrix(){
        super();
        this.adjMatrix = new int[0][0];
    }

    public void addNode(){
        this.addnumNode();

        int graphsize = this.getNumNodes();
        if(graphsize >= this.adjMatrix.length){
            int[][] newMatrix = new int[graphsize * 2][graphsize * 2];
            for(int i = 0; i < adjMatrix.length; i++){
                for(int j = 0; j < adjMatrix.length; j++){
                    newMatrix[i][j] = this.adjMatrix[i][j]; 
                }
            }
            this.adjMatrix = newMatrix;
        }
        
        for(int i = 0; i < graphsize; i++){
            this.adjMatrix[graphsize - 1][i] = 0;
            this.adjMatrix[i][graphsize - 1] = 0;
        }
    }
    public void addEdge(int i, int j){
        this.addnumEdges(j);
        this.adjMatrix[i][j] = 1;
    }

    public static void main(String[] args) {
        Graph testgraph = new GraphAdjMatrix();
        testgraph.addNode();
        testgraph.addNode();
        testgraph.addEdge(0, 1);
        System.out.println(testgraph.getNumEdges());
        System.out.println(testgraph.getNumNodes());
    }
}