#pragma once
#ifndef TREE_H
#define TREE_H

#include <algorithm>
#include <cassert>
#include <functional>
#include <string>

using std::string;

template <typename T>
std::string my_to_string(const T& t) {
  return std::to_string(t);
}

template <>
std::string my_to_string(const std::string& t) {
  return "\"" + t + "\"";
}

template <typename T> struct Node {
  T element;
  int height;
  Node<T> *left;
  Node<T> *right;

  Node(T element)
      : element{element}, height{0}, left{nullptr}, right{nullptr} {}
  Node(T element, int height)
      : element{element}, height{height}, left{nullptr}, right{nullptr} {}
};

template <typename T> class Tree {
private:
  size_t m_size;
  Node<T> *m_root;

public:
  // Constructor
  Tree();

  // Rule of three:
  // If a class requires a user-defined destructor, a user-defined copy
  // constructor, or a user-defined copy assignment operator, it almost
  // certainly requires all three.

  // Destructor
  ~Tree();
  void _deleteTree(Node<T> *curr);

  // Returns a pointer to the root
  Node<T> *root();

  // Checks whether the tree is empty
  bool empty() const;

  // Returns the number of elements
  size_t size() const;

  // Returns the height of the tree
  int height() const;

  Node<T>* _balanceNode(Node<T> *node);
  void _updateNodeHeight(Node<T> *node);
  Node<T>* _rotateLeft(Node<T> *node);
  Node<T>* _rotateRight(Node<T> *node);
  int _getNodeHeight(Node<T> *node);

  // Inserts the specified element
  Node<T>* _insert(T element, Node<T> *curr);
  void insert(T element);

  // Checks whether the container contains the specified element
  bool contains(T element) const;

  // Returns the maximum element
  T max() const;

  // Returns the minimum element
  T min() const;

  T _min(Node<T> *node);
  // Returns the successor of the specified element
  T successor(T element);

  // Convert each element in the tree to string in pre-order.
  string pre_order();

  // Convert each element in the tree to string in order.
  string _in_order(Node<T> *node);
  string in_order();

  // Convert each element in the tree to string in post-order.
  string _post_order(Node<T> *node);
  string post_order();

  // Returns a string equivalent of the tree
  string to_string(bool with_height = true) const {
    return m_to_string(with_height, m_root, 0);
  }

private:
  string m_to_string(bool with_height, Node<T> *node, int ident) const {
    string res;
    if (node == nullptr) {
      return res;
    }
    if (node->right != nullptr) {
      res += m_to_string(with_height, node->right, ident + 2);
    }
    for (int i = 0; i < ident; i++) {
      res += " ";
    }
    res += my_to_string(node->element);
    if (with_height) {
      res += "(h=" + my_to_string(node->height) + ")";
    }
    res += "\n";
    if (node->left != nullptr) {
      res += m_to_string(with_height, node->left, ident + 2);
    }
    return res;
  }

  // Feel free to declare helper functions here, if necessary
  };

// Constructor
template <typename T> Tree<T>::Tree() {
    m_root = nullptr;
    m_size = 0;
}

template <typename T> void Tree<T>::_deleteTree(Node<T> *curr){
  if(curr == nullptr){
    return;
  }
  _deleteTree(curr -> left);
  _deleteTree(curr -> right);
  delete curr;
}

// Destructor
template <typename T> Tree<T>::~Tree() {
  _deleteTree(this -> m_root);
  this -> m_size = 0;
  this -> m_root = nullptr;
}

// Returns a pointer to the root
template <typename T> Node<T> *Tree<T>::root() {
  return this -> m_root;
}

// Checks whether the tree is empty
template <typename T> bool Tree<T>::empty() const {
  return (this -> m_size == 0);
}

// Returns the number of elements
template <typename T> size_t Tree<T>::size() const {
  return this -> m_size;
}

// Returns the height of the tree
template <typename T> int Tree<T>::height() const {
  if(this -> m_root == nullptr){
    return -1;
  }
  return this -> m_root -> height;
}

template <typename T>
Node<T>* Tree<T>::_rotateLeft(Node<T> *node){
  Node<T> *w = node -> right;
  node -> right = w -> left;
  w -> left = node;

  _updateNodeHeight(node);
  _updateNodeHeight(w);
  return w; // Return new root of the sub-tree
}

template <typename T>
Node<T>* Tree<T>::_rotateRight(Node<T> *node){
  Node<T> *w = node -> left;
  node -> left = w -> right;
  w -> right = node;

  _updateNodeHeight(node);
  _updateNodeHeight(w);
  return w;
}

template <typename T>
int Tree<T>::_getNodeHeight(Node<T> *node){
  if(node == nullptr){
    return -1;
  }
  return node -> height;
}

template <typename T>
void Tree<T>::_updateNodeHeight(Node<T> *node){
  int leftHeight = _getNodeHeight(node -> left);
  int rightHeight = _getNodeHeight(node -> right);
  node -> height = std::max(leftHeight, rightHeight) + 1;
  return;
}

