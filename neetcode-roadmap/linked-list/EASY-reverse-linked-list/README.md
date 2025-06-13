# LeetCode Problem: [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

## Problem Overview

The "Reverse Linked List" problem asks you to reverse a singly linked list. Given the head of a singly linked list, return the head of the reversed list.

**Example:**
```
Input:  1 -> 2 -> 3 -> 4 -> 5 -> NULL
Output: 5 -> 4 -> 3 -> 2 -> 1 -> NULL
```

## Why This Problem is Important

- **Pointer Manipulation:** Essential for understanding how linked data structures work
- **In-Place Operations:** Teaches efficient memory usage by modifying existing structure
- **Undo Operations:** Reversing action history in applications

## Solution Walkthrough

### Approach: Iterative with Three Pointers

The key insight is to reverse the direction of each link one at a time while keeping track of three nodes: previous, current, and next.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    """
    Reverse a singly linked list iteratively.
    
    Args: head: ListNode - Head of the original linked list
    
    Returns: ListNode - Head of the reversed linked list
    """
    # Initialize three pointers
    prev = None     # Previous node (initially None)
    curr = head     # Current node (start at head)
    
    # Traverse the list
    while curr:
        # Store the next node before we lose it
        next_temp = curr.next
        
        # Reverse the link
        curr.next = prev
        
        # Move pointers forward
        prev = curr
        curr = next_temp
    
    # prev is now the new head of the reversed list
    return prev
```

### Alternative: Recursive Solution

```python
def reverseListRecursive(head):
    """
    Reverse a singly linked list recursively.
    """
    # Base case: empty list or single node
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest of the list
    reversed_head = reverseListRecursive(head.next)
    
    # Reverse the current connection
    head.next.next = head
    head.next = None
    
    return reversed_head
```

## Complexity Analysis

### Iterative Solution
- **Time Complexity:** O(n)
  - We visit each node exactly once
  - Each operation per node is O(1)
  - Total: O(n) where n is the number of nodes

- **Space Complexity:** O(1)
  - Only uses a constant amount of extra space
  - Three pointer variables regardless of input size
  - True in-place algorithm

### Recursive Solution
- **Time Complexity:** O(n)
  - Same reasoning as iterative approach
  - Each recursive call processes one node

- **Space Complexity:** O(n)
  - Recursive call stack goes n levels deep
  - Each call frame takes constant space
  - Total space: O(n) for the call stack

## Learning Journey

I love this problem. I haven't tackled linked lists since my university days so this was a great refresher. Using three pointer variables to walk from head to tail is a clever strategy that will be a useful tool to know. Took a good amount of walking through the solution to full understand it, but it's absolutely worth it.
