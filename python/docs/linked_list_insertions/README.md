# README.md

## linked-list-insertions

() method with a non-existent value:
Given a linked list with head -> {1} -> {3} -> {2} -> NULL and the values 4 and 5
Expected output: head -> {1} -> {3} -> {2} -> NULL (no changes to the linked list)

## Whiteboard Process

![challenge 6 whiteboard](code_challenge_6_whiteboard.png)

## Approach & Efficiency

## Big O:

The time complexity of the insert before and insert after functions is O(n) because we have to traverse through the linked list until the given value is found, which could take up to n steps. The time complexity of the append function is O(1) because we can directly add a new node to the end of the linked list without having to traverse through it

## Solution

## Test cases

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

linked-list-insertions](linked_list/linked-list-insertions/README.md)
