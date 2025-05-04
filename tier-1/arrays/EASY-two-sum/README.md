# Two Sum Problem

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to the target.

## Approaches

### Naive Solution (Brute Force)
My initial solution used a brute force approach with nested loops:

```python
def twoSum(nums, target):
    length = len(nums)
    x = 0
    y = 0

    while nums[x] < range(length):
        while nums[y] < range(length):
            if nums[x] + nums[y] == target:
                return [x, y]       
        x += 1
        y = x + 1
```

**Time Complexity:** O(n²) - We check every possible pair of numbers in the array.
**Space Complexity:** O(1) - We only use a constant amount of extra space.

### Optimal Solution (Hash Map)
After learning about hash maps, I implemented a much more efficient solution:

```python
def twoSum(nums, target):
    hash_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in hash_map:
            return [hash_map[complement], i]
        
        hash_map[num] = i
    
    return []
```

**Time Complexity:** O(n) - We only need to traverse the array once.
**Space Complexity:** O(n) - In the worst case, we might store all elements in the hash map.

## Learning Journey
I initially approached this problem with the intuitive brute force method, checking all possible pairs to find a matching sum. This solution worked but was inefficient for large arrays.

The breakthrough came when I learned about hash maps. I discovered that by storing each element's value as a key and its index as a value, I could check in constant time whether a number's complement exists in the array.

Hash maps work by:
1. Using a hash function to calculate where to store each key-value pair
2. Providing constant-time lookups for keys
3. Only storing each unique key once (newer values override older ones with the same key)
