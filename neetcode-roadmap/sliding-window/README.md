# Sliding Window Technique

## Overview

The sliding window technique is a powerful algorithmic approach used to solve problems involving contiguous subarrays or substrings. Instead of examining every possible subarray (which would be O(n²) or O(n³)), sliding window maintains a "window" that expands and contracts as it moves through the data structure, achieving optimal O(n) time complexity.

The technique works by maintaining two pointers (typically called `left` and `right`) that define the boundaries of the current window. As you iterate through the data, you:
- Expand the window by moving the right pointer
- Contract the window by moving the left pointer when certain conditions are met
- Keep track of the optimal result as the window slides

## Why It's Useful and Important

**Efficiency**: Transforms brute force O(n²) or O(n³) solutions into O(n) solutions by avoiding redundant calculations.

**Memory Optimization**: Usually requires only O(1) extra space regardless of input size.

**Pattern Recognition**: Once you recognize the sliding window pattern, many seemingly complex problems become straightforward.

**Real-world Applications**: Useful for problems involving:
- Network packet analysis (finding patterns in data streams)
- Financial analysis (moving averages, trend detection)
- Text processing (finding substrings with specific properties)
- Resource allocation (managing fixed-size buffers)

## Detailed Example: Longest Substring Without Repeating Characters

**Problem**: Given a string, find the length of the longest substring without repeating characters.

**Example**: `"abcabcbb"` → Answer: `3` (substring `"abc"`)

### Step-by-Step Walkthrough

```python
def lengthOfLongestSubstring(s):
    if not s:
        return 0
    
    left = 0
    char_set = set()
    max_length = 0
    
    for right in range(len(s)):
        # Expand window: add current character
        while s[right] in char_set:
            # Contract window: remove characters from left until no duplicates
            char_set.remove(s[left])
            left += 1
        
        # Add current character to our window
        char_set.add(s[right])
        
        # Update maximum length seen so far
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

### Trace Through Example: `"abcabcbb"`

| Step | right | s[right] | left | Window | char_set | max_length |
|------|-------|----------|------|---------|----------|------------|
| 1    | 0     | 'a'      | 0    | "a"     | {'a'}    | 1          |
| 2    | 1     | 'b'      | 0    | "ab"    | {'a','b'} | 2          |
| 3    | 2     | 'c'      | 0    | "abc"   | {'a','b','c'} | 3      |
| 4    | 3     | 'a'      | 0    | Found duplicate! Contract window... |  |   |
|      |       |          | 1    | "bca"   | {'b','c','a'} | 3      |
| 5    | 4     | 'b'      | 1    | Found duplicate! Contract window... |  |   |
|      |       |          | 2    | "cab"   | {'c','a','b'} | 3      |
| 6    | 5     | 'c'      | 2    | Found duplicate! Contract window... |  |   |
|      |       |          | 3    | "abc"   | {'a','b','c'} | 3      |

**Key Insights**:
- Window expands by moving `right` pointer
- Window contracts by moving `left` pointer when duplicates are found
- We maintain the invariant that our window contains no duplicate characters
- Time complexity: O(n) - each character is visited at most twice
- Space complexity: O(min(m,n)) where m is the size of the character set

## Sliding Window vs. Two Pointers: Key Differences

While sliding window and two pointers both use multiple pointers, they serve different purposes and have distinct characteristics:

### Sliding Window Characteristics
- **Purpose**: Find optimal contiguous subarrays/substrings
- **Window Constraint**: Maintains a contiguous range [left, right]
- **Movement Pattern**: Right pointer always moves forward; left pointer moves forward to shrink window
- **Data Structure**: Often uses additional data structures (HashSet, HashMap) to track window contents
- **Focus**: The entire range/subarray within the window matters

```python
# Sliding Window Example: Longest substring without repeating characters
def lengthOfLongestSubstring(s):
    left = 0
    char_set = set()  # Tracks what's IN the window
    max_length = 0
    
    for right in range(len(s)):  # Right always moves forward
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1  # Left moves forward to shrink window
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)  # Window size matters
```

### Two Pointers Characteristics
- **Purpose**: Find pairs of elements that satisfy a condition
- **Movement Freedom**: Pointers can move toward or away from each other
- **Data Focus**: Only cares about elements AT the pointer positions, not between them
- **No Window**: Doesn't maintain a contiguous range concept
- **Simpler State**: Usually no additional data structures needed

```python
# Two Pointers Example: Two Sum in sorted array
def twoSum(nums, target):
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]  # Only care about these two elements
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1      # Move closer together
        else:
            right -= 1     # Move closer together
        # No tracking of elements between left and right
```

### When to Use Which Technique

**Use Sliding Window when:**
- Problem mentions "contiguous subarray/substring"
- You need to track what's inside a range
- Looking for optimal window size or properties
- Keywords: "longest", "shortest", "contains all", "without repeating"

**Use Two Pointers when:**
- Looking for pairs that meet criteria
- Working with sorted arrays
- Need to check elements from both ends
- Keywords: "two sum", "closest to target", "remove duplicates"

### Hybrid Approaches
Some problems combine both techniques, but they maintain distinct roles:
- Sliding window for maintaining the valid range
- Two pointers within that range for specific pair-finding logic

## Common Sliding Window Patterns

1. **Fixed Window Size**: Window size remains constant (e.g., maximum sum of k consecutive elements)
2. **Variable Window Size**: Window grows and shrinks based on conditions (e.g., longest substring with at most k distinct characters)
3. **Shrinking Window**: Window expands until invalid, then shrinks until valid again

## Relevant LeetCode Problems

### Easy
- **3. Longest Substring Without Repeating Characters**
- **209. Minimum Size Subarray Sum**
- **219. Contains Duplicate II**

### Medium  
- **424. Longest Repeating Character Replacement**
- **438. Find All Anagrams in a String**
- **567. Permutation in String**
- **713. Subarray Product Less Than K**
- **904. Fruit Into Baskets**
- **930. Binary Subarrays With Sum**
- **992. Subarrays with K Different Integers**
- **1004. Max Consecutive Ones III**
- **1052. Grumpy Bookstore Owner**
- **1234. Replace the Substring for Balanced String**

### Hard
- **76. Minimum Window Substring**
- **239. Sliding Window Maximum**
- **480. Sliding Window Median**

## Tips for Recognition

Look for sliding window when you see:
- "Contiguous subarray/substring"
- "Maximum/minimum length"
- "All subarrays/substrings with property X"
- "Find the optimal window/range"
- Problems that seem to require nested loops but involve contiguous elements

The key insight is recognizing when you can maintain useful information about your current window and avoid recalculating everything from scratch as the window moves.