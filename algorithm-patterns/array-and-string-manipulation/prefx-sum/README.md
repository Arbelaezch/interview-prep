# Prefix Sum

Prefix Sum is a preprocessing technique that allows for efficient calculation of range sums in arrays. By pre-computing cumulative sums, we can answer range sum queries in O(1) time after O(n) preprocessing.

## Core Concept

Given an array `arr`, the prefix sum array `prefixSum` is constructed where:
- `prefixSum[i] = arr[0] + arr[1] + ... + arr[i]`

This enables us to calculate the sum of any subarray `arr[i...j]` using:
- `sum(i, j) = prefixSum[j] - prefixSum[i-1]`

## Walkthrough

Imagine you have an array `[2, 3, 1, 4, 5]` and need to answer multiple questions about range sums:

- What's the sum from index 1 to 3? (elements 3, 1, 4)
- What's the sum from index 0 to 2? (elements 2, 3, 1)
- What's the sum from index 2 to 4? (elements 1, 4, 5)

How would you solve this efficiently?

## The Naive Approach

Without any preprocessing, for each question we'd loop through the range and add up the elements:

```
Array: [2, 3, 1, 4, 5]
Index:  0  1  2  3  4

Question 1: Sum from index 1 to 3
- Loop: 3 + 1 + 4 = 8

Question 2: Sum from index 0 to 2  
- Loop: 2 + 3 + 1 = 6

Question 3: Sum from index 2 to 4
- Loop: 1 + 4 + 5 = 10
```

**Time Complexity**: O(n) per query, where n is the range size
**Problem**: If we have many queries, we're doing repeated work

## The Prefix Sum Solution

Instead of recalculating sums repeatedly, we can precompute all cumulative sums once. This is called building a **prefix sum array**.

### Step 1: Build the Prefix Sum Array

Starting with our original array:
```
Original: [2, 3, 1, 4, 5]
Index:     0  1  2  3  4
```

We create a prefix sum array where each position stores the cumulative sum up to that point:

```
prefixSum[0] = 0                    (starting point)
prefixSum[1] = 0 + 2 = 2           (sum up to index 0)
prefixSum[2] = 2 + 3 = 5           (sum up to index 1) 
prefixSum[3] = 5 + 1 = 6           (sum up to index 2)
prefixSum[4] = 6 + 4 = 10          (sum up to index 3)
prefixSum[5] = 10 + 5 = 15         (sum up to index 4)
```

**Result**: `prefixSum = [0, 2, 5, 6, 10, 15]`

### Step 2: Answer Queries in O(1) Time

Now we can answer any range sum query using the formula:
```
sum(i to j) = prefixSum[j+1] - prefixSum[i]
```

Let's solve our three questions:

**Question 1: Sum from index 1 to 3**
```
sum(1 to 3) = prefixSum[4] - prefixSum[1] = 10 - 2 = 8
Verification: [3, 1, 4] → 3 + 1 + 4 = 8 ✓
```

**Question 2: Sum from index 0 to 2**
```
sum(0 to 2) = prefixSum[3] - prefixSum[0] = 6 - 0 = 6
Verification: [2, 3, 1] → 2 + 3 + 1 = 6 ✓
```

**Question 3: Sum from index 2 to 4**
```
sum(2 to 4) = prefixSum[5] - prefixSum[2] = 15 - 5 = 10
Verification: [1, 4, 5] → 1 + 4 + 5 = 10 ✓
```

## Why Does This Work?

Think of prefix sums like a running total. `prefixSum[4]` contains the sum of everything from the start up to index 3. `prefixSum[1]` contains the sum of everything from the start up to index 0.

When we calculate `prefixSum[4] - prefixSum[1]`, we're subtracting out the "start up to index 0" part, leaving us with exactly the sum from index 1 to index 3.

**Visual representation**:
```
prefixSum[4] = [2, 3, 1, 4] = 10
prefixSum[1] = [2] = 2
Difference   = [3, 1, 4] = 8
```

It's like measuring distance traveled: if your odometer reads 100 miles and it read 30 miles at your last checkpoint, you traveled 70 miles between checkpoints.

## Complexity Analysis

| Operation | Naive Approach | Prefix Sum Approach |
|-----------|----------------|-------------------|
| Preprocessing | O(1) | O(n) |
| Single Query | O(k) where k = range size | O(1) |
| Multiple Queries | O(m×k) where m = number of queries | O(n + m) |

**Key Insight**: We trade O(n) preprocessing time for O(1) query time. This is massively beneficial when we have many queries!

## Simple Implementation

```python
def build_prefix_sum(arr):
    """Build prefix sum array with extra 0 at beginning"""
    prefix_sum = [0]
    for num in arr:
        prefix_sum.append(prefix_sum[-1] + num)
    return prefix_sum

def range_sum(prefix_sum, left, right):
    """Get sum from index left to right (inclusive)"""
    return prefix_sum[right + 1] - prefix_sum[left]

# Example usage
arr = [2, 3, 1, 4, 5]
prefix = build_prefix_sum(arr)  # [0, 2, 5, 6, 10, 15]

print(range_sum(prefix, 1, 3))  # 8
print(range_sum(prefix, 0, 2))  # 6  
print(range_sum(prefix, 2, 4))  # 10
```

## When to Recognize This Pattern

Use prefix sum when you see:
- Multiple range sum queries on the same array
- Problems asking about subarrays with specific sum properties
- Questions involving cumulative effects or running totals
- Need to optimize from O(n) per query to O(1) per query

## Popular LeetCode Problems

Here are the most common interview problems that use prefix sum:

**Easy:**
- [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)
- [1588. Sum of All Odd Length Subarrays](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/)

**Medium:**
- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) **(Very Popular)**
- [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)
- [525. Contiguous Array](https://leetcode.com/problems/contiguous-array/)
- [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
- [304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)

**Hard:**
- [327. Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/)

**Most Important**: Start with problems #303 and #560 - they perfectly demonstrate the core concepts and are frequently asked in interviews.

The key is recognizing that many "subarray" problems are actually prefix sum problems in disguise!