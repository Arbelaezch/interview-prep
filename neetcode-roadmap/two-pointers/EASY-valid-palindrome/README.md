# Valid Palindrome

## Problem Description

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

**Example 1:**
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

## Solution

```python
def isPalindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True
```

## Complexity Analysis

- **Time Complexity:** O(n) - We traverse the string once with two pointers
- **Space Complexity:** O(1) - Only using constant extra space for the pointers

## Learning Journey

I have already completed Two Sum II, so this was quite easy. The only trip up is being able to verify the pointer is on an alphanumeric character. I had to google isalnum(), and who knows if you'd be allowed to use it in an interview. Regex would be another solution, but you need to import (you also need to write regex lol). Either way, I was able to solve the problem on my own, I just need to memorize some of python's string methods.
