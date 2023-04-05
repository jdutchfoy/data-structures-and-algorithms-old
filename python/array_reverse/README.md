# README.md

# Linked List Implementation
<!-- Description of the challenge -->

## Whiteboard Process
[Array_Reversed](Figjam Code Challenge 1.png)
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## Solution

- [ ] Top-level README “Table of Contents” is updated
 - [ ] README for this challenge is complete
       - [ ] Summary, Description, Approach & Efficiency, Solution
       - [ ] Picture of whiteboard
       - [ ] Link to code
 - [ ] Feature tasks for this challenge are completed
 - [ ] Unit tests written and passing
       - [ ] “Happy Path” - Expected outcome
       - [ ] Expected failure
       - [ ] Edge Case (if applicable/obvious)

# Example Tests

def sum(a,b):
  """ sum two numeric arguments """

  if isinstance(a, (int, float)) and isinstance(b, (int, float)):
    return a + b

  raise TypeError('argument must be int or float')

# Test the ‘Happy Path’ cases

def test_should_sum_two_integers():
    expected = 3
    actual = sum(1,2)
    assert expected is actual, "sum of 1 and 2 should be 3"

def test_should_sum_two_larger_integers():
    expected = 1333332
    actual = sum(1234567,98765)
    assert expected is actual, "sum of 1234567 and 98765 should be 1333332"

# Test with less obvious values. E.g. zero and negative numbers

def test_should_sum_negative_numbers():
    expected = 3
    actual = sum(5,-2)
    assert expected is actual, "sum of 5 and -2 should be 3"
# Test default argument values as needed

def test_should_handle_single_argument():
    expected = 2
    actual = sum(2)
    assert expected is actual, "sum of 2 and nothing should be 2 because 2nd argument defaults to 0"
# Test acceptable argument types

def test_should_sum_floats():
    expected = 5.0
    actual = sum(3.5,1.5)
    assert expected == actual, "sum of 3.5 and 1.5 should be 5.0"
def test_should_sum_integer_and_float():
    expected = 5.5
    actual = sum(3.5,2)
    assert expected == actual, "sum of 3.5 and 2 should be 5.5"

# Test unsupported argument types

def test_should_accept_only_numbers():
    # consult docs for how your test framework handles testing exceptions
    with pytest.raises(TypeError):
        sum('1',3)
