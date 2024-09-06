#include "LinkedList.h"
#include <stdexcept>

// Returns the value at head
int List::head() {
    if(this -> empty()){
        throw std::out_of_range("List is empty");
    }
	return this -> m_head -> element;
}
// Checks whether the container is empty
bool List::empty() const {
	return (this -> m_size == 0 && this -> m_head == nullptr);
}
// Returns the number of elements
size_t List::size() const {
	return this -> m_size;
}
// Inserts an element to the head
void List::push_head(int element) {
	Node* newNode = new Node(element, this -> m_head);
	this -> m_head = newNode;
	this -> m_size++;
}
// Removes the head element
int List::pop_head() {
	if(this -> empty()){
		throw std::out_of_range("List is empty");
	}
	int res = this -> m_head -> element;
	if(this -> m_size == 1){
		delete this -> m_head;
	}
	else{
		Node* temp = this -> m_head -> next;
		delete this -> m_head;
		this -> m_head = temp;
	}
	this -> m_size--;
	return res;
}
// Checks whether the container contains the specified element
bool List::contains(int element) const {
	Node* curr = this -> m_head;
	while(curr != nullptr){
		if(curr -> element == element){
			return true;
		}
		curr = curr -> next;
	}
	return false;
}
// Returns a std::string equivalent of the container
std::string List::to_string() const {
	if(this -> empty()){
		return "{}";
	}
	std::string res;
	res.append("{");
	Node* curr = this -> m_head;
	while(curr != nullptr){
		res.append(std::to_string(curr -> element));
		if(curr -> next != nullptr){
			res.append(", ");
		}
		curr = curr -> next;
	}
	res.append("}");
	return res;
}