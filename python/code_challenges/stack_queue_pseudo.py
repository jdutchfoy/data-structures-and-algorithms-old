from queue import Queue
import pytest
from stack_queue_pseudo import PseudoQueue, Stack
# from stack_and_queue.stack_and_queue import Stack

# from data_structures.stack import Stack

# Define two custom exception classes to handle empty stack and empty queue errors


class EmptyStackException(Exception):
    pass


class EmptyQueueException(Exception):
    pass

# Define a Node class with a constructor to create a node
# It stores a value and a reference to the next node in the linked list


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Define a Stack class with methods to push, pop, and peek elements, and check if it's empty


class Stack:
    def __init__(self):
        self.top = None

    # + element to the top of the stack
    def push(self, value):
        # Create a new node with the specified value
        node = Node(value)
        # Set the new node's next reference to the current top node
        node.next = self.top
        # Update the top node to the new node
        self.top = node

 # Remove/return the top element from the stack
    def pop(self):
        # If the stack is empty, raise an EmptyStackException
        if self.top == None:
            raise EmptyStackException("Pop from empty stack is not allowed")
        # Store the current top node in a temporary variable
        temp = self.top
        # Update the top node to the next node in the stack
        self.top = temp.next
        # Set the next reference of the removed node to None
        temp.next = None
        # Return the value of the removed node
        return temp.value

    # Return the value of the top element in the stack without removing it
    def peek(self):
        # If the stack is empty, raise an EmptyStackException
        if self.top == None:
            raise EmptyStackException("Peek from empty stack is not allowed")
        else:
            return self.top.value
 # Check if the stack is empty and return True or False

    def is_empty(self):
        return True if self.top == None else False

# Return a string representation of the stack
    def __str__(self):
        # Start at the top
        current = self.top
        # Initialize an empty string to store the values of each node ??
        items = ''
        # Traverse the stack and add the value of each node to the string stackoverflow
        while current:
            items += str(current.value) + '\n'
            current = current.next
        # Return the string representation of the stack
        return items
# Define a PseudoQueue class that emulates a queue using two stacks


class PseudoQueue:
    def __init__(self):
        # Create two stacks to store the elements
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    # + an element to the end of the queue
    def enqueue(self, value):  # type: ignore
        self.stack_1.push(value)

    # Remove/return the first element from the queue

    def enqueue(self, value):
        # If the second stack is empty, move all elements from the first stack to the second stack in reverse order
        while not self.stack_1.is_empty():
            self.stack_2.push(self.stack_1.pop())

        self.stack_1.push(Node(value))

        while not self.stack_2.is_empty():
            self.stack_1.push(self.stack_2.pop())

    def dequeue(self):
        if self.stack_1.is_empty():
            return None

        # Remove and return the top element from the second stack
        return self.stack_2.pop().value

    if __name__ == '__main__':

        # Create a new PseudoQueue instance
        pq = Queue()

    # Add some elements to the queue
    # Create an empty list 'pq'
    pq = []
    
    # Add some elements to the queue
    if pq:
         pq.append(1)
         pq.append(2)
    
    

