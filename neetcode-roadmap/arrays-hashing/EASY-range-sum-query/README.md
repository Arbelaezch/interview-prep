# Range Sum Query - Immutable (LeetCode 303)

## Problem Statement

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

- `NumArray(int[] nums)` Initializes the object with the integer array nums.
- `int sumRange(int left, int right)` Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

## Approaches

### Naive Solution

Store the array and calculate sum for each query by iterating through the range.

```python
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
    
    def sumRange(self, left: int, right: int) -> int:
        total = 0
        for i in range(left, right + 1):
            total += self.nums[i]
        return total
```

**Time Complexity:** O(1) for initialization, O(n) for each sumRange query where n is the size of the range
**Space Complexity:** O(1) additional space (just storing the original array)

**Problems with this approach:**
- If we have many queries, we're recalculating sums repeatedly
- For m queries, total time complexity becomes O(m × n)
- Very inefficient for frequent range sum operations

### Optimal Solution

Use prefix sum array to precompute cumulative sums, enabling O(1) range queries.

```python
class NumArray:
    def __init__(self, nums: List[int]):
        # Build prefix sum array with extra 0 at beginning
        self.prefixSum = [0]
        for num in nums:
            self.prefixSum.append(self.prefixSum[-1] + num)
    
    def sumRange(self, left: int, right: int) -> int:
        # Range sum = prefixSum[right+1] - prefixSum[left]
        return self.prefixSum[right + 1] - self.prefixSum[left]
```

**Time Complexity:** O(n) for initialization, O(1) for each sumRange query
**Space Complexity:** O(n) for storing the prefix sum array

**Why this works:**
- `prefixSum[i]` stores the sum of all elements from index 0 to i-1
- To get sum from left to right: take "sum up to right" minus "sum up to left-1"
- The extra 0 at the beginning handles edge cases cleanly

## Learning Journey

I was learning about prefix sums when I figured I should do a problem to help solidify my understanding. My previous walkthroughs of prefix sums made this problem easy to solve. It's a funny thing, going from not grasping a concept at all, to being able to use it to solve a problem. This is part of the addictiveness of learning. You slowly accrue more skills to solve any problems that come your way.