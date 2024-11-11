#include "graph.h"
#include "shortest_path.h"
#include "4 - heap/heap.hpp"

// add all out going edges into priority queue
void addOutGoingPaths(int v, const Graph& g, Heap<GraphEdge>& q, int* distance_arr){
  forward_list<GraphEdge> edges = g.edges_from(v);

  for(auto edge : edges){
    int dest_v = edge.dest();
    GraphEdge e = GraphEdge(dest_v, -1 * (distance_arr[dest_v]));
    q.insert((e));
  }
}

void relaxVertex(int v, const Graph& g, int* distance_arr, int* parent_arr){
  forward_list<GraphEdge> edges = g.edges_from(v);

  for(auto edge : edges){
    int dest_v = edge.dest();
    if(distance_arr[dest_v] == -1 || distance_arr[v] + edge.weight() < distance_arr[dest_v]){
      distance_arr[dest_v] = distance_arr[v] + edge.weight();
      parent_arr[dest_v] = v;
    }
  }
}

Path shortestPath(const Graph& g, int source, int dest) {
  vector<int> path;
  if(source == dest){
    return Path(0, path);
  }

  int graph_size = g.num_vertices();
  int distance_from_s[graph_size];
  std::fill(distance_from_s, distance_from_s + graph_size, -1);
  distance_from_s[source] = 0;

  Heap<GraphEdge> priortity_queue;
  int visited[graph_size];
  std::fill(visited, visited + graph_size, 0);
  visited[source] = 1;

  int parent[graph_size];
  for(int i = 0; i < graph_size; i++){
    parent[i] = i;
  }

  int curr_v = source;
  GraphEdge curr_edge;
  while(curr_v != dest){
    relaxVertex(curr_v, g, distance_from_s, parent);
    addOutGoingPaths(curr_v, g, priortity_queue, distance_from_s);

    while(visited[curr_v]){
      curr_edge = priortity_queue.extractMax();
      curr_v = curr_edge.dest();
    }

    visited[curr_v] = 1;
  }

  int start = dest;
  path.insert(path.begin(), start);
  while(start != source){
    start = parent[start];
    path.insert(path.begin(), start);
  }

  return Path(distance_from_s[dest], path);
}