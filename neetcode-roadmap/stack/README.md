# Stack Data Structure

## What is a Stack?

A stack is a linear data structure that follows the **Last In, First Out (LIFO)** principle. Think of it like a stack of pringles chips - you can only add or remove chips from the top. The last chip you put on the stack is the first one you'll take off.

## Why are Stacks Important?

Stacks are fundamental in computer science because they:

- **Function Call Management**: Every programming language uses a call stack to manage function calls and returns
- **Expression Evaluation**: Used in compilers to evaluate mathematical expressions and handle operator precedence
- **Undo Operations**: Applications use stacks to implement undo functionality (Ctrl+Z)
- **Browser History**: Web browsers use stacks to manage the back button functionality
- **Memory Management**: Stack memory allocation is faster than heap allocation
- **Parsing**: Essential for parsing nested structures like parentheses, brackets, and braces

## Basic Stack Implementation

Here's a simple stack implementation in Python:

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add an item to the top of the stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return the top item without removing it"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # Output: 3
print(stack.peek()) # Output: 2
print(stack.size()) # Output: 2
```

## Time Complexity of Stack Operations

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Push      | O(1)           | O(1)            |
| Pop       | O(1)           | O(1)            |
| Peek/Top  | O(1)           | O(1)            |
| Search    | O(n)           | O(1)            |
| Size      | O(1)           | O(1)            |

The stack operations are highly efficient with constant time complexity for the main operations.

## LeetCode Problems Using Stacks

### Easy Problems:
- **Valid Parentheses** - Check if brackets are properly matched
- **Baseball Game** - Calculate score based on operations
- **Remove All Adjacent Duplicates In String** - Remove consecutive duplicate characters

### Medium Problems:
- **Min Stack** - Design a stack that supports getMin() in O(1)
- **Evaluate Reverse Polish Notation** - Calculate the result of RPN expressions
- **Daily Temperatures** - Find next warmer temperature for each day
- **Asteroid Collision** - Simulate asteroid collisions

### Hard Problems:
- **Largest Rectangle in Histogram** - Find the area of largest rectangle
- **Trapping Rain Water** - Calculate trapped rainwater
- **Valid Number** - Validate if string represents a valid number
