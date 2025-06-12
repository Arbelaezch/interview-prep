# Binary Search Algorithm

Binary search is a highly efficient search algorithm that finds the position of a target value within a **sorted array**. It works by repeatedly dividing the search interval in half, comparing the target with the middle element, and eliminating half of the remaining elements in each step.

The key insight is that in a sorted array, if the middle element is greater than our target, we know the target (if it exists) must be in the left half. If the middle element is smaller than our target, the target must be in the right half.

## Why is Binary Search Important?

Binary search is crucial for several reasons:

- **Efficiency**: It reduces search time from O(n) to O(log n), making it exponentially faster for large datasets
- **Scalability**: The difference becomes dramatic as data size grows (searching 1 million elements takes at most 20 comparisons)
- **Foundation**: It's a building block for many advanced algorithms and data structures
- **Real-world applications**: Used in databases, file systems, and anywhere fast searching is needed
- **Interview relevance**: Commonly tested in technical interviews as it demonstrates understanding of divide-and-conquer principles

## Problem Example: Search in Sorted Array

Here's a classic binary search problem and its solution:

### Problem Statement
Given an integer array `nums` sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, return its index. Otherwise, return -1.

### Solution

```python

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int] - Ordered in ascending order
        :type target: int
        :rtype: int - Return index, or -1 if not found
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # Use integer division (//) instead of floor()
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # Target is in left half
                right = mid - 1
            else:
                # Target is in right half
                left = mid + 1
        
        return -1
```

## Time and Space Complexity

- **Time Complexity**: O(log n)
  - Each comparison eliminates half of the remaining elements
  - Maximum comparisons needed: ⌈log₂(n)⌉
  - For 1,000,000 elements, maximum 20 comparisons needed

- **Space Complexity**: O(1)
  - Uses only a constant amount of extra space
  - No recursion in iterative implementation (recursive version would be O(log n) space)

## Other LeetCode Problems Using Binary Search

Binary search is versatile and appears in many problem variations:

### Direct Applications
- **LeetCode 35**: Search Insert Position
- **LeetCode 278**: First Bad Version  
- **LeetCode 374**: Guess Number Higher or Lower
- **LeetCode 69**: Sqrt(x)

### Search in Modified Arrays
- **LeetCode 33**: Search in Rotated Sorted Array
- **LeetCode 81**: Search in Rotated Sorted Array II
- **LeetCode 153**: Find Minimum in Rotated Sorted Array
- **LeetCode 162**: Find Peak Element

### Binary Search on Answer Space
- **LeetCode 4**: Median of Two Sorted Arrays
- **LeetCode 875**: Koko Eating Bananas
- **LeetCode 1011**: Capacity To Ship Packages Within D Days
- **LeetCode 410**: Split Array Largest Sum

### Finding Boundaries
- **LeetCode 34**: Find First and Last Position of Element in Sorted Array
- **LeetCode 278**: First Bad Version
- **LeetCode 852**: Peak Index in a Mountain Array

## Learning Journey

Binary search is intuitively easy for me, but implementing it has always tripped me up. You can see my most recent attempt in the `my_first_try_in_10_years.py` file. It does not handle indexing properly and I try to divide an int by a float which is not allowed. I will have to improve and drill it into my brain if I want to use it to solve more complex problems.
