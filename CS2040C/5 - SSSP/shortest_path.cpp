#include "graph.h"
#include "shortest_path.h"
#include "4 - heap/heap.hpp"

// add all out going edges into priority queue
void addOutGoingPaths(int v, const Graph& g, Heap<GraphEdge>& q){
  forward_list<GraphEdge> edges = g.edges_from(v);

  for(auto edge : edges){
    GraphEdge e = GraphEdge(edge.dest(), (-1 * edge.weight()));
    q.insert((e));
  }
}

void relaxVertex(int v, const Graph& g, int& distance_arr, int& parent_arr){
  forward_list<GraphEdge> edges = g.edges_from(v);

  for(auto edge : edges){
    int curr_v = edge.dest();
    if(distance_arr[...])
  }
}

Path shortestPath(const Graph& g, int source, int dest) {
  vector<int> path;
  int distance = 0;
  if(source == dest){
    return Path(distance, path);
  }

  int graph_size = g.num_vertices();
  int distance_from_s[graph_size] = {-1};
  int parents[graph_size];
  for(int i = 0; i < graph_size; i++){
    parents[i] = i;
  }

  Heap<GraphEdge> priortity_queue;
  addOutGoingPaths(source, g, priortity_queue);
  
  GraphEdge curr_edge = priortity_queue.extractMax();
  distance += -1 * curr_edge.weight();
  path.push_back(curr_edge.dest());
  while(curr_edge.dest() != dest){
    ...
  }

  return Path(distance, path);
}