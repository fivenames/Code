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

  // Returns a pointer to the root
  Node<T> *root();

  // Checks whether the tree is empty
  bool empty() const;

  // Returns the number of elements
  size_t size() const;

  // Returns the height of the tree
  int height() const;

  void _balanceNode(Node<T> *node);
  void _updateNodeHeight(Node<T> *node);
  void _rotateLeft(Node<T> *node);
  void _rotateRight(Node<T> *node);

  // Inserts the specified element
  Node<T>* _insert(T element, Node<T> *curr);
  void insert(T element);

  // Checks whether the container contains the specified element
  bool contains(T element) const;

  // Returns the maximum element
  T max() const;

  // Returns the minimum element
  T min() const;

  // Returns the successor of the specified element
  T successor(T element);

  // Convert each element in the tree to string in pre-order.
  string pre_order();

  // Convert each element in the tree to string in order.
  string in_order();

  // Convert each element in the tree to string in post-order.
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
  // TODO: Implement this method
}

// Destructor
template <typename T> Tree<T>::~Tree() {
  // TODO: Implement this method
}

// Returns a pointer to the root
template <typename T> Node<T> *Tree<T>::root() {
  // TODO: Implement this method
  return nullptr;
}

// Checks whether the tree is empty
template <typename T> bool Tree<T>::empty() const {
  // TODO: Implement this method
  return true;
}

// Returns the number of elements
template <typename T> size_t Tree<T>::size() const {
  // TODO: Implement this method
  return 0;
}

// Returns the height of the tree
template <typename T> int Tree<T>::height() const {
  // TODO: Implement this method
  return 0;
}

template <typename T>
void Tree<T>::_balanceNode(Node<T> *node){
  return;
}

template <typename T>
void Tree<T>::_updateNodeHeight(Node<T> *node){
  int leftHeight = -1;
  int rightHeight = -1;
  if(node -> left != nullptr){
    leftHeight = node -> left ->height;
  }
  if(node -> right != nullptr){
    rightHeight = node -> right -> height;
  }
  node -> height = std::max(leftHeight, rightHeight) + 1;
  return;
}

template <typename T>
void Tree<T>::_rotateLeft(Node<T> *node){
  return;
}

template <typename T>
void Tree<T>::_rotateRight(Node<T> *node){
  return;
}

// Inserts an element
template <typename T>
Node<T>* Tree<T>::_insert(T element, Node<T> *curr) {
  if(element < curr -> element && curr -> left == nullptr){
    return new Node(element, 0);
  } else if(element > curr -> element && curr -> right == nullptr){
    return new Node(element, 0);
  }

  if(element < curr -> element){
    curr -> left = Tree::insert(element, curr -> left);
  } else {
    curr -> right = Tree::insert(element, curr -> right);
  }

  Tree::_updateNodeHeight(curr);
  Tree::_balanceNode(curr);
  return curr;
}

template <typename T>
void Tree<T>::insert(T element){
  Tree::_insert(element, this -> m_root);
  return;
}

// Checks whether the container contains the specified element
template <typename T> bool Tree<T>::contains(T element) const {
  // TODO: Implement this method
  return false;
}

// Returns the maximum element
template <typename T> T Tree<T>::max() const {
  // TODO: Implement this method
  throw std::runtime_error("not implemented");
}

// Returns the minimum element
template <typename T> T Tree<T>::min() const {
  // TODO: Implement this method
  throw std::runtime_error("not implemented");
}

// Returns the successor of the specified element
template <typename T> T Tree<T>::successor(T element) {
  // TODO: Implement this method
  throw std::runtime_error("not implemented");
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
string Tree<T>::in_order() {
  // TODO: Implement this method
  return "";
}

template <typename T>
string Tree<T>::post_order() {
  // TODO: Implement this method
  return "";
}

#endif
