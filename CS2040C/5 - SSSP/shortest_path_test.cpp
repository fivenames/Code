#include <utility>
#include "graph.h"
#include "shortest_path.h"

using namespace std;

int main(){
  Graph g(25);
  g.addEdge(0, 1, 82);
  g.addEdge(0, 2, 72);
  g.addEdge(1, 3, 145);
  g.addEdge(1, 5, 119);
  g.addEdge(1, 6, 152);
  g.addEdge(2, 1, 38);
  g.addEdge(2, 4, 59);
  g.addEdge(3, 1, 30);
  g.addEdge(3, 7, 168);
  g.addEdge(4, 8, 174);
  g.addEdge(5, 6, 38);
  g.addEdge(6, 3, 186);
  g.addEdge(6, 4, 139);
  g.addEdge(6, 5, 99);
  g.addEdge(6, 7, 107);
  g.addEdge(7, 4, 82);
  g.addEdge(7, 8, 133);
  g.addEdge(7, 9, 166);
  g.addEdge(8, 2, 112);
  g.addEdge(8, 3, 160);
  g.addEdge(8, 6, 50);
  g.addEdge(8, 7, 180);
  g.addEdge(9, 0, 98);
  g.addEdge(9, 3, 52);
  g.addEdge(9, 5, 70);

  Path p = shortestPath(g, 6, 1);
  std::cout << "The shortest distance from " << 6 << " to " << 1 << " is " << p.total_distance() << " and the path is: { ";
  for (int i = 0; i < p.path().size(); i++) {
    std::cout << p.path()[i];
    if (i!=p.path().size()-1) std::cout << " , ";
  }
  std::cout << " }" << endl;
}

