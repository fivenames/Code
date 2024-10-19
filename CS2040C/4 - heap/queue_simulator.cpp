#include "queue_simulator.h"

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



vector<Customer> QueueSimulator::simulateQueue(
    const vector<Customer>& customers) {
      // handle priority queue
      if(this -> _priority_order){ 

        int curr_time = customers[0].arrival_time();
        MinHeap priority_queue = MinHeap();
        vector<Customer> res;
        
        for(auto customer : customers){

          if(curr_time >= customer.arrival_time()){ // add all arrived customers into the queue
            Customer curr = Customer(customer.arrival_time(), customer.processing_time());
            priority_queue.insert(curr);
            continue;
          }

          while(curr_time < customer.arrival_time() && priority_queue.get_size() > 0){ // serve the customer until next customer arrive
            Customer serving = priority_queue.extractMin();
            serving.set_service_time(curr_time);
            
            curr_time += serving.processing_time();
            res.push_back(serving);
          }

          if(priority_queue.get_size() == 0 && curr_time < customer.arrival_time()){ // if there is no one in the shop, wait till the next customer
            curr_time = customer.arrival_time();
          }
          Customer curr = Customer(customer.arrival_time(), customer.processing_time()); // add current customer to queue
          priority_queue.insert(curr);
        }

        while(priority_queue.get_size() != 0){
          Customer serving = priority_queue.extractMin();
          serving.set_service_time(curr_time);

          curr_time += serving.processing_time();
          res.push_back(serving);
        }

        return res;
      }

      // handle normal queue
      vector<Customer> queue; 
      int curr_time = customers[0].arrival_time();
      for (auto customer : customers){
        if(curr_time < customer.arrival_time()){
          curr_time = customer.arrival_time();
        }
        Customer curr = Customer(customer.arrival_time(), customer.processing_time());

        curr.set_service_time(curr_time);
        queue.push_back(curr);

        curr_time += customer.processing_time();
      }

      return queue;
}