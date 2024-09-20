#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include <initializer_list>
#include <string>

template<typename T> //template, use to define functions, classes that can work with any type
std::string element_to_string(T& element) {
  return std::to_string(element);
}

template<> //template specialisation, use to implement specific operations to a certain type
std::string element_to_string<std::string>(std::string& element) {
  std::string str;
  str.append("\"");
  str.append(element);
  str.append("\"");
  
  return str;
}

// Alternatively
/* 
template<typename T>
std::string element_to_string(T element) {
  return std::to_string(element);
}

// function overloading
std::string element_to_string(std::string element) {
  std::string str;
  str.append("\"");
  str.append(element);
  str.append("\"");
  
  return str;
}
*/

template <typename T> struct Node {
  T element;
  Node<T> *next;

  Node(T element) : element{element}, next{nullptr} {}
  Node(T element, Node<T> *next) : element{element}, next{next} {}

  bool isString(T) {}
};

template <typename T> class List {
private:
  size_t m_size;
  Node<T> *m_head;

  // Feel free to add helper functions here, if necessary

public:
  // Constructs an empty container
  List() : m_size{0}, m_head{nullptr} {}

  // Constructs the container with the contents of the initializer list
  List(std::initializer_list<T> init_list) : m_size{0}, m_head{nullptr} {
    auto it = init_list.end();
    while (--it != init_list.begin()) {
      push_head(*it);
    }
    push_head(*it);
  }

  // Rule of three:
  // If a class requires a user-defined destructor, a user-defined copy
  // constructor, or a user-defined copy assignment operator, it almost
  // certainly requires all three.

  // Destructor
  ~List() {
    // TODO: (Optional) Implement this method
  }

  // Copy constructor
  List(const List<T> &other) {
    // TODO: (Optional) Implement this method
  }

  // Copy assignment
  List<T> &operator=(const List<T> &other) {
    // TODO: (Optional) Implement this method
  }

  // Returns the contents of the head node
  const T& head() {
    if (m_size <= 0) {
      throw std::out_of_range("List is empty");
    }
    return m_head->element;
  }

  // Checks whether the container is empty
  bool empty() const { return m_size == 0; }

  // Returns the number of elements
  size_t size() const { return m_size; }

  // Inserts an element to the head
  void push_head(const T& element) {
    Node<T> *node = new Node<T>{element, m_head};
    m_head = node;
    m_size++;
  }

  // Removes the head element
  void pop_head() {
    if (m_size <= 0) {
      throw std::out_of_range("List is empty");
    }
    Node<T> *node = m_head;
    m_head = m_head->next;
    delete node;
    m_size--;
  }

  // Checks whether the container contains the specified element
  bool contains(const T& element) const {
    Node<T>* ptr = this -> m_head;
    while(ptr != nullptr){
      if(ptr -> element == element){
        return true;
      }
      ptr = ptr -> next;
    }  
    return false;
  }

  // Extracts the maximum element from the container
  T extract_max() {
    if(this -> m_head == nullptr){
      throw std::out_of_range("List is empty");
    }
    Node<T>* ptr = this -> m_head;
    T currMax = ptr -> element;
    while(ptr != nullptr){ // find currMax
      if(ptr -> element > currMax){
        currMax = ptr -> element;
      }
        ptr = ptr -> next;
    }
    
    if(this -> m_head -> element == currMax){
      this -> pop_head();
      return currMax;
    }
    
    Node<T>* prev = this -> m_head;
    ptr = prev -> next;
    while(ptr != nullptr){ // delete max
      if(ptr -> element == currMax){
        prev -> next = ptr -> next;
        delete ptr;
        this -> m_size--;
        return currMax;
      }
      prev = prev -> next;
      ptr = ptr -> next;
    }
    
    return currMax;
  }

  // Reverse the container
  void reverse() {
    Node<T>* ptr = this -> m_head;
    if(ptr == nullptr || ptr -> next == nullptr){
      return;
    }

    Node<T>* prev = ptr;
    Node<T>* next = ptr -> next;
    ptr -> next = nullptr;
    while(next != nullptr){
      ptr = next;
      next = next -> next;
      ptr -> next = prev;
      prev = ptr;
    }
    
    this -> m_head = ptr;
    return;
  }
  
  // Returns a std::string equivalent of the container
  std::string to_string() const {
    if(this -> m_head == nullptr){
      return "{}";
    }

    std::string res;
    res.append("{");

    Node<T>* ptr = this -> m_head;
    while(ptr != nullptr){
      res.append(element_to_string(ptr -> element));
      ptr = ptr -> next;
      if(ptr != nullptr){
        res.append(", ");
      }
    }

    res.append("}");
    return res;
  }

};

#endif
