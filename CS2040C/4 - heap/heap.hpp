#pragma once
#include <math.h>

#include <iostream>
using namespace std;

#ifndef HEAPHPP
#define HEAPHPP

#define DEFAULTHEAPSIZE 1023

template <class T>
class Heap {
 protected:
  T* _heap;
  unsigned int _size;


 public:
  Heap() {
    _heap = new T[DEFAULTHEAPSIZE]; 
    _size = 0;
  }

  unsigned int size() const {
    return this -> _size;
  }

  bool empty() const {
    return (this -> size() == 0);
  }
  
  void insert(const T&);
  T extractMax();
  T peekMax() const;
  void printHeapArray() const;
  void printTree() const;
  void changeKey(const T& from, const T& to);
  void deleteItem(const T&);
  void _bubbleUp(const unsigned int index);
  void _bubbleDown(const unsigned int index);

  ~Heap() { delete[] _heap; };
};

template <class T>
void Heap<T>::_bubbleUp(const unsigned int index){
  if(index == 0){ // if reached root, return
    return;
  }

  unsigned int parent_index = (index - 1) / 2; 
  if(this -> _heap[parent_index] < this -> _heap[index]){ // if bigger than parent, swap and recursively bubble up
    std::swap(this -> _heap[parent_index], this -> _heap[index]);
    this -> _bubbleUp(parent_index);
  } 

  return;
}

template <class T>
void Heap<T>::_bubbleDown(const unsigned int index) {
  unsigned int left_child = 2 * index + 1;
  unsigned int right_child = 2 * index + 2;
  unsigned int largest = index; // store the largest node

  if (left_child < this -> _size && this -> _heap[left_child] > this -> _heap[largest]) { // if left child exists and is bigger, update largest
    largest = left_child;
  }
  if (right_child < this -> _size && this -> _heap[right_child] > this -> _heap[largest]) { // same for right
    largest = right_child;
  }

  if (largest != index) { // if current node is not the largest, swap and recursively bubble down
    std::swap(this -> _heap[index], this -> _heap[largest]);
    this->_bubbleDown(largest);
  }
  return;
}

template <class T>
void Heap<T>::insert(const T& item) {
  this -> _heap[this -> size()] = item;
  this -> _size++; 
  this -> _bubbleUp(this -> size() - 1);
  
  return;
}

template <class T>
T Heap<T>::extractMax() {
  if(this -> empty()){
    throw std::out_of_range("empty heap");
  }

  this -> deleteItem(this -> _heap[0]);
  return this -> _heap[this -> size()];
}

template <class T>
T Heap<T>::peekMax() const {
  if(this -> empty()){
    throw std::out_of_range("empty heap");
  }

  return this ->  _heap[0];
};

template <class T>
void Heap<T>::printHeapArray() const {
  for (int i = 0; i < size(); i++) {
    cout << _heap[i] << " ";
  }
  cout << endl;
}

template <class T>
void Heap<T>::changeKey(const T& from, const T& to) {
  if(from == to){
    return;
  }
  if(this -> empty()){
    throw std::out_of_range("empty heap");
  }

  int location = -1;
  for(int i = 0; i < this -> size(); i++){ // find the index of item to delete
    if(this -> _heap[i] == from){
      location = i;
      break;
    }
  }
  if(location == -1){
    throw std::out_of_range("no such item in heap");
  }

  this -> _heap[location] = to;
  if(from > to){ // decrease key
    this -> _bubbleDown(location);
  } else { // increase key
    this -> _bubbleUp(location);
  }

  return;
}

template <class T>
void Heap<T>::deleteItem(const T& x) {
  if(this -> empty()){
    throw std::out_of_range("empty heap");
  }

  int location = -1;
  for(int i = 0; i < this -> size(); i++){ // find the index of item to delete
    if(this -> _heap[i] == x){
      location = i;
      break;
    }
  }
  if(location == -1){
    throw std::out_of_range("no such item in heap");
  }

  std::swap(this -> _heap[location], this -> _heap[this -> size() - 1]);
  this -> _size--;
  
  T item = this -> _heap[location];
  this -> _bubbleDown(location);
  if(this -> _heap[location] == item){ // if the node did not bubble down, bubble up instead
    this -> _bubbleUp(location);
  }

  return;
}

template <class T>
void Heap<T>::printTree() const {
  int parity = 0;
  if (size() == 0) return;
  int space = pow(2, 1 + (int)log2f(size())), i;
  int nLevel = (int)log2f(size()) + 1;
  int index = 0, endIndex;
  int tempIndex;

  for (int l = 0; l < nLevel; l++) {
    index = 1;
    parity = 0;
    for (i = 0; i < l; i++) index *= 2;
    endIndex = index * 2 - 1;
    index--;
    tempIndex = index;
    while (index < size() && index < endIndex) {
      for (i = 0; i < space - 1; i++) cout << " ";
      if (index == 0)
        cout << "|";
      else if (parity)
        cout << "\\";
      else
        cout << "/";
      parity = !parity;
      for (i = 0; i < space; i++) cout << " ";
      index++;
    }
    cout << endl;
    index = tempIndex;
    while (index < size() && index < endIndex) {
      for (i = 0; i < (space - 1 - ((int)log10(_heap[index]))); i++)
        cout << " ";
      cout << _heap[index];
      for (i = 0; i < space; i++) cout << " ";
      index++;
    }

    cout << endl;
    space /= 2;
  }
}

#endif
