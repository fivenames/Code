// Assignment 4.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include "heap.hpp"
#include "customer.h"
#include "queue_simulator.h"
#include <iostream>
#include <vector>
#include <algorithm>
#define EXPECT_EQ(x,y) {std::cout << (((x)==(y)) ? "Test Passed" : "Test Failed" )<< std::endl;};
#define EXPECT_TRUE(x) EXPECT_EQ(x,true)
#define EXPECT_FALSE(x) EXPECT_EQ(x,false)


void heapTest0();
void heapTest1();
void heapTest2();
void heapTest3();
void heapTest4();

void simpleQueueTest0();
void simpleQueueTest1();
void simpleQueueTest2();
void simpleQueueTest3();
void simpleQueueTest4();
void simpleQueueTest5();


const vector<int> sample_array{ 3, -27, -26, -25, 8, -22, 16, -16, -3, -15, -13, -8, 25, -4, 29, 30 };

int calculate_average_wait_time(vector<Customer> customers){
    int total_wait_time = 0;
    for(auto customer : customers){
        total_wait_time += customer.service_time();
    }
    return total_wait_time / customers.size();
}

int main()
{   
    const vector<Customer> SAMPLE{
        Customer(2, 10), Customer(3, 8), Customer(4, 2),
        Customer(5, 3), Customer(8, 1), Customer(12, 2),
    };
    const vector<Customer> SAMPLE0{
        Customer(2, 10), Customer(4, 2), Customer(8, 1),
    };
        const vector<Customer> SAMPLE1{
        Customer(3, 8), Customer(5, 3), Customer(12, 2),
    };

    QueueSimulator sim;
    QueueSimulator sim0;
    QueueSimulator sim1;

    sim.set_num_servers(2);
    
    auto result = sim.simulateQueue(SAMPLE);
    std::cout << "average wait time for single FIFO queue: " << calculate_average_wait_time(result) << "\n";

    sim.set_priority_order(true);
    result = sim.simulateQueue(SAMPLE);
    std::cout << "average wait time for single priority queue: " << calculate_average_wait_time(result) << "\n";

    auto result0 = sim0.simulateQueue(SAMPLE0);
    auto result1 = sim1.simulateQueue(SAMPLE1);
    int sample_average = (calculate_average_wait_time(result0) + calculate_average_wait_time(result1)) / 2;
    std::cout << "average wait time for multiple FIFO queue: " << sample_average << "\n";

    sim0.set_priority_order(true);
    sim1.set_priority_order(true);
    result0 = sim0.simulateQueue(SAMPLE0);
    result1 = sim1.simulateQueue(SAMPLE1);
    sample_average = (calculate_average_wait_time(result0) + calculate_average_wait_time(result1)) / 2;
    std::cout << "average wait time for multiple FIFO queue: " << sample_average << "\n";
}



void heapTest0() {
    std::cout << "Check that default construct builds sane heap. Heap Test 0" << std::endl;
    Heap<int> heap;
    EXPECT_EQ(heap.size(), 0);
    EXPECT_TRUE(heap.empty());
}

void heapTest1() {
    std::cout << "Check that calling insert with a single value works as expected. Heap Test 1" << std::endl;
    Heap<int> heap;
    heap.insert(-1);
    EXPECT_EQ(heap.size(), 1);
    EXPECT_FALSE(heap.empty());
    EXPECT_EQ(heap.peekMax(), -1);
}

void heapTest2() {
    std::cout << "Heap Test 2" << std::endl;
    Heap<int> heap;
    heap.insert(5);
    EXPECT_EQ(heap.size(), 1);
    heap.insert(4);
    EXPECT_EQ(heap.size(), 2);
    heap.insert(3);
    EXPECT_EQ(heap.size(), 3);
    heap.insert(2);
    EXPECT_EQ(heap.size(), 4);
    heap.insert(1);
    EXPECT_EQ(heap.size(), 5);

}


template <typename T>
vector<T> extract_all(Heap<T>& heap) {
    vector<T> elements;
    while (!heap.empty()) {
        elements.push_back(heap.extractMax());
    }

    return elements;
}


void heapTest3(){
    std::cout << "Check that extract_max works correctly for various insertions. Heap Test 3" << std::endl;
    Heap<int> heap;
    for (const auto v : sample_array) {
        heap.insert(v);
    }
    vector<int> elements = extract_all(heap);
    vector<int> expected = sample_array;
    std::sort(expected.begin(), expected.end(), greater<int>());
    EXPECT_EQ(elements, expected);
}

