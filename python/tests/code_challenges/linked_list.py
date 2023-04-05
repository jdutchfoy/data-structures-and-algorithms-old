class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def insert_before(self, value, new_value):
        if not self.head:
            return
        new_node = Node(new_value)
        if self.head.data == value:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        while current_node.next and current_node.next.data != value:
            current_node = current_node.next
        if current_node.next and current_node.next.data == value:
            new_node.next = current_node.next
            current_node.next = new_node

    def insert_after(self, value, new_value):
        if not self.head:
            return
        new_node = Node(new_value)
        current_node = self.head
        while current_node and current_node.data != value:
            current_node = current_node.next
        if current_node and current_node.data == value:
            new_node.next = current_node.next
            current_node.next = new_node

    def __str__(self):
        if not self.head:
            return "Empty linked list"
        current_node = self.head
        result = ""
        while current_node:
            result += f"{str(current_node.data)} -> "
            current_node = current_node.next
        result += "NULL"
        return result

# Test cases
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(3)
linked_list.append(2)
linked_list.append(5)
assert str(linked_list) == "1 -> 3 -> 2 -> 5 -> NULL"

empty_list = LinkedList()
empty_list.append(5)
assert str(empty_list) == "5 -> NULL"

linked_list.insert_before(3, 5)
assert str(linked_list) == "1 -> 5 -> 3 -> 2 -> 5 -> NULL"

linked_list.insert_before(4, 5)
assert str(linked_list) == "1 -> 5 -> 3 -> 2 -> 5 -> NULL"

linked_list.insert_after(3, 5)
assert str(linked_list) == "1 -> 5 -> 3 -> 5 -> 2 -> 5 -> NULL"

linked_list.insert_after(4, 5)
assert str(linked_list) == "1 -> 5 -> 3 -> 5 -> 2 -> 5 -> NULL"
