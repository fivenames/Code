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
  Tree();
  ~Tree();

  Node<T> *root();                  // Returns a pointer to the root
  bool empty() const;               // Checks whether the tree is empty
  size_t size() const;              // Returns the number of elements
  int height() const;               // Returns the height of the tree
  void insert(T element);           // Inserts the specified element
  bool contains(T element) const;   // Checks whether the container contains the specified element
  T max() const;                    // Returns the maximum element
  T min() const;                    // Returns the minimum element
  T successor(T element);           // Returns the successor of the specified element
  string pre_order();               // Convert each element in the tree to string in pre-order.
  string in_order();                // Convert each element in the tree to string in order.
  string post_order();              // Convert each element in the tree to string in post-order.

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

  void recursiveDestructor(Node<T> *node); // ~Tree() helper
  Node<T>* _insert(Node<T> *node, T element); // insert helper
  string _in_order(Node<T> *node);         // in-order helper
  string _post_order(Node<T> *node);       // post-order helper
  int _updateHeight(Node<T> *node);        // updates height of current node
  Node<T>* rotateRight(Node<T>* node);
  Node<T>* rotateLeft(Node<T>* node);
};

// Constructor
template <typename T> Tree<T>::Tree() {
    m_root = nullptr;
    m_size = 0;
}

// Destructor
template <typename T> void Tree<T>::recursiveDestructor(Node<T> *node) {
    if (node == nullptr) return;
    
    if (node->left != nullptr) {
        recursiveDestructor(node->left);
        node->left = nullptr;
    }

    if (node->right != nullptr) {
        recursiveDestructor(node->right);
        node->right = nullptr;
    }

    delete node;
}

template <typename T> Tree<T>::~Tree() {
    if (m_root == nullptr) return; 
    recursiveDestructor(m_root);
}

// Returns a pointer to the root
template <typename T> Node<T> *Tree<T>::root() {
    return m_root; // if tree is empty, then m_root = nullptr
}

// Checks whether the tree is empty
template <typename T> bool Tree<T>::empty() const {
  return m_size == 0;
}

// Returns the number of elements
template <typename T> size_t Tree<T>::size() const {
  return m_size;
}

// Returns the height of the tree
template <typename T> int Tree<T>::height() const {
  if (m_size == 0) return -1;
  return m_root->height;
}

// Inserts an element
template <typename T> Node<T>* Tree<T>::_insert(Node<T> *node, T element) {
    if (element > node->element) {
        if (node->right) node->right = _insert(node->right, element);
        else node->right = new Node<T>(element, 0);
    } else {
        if (node->left) node->left = _insert(node->left, element);
        else node->left = new Node<T>(element, 0);
    }

    _updateHeight(node);
    // check balance
    int right_height = _updateHeight(node->right);
    int left_height = _updateHeight(node->left);
    if (right_height - left_height > 1) {
        // right heavy
        if (element <= node->right->element) // RL
            node->right = rotateRight(node->right);
        node = rotateLeft(node);
    } else if (left_height - right_height > 1) {
        // left heavy
        if (element > node->left->element) // LR
            node->left = rotateLeft(node->left);
        node = rotateRight(node);
    }
    
    _updateHeight(node); 
    return node;
}

template <typename T> Node<T>* Tree<T>::rotateLeft(Node<T>* node) {
    Node<T> *x = node;
    Node<T> *y = node->right;
    Node<T> *T1 = y->left;

    x->right = T1;
    y->left = x;
    _updateHeight(x);
    _updateHeight(y);
    return y;
}

template <typename T> Node<T>* Tree<T>::rotateRight(Node<T>* node) {
    Node<T> *y = node;
    Node<T> *x = node->left;
    Node<T> *T1 = x->right;

    y->left = T1;
    x->right = y;
    _updateHeight(y);
    _updateHeight(x);
    return x;
}

template <typename T> int Tree<T>::_updateHeight(Node<T> *node) {
    if (node == nullptr) return -1;
    int left_height = (node->left ? node->left->height : -1);
    int right_height = (node->right ? node->right->height : -1);
    return node->height = ((left_height > right_height) ? left_height : right_height) + 1;
}

template <typename T> void Tree<T>::insert(T element) {
    if (contains(element)) return;
    m_size++;
    if (m_size == 1) {
        m_root = new Node<T>(element, 0);
        return;
    }

    m_root = _insert(m_root, element);
}

// Checks whether the container contains the specified element
template <typename T> bool Tree<T>::contains(T element) const {
  Node<T> *curr = m_root;
  while (curr && curr->element != element) {
      if (element > curr->element) curr = curr->right;
      else curr = curr->left;
  }
  return curr != nullptr;
}

// Returns the maximum element
template <typename T> T Tree<T>::max() const {
    if (m_root == nullptr) throw std::runtime_error("Tree is empty.");
    Node<T> *curr = m_root;
    while (curr->right) curr = curr->right;
    return curr->element;
}

// Returns the minimum element
template <typename T> T Tree<T>::min() const {
    if (m_root == nullptr) throw std::runtime_error("Tree is empty.");
    Node<T> *curr = m_root;
    while (curr->left) curr = curr->left;
    return curr->element;
}

// Returns the successor of the specified element
template <typename T> T Tree<T>::successor(T element) {
    if (m_size == 0) throw std::runtime_error("Tree is empty.");
    Node<T> *curr = m_root;
    Node<T> *greater_parent = nullptr;
   
    // searching for element 
    while (curr && curr->element != element) {
        if (element > curr->element) curr = curr->right;
        else {
            greater_parent = curr;
            curr = curr->left;
        }
    }
    
    // if element has right sub-tree, find the right most child
    if (curr && curr->right) {
        curr = curr->right;
        while (curr->left) curr = curr->left;
        return curr->element;
    }
    
    // if element has no right sub-tree, find the last ancestor who is greater
    if (greater_parent) return greater_parent->element;

    // no greater ancester && no subtree == largest value in BST
    throw std::runtime_error("Element is the largest value in the BST.");
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
string Tree<T>::_in_order(Node<T> *node) {
  return (node->left == nullptr ? "" : _in_order(node->left))
    + (node->left == nullptr ? "" : " ") + my_to_string(node->element)
    + (node->right == nullptr ? "" : " " + _in_order(node->right)); 
}

template <typename T>
string Tree<T>::in_order() {
    if (m_root == nullptr) return "";
    return _in_order(m_root);
}

template <typename T>
string Tree<T>::_post_order(Node<T> *node) {
  return (node->left == nullptr ? "" : _post_order(node->left) + " ")
    + (node->right == nullptr ? "" : _post_order(node->right) + " ")
    + my_to_string(node->element);
}

template <typename T>
string Tree<T>::post_order() {
    if (m_root == nullptr) return "";
    return _post_order(m_root);
}

#endif