void heapTest4() {
    std::cout <<  "Check that peek_max works correctly for various insertions. Heap Test 4" << std::endl;

    Heap<int> heap;
    for (const auto v : sample_array) {
        heap.insert(v);
    }

    int last_max = heap.peekMax();
    EXPECT_EQ(last_max, heap.extractMax());
    while (!heap.empty()) {
        int max = heap.peekMax();
        EXPECT_EQ(max, heap.extractMax());
        EXPECT_TRUE(last_max>= max);
        last_max = max;
    }
}




void simpleQueueTest0() {
    std::cout << "Check that a single customer gets served." << std::endl;
    vector<Customer> customers = { Customer(0, 1) };
    QueueSimulator sim;
    auto result = sim.simulateQueue(customers);
    EXPECT_EQ(result.size(), 1);
    EXPECT_EQ(result[0].service_time(), 0);
}


void simpleQueueTest1() {
    std::cout << "simpleQueueTest1" << std::endl;
    vector<Customer> customers = { Customer(0, 2), Customer(1, 5), Customer(3, 2) };
    QueueSimulator sim;
    auto result = sim.simulateQueue(customers);
    EXPECT_EQ(result.size(), 3);
    EXPECT_EQ(result[0].service_time(), 0);
    EXPECT_EQ(result[1].service_time(), 2);
    EXPECT_EQ(result[2].service_time(), 7);
}

const vector<Customer> SAMPLE_CUSTOMERS{
    Customer(1, 5), Customer(2, 7), Customer(3, 2),
    Customer(4, 3), Customer(8, 1),
};

void simpleQueueTest2() {
    std::cout << "Longer Queue Test" << std::endl;
    vector<Customer> customers = SAMPLE_CUSTOMERS;
    QueueSimulator sim;
    auto result = sim.simulateQueue(customers);
    EXPECT_EQ(result.size(), 5);
    EXPECT_EQ(result[0].service_time(), 1);
    EXPECT_EQ(result[1].service_time(), 6);
    EXPECT_EQ(result[2].service_time(), 13);
    EXPECT_EQ(result[3].service_time(), 15);
    EXPECT_EQ(result[4].service_time(), 18);
}

void simpleQueueTest3() {
    std::cout << "Priority Queue Test" << std::endl;
    vector<Customer> customers = SAMPLE_CUSTOMERS;
    QueueSimulator sim;
    sim.set_priority_order(true);
    auto result = sim.simulateQueue(customers);
    EXPECT_EQ(result.size(), 5);
    EXPECT_EQ(result[0].arrival_time(), 1);
    EXPECT_EQ(result[0].service_time(), 1);
    EXPECT_EQ(result[1].arrival_time(), 3);
    EXPECT_EQ(result[1].service_time(), 6);
    EXPECT_EQ(result[2].arrival_time(), 8);
    EXPECT_EQ(result[2].service_time(), 8);
    EXPECT_EQ(result[3].arrival_time(), 4);
    EXPECT_EQ(result[3].service_time(), 9);
    EXPECT_EQ(result[4].arrival_time(), 2);
    EXPECT_EQ(result[4].service_time(), 12);
}


void simpleQueueTest4() {
    std::cout << "multiple_servers Test" << std::endl;
    vector<Customer> customers = SAMPLE_CUSTOMERS;
    QueueSimulator sim;
    sim.set_num_servers(2);
    auto result = sim.simulateQueue(customers);
    EXPECT_EQ(result.size(), 5);
    EXPECT_EQ(result[0].service_time(), 1);
    EXPECT_EQ(result[1].service_time(), 2);
    EXPECT_EQ(result[2].service_time(), 6);
    EXPECT_EQ(result[3].service_time(), 8);
    EXPECT_EQ(result[4].service_time(), 9);
}

void simpleQueueTest5() {
    std::cout << "multiple_servers_priority_queue Test" << std::endl;
    vector<Customer> customers{
        Customer(1, 5), Customer(2, 7), Customer(3, 5),
        Customer(4, 2), Customer(5, 1), Customer(8, 1),
    };
    QueueSimulator sim;
    sim.set_num_servers(2);
    sim.set_priority_order(true);
    auto result = sim.simulateQueue(customers);
    EXPECT_EQ(result.size(), 6);
    EXPECT_EQ(result[0].arrival_time(), 1);
    EXPECT_EQ(result[0].service_time(), 1);
    EXPECT_EQ(result[1].arrival_time(), 2);
    EXPECT_EQ(result[1].service_time(), 2);
    EXPECT_EQ(result[2].arrival_time(), 5);
    EXPECT_EQ(result[2].service_time(), 6);
    EXPECT_EQ(result[3].arrival_time(), 4);
    EXPECT_EQ(result[3].service_time(), 7);
    EXPECT_EQ(result[4].arrival_time(), 8);
    EXPECT_EQ(result[4].service_time(), 9);
    EXPECT_EQ(result[5].arrival_time(), 3);
    EXPECT_EQ(result[5].service_time(), 9);
}
