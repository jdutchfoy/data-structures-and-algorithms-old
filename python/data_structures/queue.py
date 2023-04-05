from lib2to3.pytree import Node
from data_structures.invalid_operation_error import InvalidOperationError


# Create a Queue class that has a front property. It creates an empty Queue when instantiated.
class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    # Add a new item to the back of the queue
    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.back = node
        else:
            self.back._next = node
            self.back = node

    # Remove the next item from the front of the queue
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        node = self.front
        self.front = self.front._next
        if self.front is None:
            self.back = None
        return node.value

    # Return the value of the item at the front of the queue without removing it
    def peek(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.front.value

    # Check whether the queue is empty
    def is_empty(self):
        return self.front is None

# Create a class for animals


class Animal:
    def __init__(self, name):
        self.name = name

# Create a class for dogs that inherits from the Animal class


class Dog(Animal):
    pass

# Create a class for cats that inherits from the Animal class


class Cat(Animal):
    pass

# Create a class for an animal shelter


class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []

    # Add an animal to the shelter
    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.dogs.append(animal)
        elif isinstance(animal, Cat):
            self.cats.append(animal)

    # Remove the next available animal from the shelter
    def dequeue(self, preference=None):
        if preference == 'dog':
            if self.dogs:
                return self.dogs.pop(0)
        elif preference == 'cat':
            if self.cats:
                return self.cats.pop(0)
        else:
            if self.dogs:
                return self.dogs.pop(0)
            elif self.cats:
                return self.cats.pop(0)
        return Animal("")


#  create new AnimalShelter object, and  add some animals to it with the enqueue. We Then remove animals from the shelter with the dequeue method.
# shelter = AnimalShelter()
dog1 = Dog('Max')
dog2 = Dog('Buddy')
cat1 = Cat('Luna

# code assistance by dom james
