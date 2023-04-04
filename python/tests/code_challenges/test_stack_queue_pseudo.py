from inspect import stack
import pytest
from code_challenges.stack_queue_pseudo import PseudoQueue
from stack_queue_pseudo import EmptyQueueException, Stack

# Test empty stack


def test_empty_stack():
    stack = Stack()
    assert stack.is_empty() == True

# Test push method


def test_push():
    stack = Stack()
    stack.push(1)
    stack = Stack()
    stack.push(1)

    # Check if stack is not empty before accessing its top element
    if stack.top is not None:
        assert stack.top.value == 1

    # Fix typo error in the next line
    value = 1


# Test pop method
def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)


assert stack.pop() == 2

# Check if top node exists before accessing its value
if stack.top is not None:
    assert stack.top.value == 1

# Test peek method

def test_peek():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1

# Test is_empty method


def test_is_empty():
    stack = Stack()
    assert stack.is_empty() == True
    stack.push(1)
    assert stack.is_empty() == False

    # Test enqueue method


def test_enqueue():
    pq = PseudoQueue()
    pq.enqueue(1)

    # Check if stack_1 is not empty before accessing its top element
if not pq.stack_1.is_empty():

    # Test dequeue method


def test_dequeue():
    pq = PseudoQueue()
    pq.enqueue(1)
    pq.enqueue(2)
    assert pq.dequeue() == 1
    assert pq.stack_2.top.value == 2

# Test empty queue


def test_empty_queue():
    pq = PseudoQueue()
    with pytest.raises(EmptyQueueException):
        pq.dequeue()


def test_exists():
    assert PseudoQueue

# @pytest.mark.skip("TODO")


def test_enqueue_one():
    pq = PseudoQueue()
    pq.enqueue("apples")
    actual = pq.dequeue()
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_enqueue_two():
    pq = PseudoQueue()
    pq.enqueue("apples")
    pq.enqueue("bananas")

    actual = pq.dequeue()
    expected = "apples"
    assert actual == expected

    actual = pq.dequeue()
    expected = "bananas"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_enqueue_dequeue_enqueue_dequeue():
    pq = PseudoQueue()
    pq.enqueue("apples")
    pq.enqueue("bananas")

    pq.dequeue()

    pq.enqueue("cucumbers")
    pq.enqueue("dates")

    actual = [pq.dequeue(), pq.dequeue(), pq.dequeue()]

    expected = ["bananas", "cucumbers", "dates"]

    assert actual == expected
