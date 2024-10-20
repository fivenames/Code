#include "queue_simulator.h"
#include <iostream>

class MinHeap{
  private:
    Customer *_heap;
    unsigned int _size;
  
  public:
    MinHeap() {
      _heap = new Customer[1023]; 
      _size = 0;
    }

    unsigned int get_size(){
      return _size;
    }

    void insert(const Customer& item){
      this -> _heap[this -> get_size()] = item;
      this -> _size++; 
      this -> _bubbleUp(this -> get_size() - 1);
      
      return;
    }

    Customer peekMin(){
      return this -> _heap[0];
    }

    Customer extractMin(){
      std::swap(this -> _heap[0], this -> _heap[this -> get_size() - 1]);
      this -> _size--;

      this -> _bubbleDown(0);
      return this -> _heap[this -> get_size()];
    }

    void _bubbleUp(const unsigned int index){
      if(index == 0){
        return;
      }

      unsigned int parent_index = (index - 1) / 2; 
      if(this -> _heap[parent_index].processing_time() > this -> _heap[index].processing_time()){
        std::swap(this -> _heap[parent_index], this -> _heap[index]);
        this -> _bubbleUp(parent_index);
      } 

      return;
    }

    void _bubbleDown(const unsigned int index) {
      unsigned int left_child = 2 * index + 1;
      unsigned int right_child = 2 * index + 2;
      unsigned int smallest = index;

      if (left_child < this -> _size && this -> _heap[left_child].processing_time() < this -> _heap[smallest].processing_time()) {
        smallest = left_child;
      }
      if (right_child < this -> _size && this -> _heap[right_child].processing_time() < this -> _heap[smallest].processing_time()) {
        smallest = right_child;
      }

      if (smallest != index) {
        std::swap(this -> _heap[index], this -> _heap[smallest]);
        this->_bubbleDown(smallest);
      }
      return;
    }
};

struct Server {
  int available_time = 0;

  bool is_available(int curr_time){
    return available_time <= curr_time;
  }
};


vector<Customer> QueueSimulator::simulateQueue(const vector<Customer>& customers) {
  // get number of servers
  int num_server = this -> _num_servers;
  Server servers[num_server];

  // handle priority queue
  if(this -> _priority_order){ 

    int curr_time = customers[0].arrival_time();
    MinHeap priority_queue = MinHeap();
    vector<Customer> res;
    
    for(const auto customer : customers){
      Customer curr = Customer(customer.arrival_time(), customer.processing_time());
      if(curr_time >= customer.arrival_time()){ // add all arrived customers into the queue
        priority_queue.insert(curr);
        continue;
      }

      while(curr_time < customer.arrival_time() && priority_queue.get_size() > 0){ // serve the customer until next customer arrive
        Customer serving = priority_queue.peekMin(); // get the highest priority customer at current time
        
        Server *next_available_server = &servers[0];
        for(auto &server : servers){ // check for available server
          if(server.is_available(curr_time)){ // if there is,
            serving.set_service_time(curr_time);  // serve
            res.push_back(serving);
            priority_queue.extractMin(); // only remove from the queue after serving the customer
            server.available_time = curr_time + serving.processing_time(); // update the server's available time
            break;
          }

          if(server.available_time < next_available_server -> available_time){
            next_available_server = &server;
          }
        }

        if(serving.service_time() == -1){ // if no available server, wait till a server is available
          curr_time = next_available_server -> available_time; // There might be customers arriving, cannot serve without adding all of them into the queue
        }
      }

      if(priority_queue.get_size() == 0 && curr_time < customer.arrival_time()){ // if there is no one in the shop, wait till the next customer
        curr_time = customer.arrival_time();
      }

      priority_queue.insert(curr); // add current customer to queue
    }

    while(priority_queue.get_size() != 0){ // serve the customer in the queue
      Customer serving = priority_queue.peekMin();
        
      Server *next_available_server = &servers[0];
      for(auto &server : servers){
        if(server.is_available(curr_time)){
          serving.set_service_time(curr_time);
          res.push_back(serving);
          priority_queue.extractMin();
          
          server.available_time = curr_time + serving.processing_time();
          break;
        }

        if(server.available_time < next_available_server -> available_time){
          next_available_server = &server;
        }
      }

      if(serving.service_time() == -1){ // if no available server, wait until the next available time and
        curr_time = next_available_server -> available_time; // update time,
        next_available_server -> available_time += serving.processing_time();
        serving.set_service_time(curr_time); // serve the customer
        res.push_back(serving);
        priority_queue.extractMin();
      } // All customers have arrived.
    }

    return res;
  }

  // handle normal queue
  vector<Customer> queue; 
  int curr_time = customers[0].arrival_time();
  for(const auto customer : customers){
    Customer curr = Customer(customer.arrival_time(), customer.processing_time());
    if(curr_time < curr.arrival_time()){ // if customer has not arrive, wait
      curr_time = curr.arrival_time();
    }

    Server *next_available_server = &servers[0];
    for(auto &server : servers){ // check if there is an available server
      if(server.is_available(curr_time)){
        curr.set_service_time(curr_time);
        queue.push_back(curr);
        
        server.available_time = curr_time + curr.processing_time();
        break;
      } 

      if(server.available_time < next_available_server -> available_time){
        next_available_server = &server;
      }
    }

    if(curr.service_time() == -1){ // if no available server, wait until the next available time
      curr_time = next_available_server -> available_time;
      next_available_server -> available_time += curr.processing_time();
      curr.set_service_time(curr_time);
      queue.push_back(curr);
    }
  }

  return queue;
}