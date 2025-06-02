# Top K Frequent Elements

## Problem Description

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

**Example:**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Follow-up:** Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

## Why This Problem is Important

The Top K Frequent Elements problem is crucial in computer science and real-world applications for several reasons:

**Data Analysis Foundation**: This problem represents a fundamental pattern in data analysis - finding the most significant items in a dataset. This appears everywhere from business analytics to machine learning feature selection.

**Algorithm Design Mastery**: The problem showcases multiple algorithmic approaches, each with different trade-offs:
- Hash maps for counting
- Sorting for simple solutions
- Heaps for efficient top-k selection
- Bucket sort for optimal linear time

## Solution Approaches

### Solution 1: Hash Map + Sorting (Simple and Clean)
Count frequencies, then sort by frequency and take top k elements.

### Solution 2: Hash Map + Bucket Sort (Optimal overall)
Use bucket sort based on frequencies to achieve O(n) time complexity.

## Implementation

### Solution 1: Hash Map + Sorting (Simple and Clean)
```python
def topKFrequent(nums, k):
    """
    Find k most frequent elements using frequency counting and sorting.
    
    Time: O(n + m log m) where m = unique elements
    Space: O(m) for frequency map
    Note: Does not meet O(n log n) follow-up requirement in worst case
    """
    # Step 1: Count frequencies
    hashMap = {}
    for num in nums:
        if num not in hashMap:
            hashMap[num] = 1
        else:
            hashMap[num] += 1
    
    # Step 2: Sort by frequency and return top k
    return sorted(hashMap, key=hashMap.get, reverse=True)[:k]
```

### Solution 2: Bucket Sort Approach (Optimal Time)
```python
def topKFrequentBucket(nums, k):
    """
    Find k most frequent elements using bucket sort.
    
    Time: O(n) - optimal time complexity
    Space: O(n) for frequency map and buckets
    """
    # Step 1: Count frequencies
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1
    
    # Step 2: Create buckets for each possible frequency
    # Maximum frequency is len(nums) (all elements same)
    buckets = [[] for _ in range(len(nums) + 1)]
    
    # Step 3: Place elements in buckets based on frequency
    for num, freq in freq_map.items():
        buckets[freq].append(num)
    
    # Step 4: Collect top k elements from highest frequency buckets
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        if buckets[i]:
            result.extend(buckets[i])
            if len(result) >= k:
                break
    
    return result[:k]
```

## Complexity Analysis

### Hash Map + Sorting Approach
- **Time Complexity**: O(n + m log m)
  - O(n) to count frequencies where n = array length
  - O(m log m) to sort unique elements where m = number of unique elements
  - In worst case when m = n: O(n log n) - does not meet follow-up requirement
- **Space Complexity**: O(m)
  - O(m) for frequency map
  - O(m) for sorted keys list

### Bucket Sort Approach
- **Time Complexity**: O(n)
  - O(n) to count frequencies
  - O(n) to fill buckets
  - O(n) to collect results
  - Optimal time complexity
- **Space Complexity**: O(n)
  - O(n) for frequency map
  - O(n) for bucket array

## Algorithm Selection Guide

**Choose Hash Map + Sorting when:**
- Implementation simplicity is priority
- Code readability is most important
- Working with small to medium datasets
- Performance requirements are relaxed

**Choose Bucket Sort when:**
- You need optimal O(n) time complexity
- k can be large relative to n
- Memory usage of O(n) is acceptable

## Key Takeaways

1. **Multiple Valid Approaches**: Different algorithms excel in different scenarios - understand the trade-offs
2. **Bucket Sort Power**: Can achieve linear time when range of values is limited
3. **Frequency Counting Pattern**: Hash map for counting is fundamental - master this pattern
4. **Time Complexity Awareness**: Always consider whether O(n log n) solutions can be optimized
5. **Real-world Relevance**: This pattern appears constantly in data analysis and system design

This problem teaches essential skills for both competitive programming and practical software development, particularly in data-heavy applications.

## Learning Journey

I felt quite accomplished solving this problem with Hashmap + sorting in minutes. I did not see the follow-up that the solution's time should be O(n log n). The bucket solution is elegant and will be a good tool to have solving problems in the future. Either way, I am proud of myself for being able to solve this problem close to optimally.
