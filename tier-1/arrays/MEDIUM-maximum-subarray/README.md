# Maximum Subarray Problem

## Problem Statement
The Maximum Subarray problem asks us to find the contiguous subarray within an array of integers that has the largest sum. This is a fundamental problem in computer science.

## Naive Solution
The naive approach examines every possible subarray and keeps track of the maximum sum found.

```python
def maxSubArray(nums):
    max_sum = nums[0]
    
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
            
    return max_sum
```

**Time Complexity:** O(n²) - For each starting position, we consider all possible ending positions.
**Space Complexity:** O(1) - Only a constant amount of extra space is used.

## Optimal Solution: Kadane's Algorithm
Kadane's algorithm uses dynamic programming to solve this problem in linear time by maintaining two variables: the maximum sum ending at the current position and the global maximum sum found so far.

```python
def maxSubArray(nums):
    current_sum = max_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

**Time Complexity:** O(n) - We make a single pass through the array.  
**Space Complexity:** O(1) - Only a constant amount of extra space is used.

## Divide and Conquer Approach
The divide and conquer approach splits the array into halves, finds the maximum subarray in each half, and also finds the maximum subarray that crosses the middle.

**Time Complexity:** O(n log n) - We divide the problem into two subproblems of half the size and combine results in linear time.

Despite its elegance, the divide and conquer approach is not more efficient than Kadane's algorithm because O(n) is better than O(n log n). The logarithmic factor in the divide and conquer approach represents the number of recursive splits, making it slower for large inputs. However, this approach can be valuable in parallel computing environments where different subproblems can be solved simultaneously.

## Learning Journey
Initially, I had trouble with this problem. I was focused too much on the indexing of the sub-array and not enough on the actual maximum value. 