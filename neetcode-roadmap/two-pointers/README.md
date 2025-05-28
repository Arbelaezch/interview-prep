# Two Pointers Algorithm

Two Pointers is a fundamental algorithmic technique where you use two index variables (pointers) to traverse through data structures, typically arrays or strings. Instead of using nested loops, you strategically move these pointers based on certain conditions to solve problems more efficiently.

## Why Two Pointers Matters

Two Pointers transforms O(n²) brute force solutions into O(n) linear time solutions. This efficiency gain is crucial when working with large datasets in real applications like data processing, searching algorithms, and string manipulation tasks.

## Core Patterns

Two Pointers typically follows these patterns:

- **Opposite Direction**: Start pointers at both ends, move them toward each other
- **Same Direction**: Both pointers start at the beginning, move at different speeds
- **Sliding Window**: Expand/contract a window using two pointers

## Example: Two Sum II (Sorted Array)

**Problem**: Given a sorted array, find two numbers that add up to a target.

```python
def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left, right]  # Found our answer
        elif current_sum < target:
            left += 1  # Need a larger sum, move left pointer right
        else:
            right -= 1  # Need a smaller sum, move right pointer left
    
    return []  # No solution found
```

### Walkthrough with [2, 7, 11, 15], target = 9:

1. **Start**: left=0 (value 2), right=3 (value 15)
   - Sum: 2 + 15 = 17 > 9, so move right pointer left

2. **Step 2**: left=0 (value 2), right=2 (value 11)
   - Sum: 2 + 11 = 13 > 9, so move right pointer left

3. **Step 3**: left=0 (value 2), right=1 (value 7)
   - Sum: 2 + 7 = 9 = target! Return [0, 1]

**Time Complexity**: O(n) | **Space Complexity**: O(1)

The key insight is leveraging the sorted property: if our sum is too large, we need to decrease it by moving the right pointer left. If too small, we increase it by moving the left pointer right.

## Common Two Pointers Problems

### Opposite Direction Pattern
- **[Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)** (LeetCode 167)
- **[Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)** (LeetCode 125)
- **[3Sum](https://leetcode.com/problems/3sum/)** (LeetCode 15)
- **[Container With Most Water](https://leetcode.com/problems/container-with-most-water/)** (LeetCode 11)
- **[Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)** (LeetCode 42)

### Same Direction Pattern (Fast & Slow Pointers)
- **[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)** (LeetCode 26)
- **[Move Zeroes](https://leetcode.com/problems/move-zeroes/)** (LeetCode 283)
- **[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)** (LeetCode 141)
- **[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)** (LeetCode 19)

### Sliding Window Pattern
- **[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)** (LeetCode 3)
- **[Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)** (LeetCode 76)
- **[Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)** (LeetCode 438)
- **[Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)** (LeetCode 424)