template <typename T>
Node<T>* Tree<T>::_balanceNode(Node<T> *node){ // Balance the sub-tree and return the new root
  int leftHeight = _getNodeHeight(node -> left);
  int rightHeight = _getNodeHeight(node -> right);
  int balanceFactor = leftHeight - rightHeight;

  if (balanceFactor > 1) {  // Left-heavy
    Node<T>* child = node->left;
    if (_getNodeHeight(child->right) > _getNodeHeight(child->left)) {
      node->left = _rotateLeft(child); // Left-Right case
    }
    return _rotateRight(node);
  } else if (balanceFactor < -1) {  // Right-heavy
    Node<T>* child = node->right;
    if (_getNodeHeight(child->left) > _getNodeHeight(child->right)) {
      node->right = _rotateRight(child); // Right-Left case
    }
    return _rotateLeft(node);
  }

  return node; // Already balanced
}

template <typename T>
Node<T>* Tree<T>::_insert(T element, Node<T> *curr) { // Backtrack each stack frame and balance the current sub-tree
  if(curr == nullptr){
    return new Node<T>(element, 0); // Create the node after reach the leaves
  }

  // Recrursively go down the tree
  if(element < curr -> element){
    curr -> left = _insert(element, curr -> left); // Receive the inserted and balanced sub-tree from the recursion stack
  } else {
    curr -> right = _insert(element, curr -> right);
  }
  _updateNodeHeight(curr); // Update each of the node height

  return _balanceNode(curr); // Balance the sub-tree and return the new root
}

// Inserts an element
template <typename T>
void Tree<T>::insert(T element){
  this -> m_root = _insert(element, this -> m_root);
  this -> m_size++;
  return;
}

// Checks whether the container contains the specified element
template <typename T> 
bool Tree<T>::contains(T element) const {
  Node<T> *ptr = this -> m_root;
  while(ptr != nullptr){
    if(element < ptr -> element){
      ptr = ptr -> left;
    } else if (element > ptr -> element) {
      ptr = ptr -> right;
    } else {
      return true;
    }
  }

  return false;
}

// Returns the maximum element
template <typename T> 
T Tree<T>::max() const {
  Node<T> *ptr = this -> m_root;
  if(ptr == nullptr){
    throw std::out_of_range("empty tree");
  }

  while(ptr -> right != nullptr){
    ptr = ptr -> right;
  }

  return ptr -> element;
}

// Returns the minimum element
template <typename T> T Tree<T>::min() const {
  Node<T> *ptr = this -> m_root;
  if(ptr == nullptr){
    throw std::out_of_range("empty tree");
  }

  while(ptr -> left != nullptr){
    ptr = ptr -> left;
  }

  return ptr -> element;
}

template <typename T> 
T Tree<T>::_min(Node<T> *node){
  Node<T> *ptr = node;
  while(ptr -> left != nullptr){
    ptr = ptr -> left;
  }

  return ptr -> element;
}

// Returns the successor of the specified element
template <typename T> 
T Tree<T>::successor(T element) {
  Node<T> *ptr = this -> m_root;
  if(ptr == nullptr){
    throw std::out_of_range("empty tree");
  }

  T successor = ptr -> element; 
  while(ptr != nullptr){
    if(element > ptr -> element){
      ptr = ptr -> right;
    } else if(element < ptr -> element){
      successor = ptr -> element; // Whenever move left, record the current sucessor
      ptr = ptr -> left;
    } else if(element == ptr -> element){ // Found the element
      if(ptr -> right != nullptr){ // Find minimum of the right sub-tree if there exists
        return _min(ptr -> right);
      }
      break;
    }
  }

  if(successor <= element){
    throw std::out_of_range("no successor");
  }
  return successor;
}

template <typename T>
string _pre_order(Node<T> *node) {
  return my_to_string(node->element)
    + (node->left == nullptr ? "" : " " + _pre_order(node->left))
    + (node->right == nullptr ? "" : " " + _pre_order(node->right));
}

template <typename T>
string Tree<T>::pre_order() {
  if (m_root == nullptr) {
    return "";
  }
  return _pre_order(m_root);
}

template <typename T>
string Tree<T>::_in_order(Node<T> *node){
  return (node -> left == nullptr ? "" : _in_order(node -> left) + " ")
    + my_to_string(node -> element)
    + (node -> right == nullptr ? "" : " " + _in_order(node -> right));
}

template <typename T>
string Tree<T>::in_order() {
  if (m_root == nullptr) {
    return "";
  }
  return _in_order(m_root);
}

template <typename T>
string Tree<T>::_post_order(Node<T> *node){
  return (node -> left == nullptr ? "" : _post_order(node -> left) + " ")
    + (node -> right == nullptr ? "" : _post_order(node -> right) + " ") 
    + my_to_string(node -> element);
}

template <typename T>
string Tree<T>::post_order() {
  if (m_root == nullptr) {
    return "";
  }
  return _post_order(m_root);
}

#endif
