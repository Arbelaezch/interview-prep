# Group Anagrams

## Problem Description

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

## Why This Problem is Important

The Group Anagrams problem is fundamental in computer science and software engineering for several key reasons:

**Hash Map Mastery**: This problem demonstrates the power of hash maps for efficient grouping and categorization. Understanding when and how to use hash maps as the primary data structure is crucial for solving many real-world problems.

**Key Generation Strategy**: The problem teaches an important concept of creating canonical forms or normalized keys. This technique is widely applicable in data deduplication, caching systems, and database indexing.

## Solution Approach

The key insight is to use a **canonical representation** of each string as the grouping key. Since anagrams contain the same characters with the same frequencies, we can create a unique identifier for each anagram group.

### Strategy 1: Sorted Characters as Key
Sort the characters of each string. All anagrams will produce the same sorted string, which serves as our hash map key.

## Implementation

```python
def groupAnagrams(strs):
    """
    Group anagrams together using sorted string as key.
    
    Args:
        strs: List of strings to group
    
    Returns:
        List of lists, where each inner list contains anagrams
    """
    anagram_groups = {}
    
    for s in strs:
        # Sort the characters to create a canonical form
        sorted_str = ''.join(sorted(s))
        
        # Check if key exists, if not create empty list
        if sorted_str not in anagram_groups:
            anagram_groups[sorted_str] = []
        
        anagram_groups[sorted_str].append(s)
    
    return list(anagram_groups.values())
```

## Complexity Analysis

### Time Complexity: O(N × K × log K)
- **N**: Number of strings in the input array
- **K**: Maximum length of a string
- **log K**: Time to sort each string of length K
- We process each string once, and sorting each string takes O(K log K)

### Space Complexity: O(N × K)
- **Hash Map Storage**: In the worst case (no anagrams), we store all N strings
- **Key Storage**: Each key is at most K characters long
- **Output Storage**: The result contains all input strings grouped together

## Key Takeaways

1. **Hash Maps for Grouping**: When you need to group items by some property, consider using a hash map with that property as the key
2. **Canonical Forms**: Creating a standard representation helps identify equivalent items

## Learning Journey

This was a tough problem that I was not able to solve on my own, but I got close. I was on the right 
track trying to sort the characters, but I did not know of the sorted() method which makes the problem much easier.
