# Contains Duplicate

## Problem Description
Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

## Naive Solution
```python
def containsDuplicate(self, nums: List[int]) -> bool:
    i = 0
    j = i+1
    length = len(nums)

    while i < length:
        while j < length:
            if nums[i] == nums[j]:
                return True

            j += 1
        i +=1
        j = i + 1

    return False
```

### Complexity Analysis - Naive Solution
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)

## Optimal Solution
```python
def containsDuplicate(self, nums: List[int]) -> bool:
    hash_set = set()
    for num in nums:
        if num in hash_set:
            return True
        hash_set.add(num)
    return False
```

### Complexity Analysis - Optimal Solution
- **Time Complexity**: O(n)
  - We traverse the array only once
  - Each lookup and insertion operation in a hash set is O(1) on average
- **Space Complexity**: O(n)
  - In the worst case, we might need to store all elements in the hash set (when there are no duplicates)

## Learning Journey
Because of the similarity between the Two Sum and Contains Duplicate problems, I was able to quickly, and intuitively adapt the optimal solution to the Contains Duplicate problem. The big difference is that instead of looking for a complement value (as in Two Sum), we're simply checking if we've seen the current value before.