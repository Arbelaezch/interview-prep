# LeetCode 20: Valid Parentheses (Easy)

Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets
2. Open brackets must be closed in the correct order
3. Every close bracket has a corresponding open bracket of the same type

## Example Cases

### Example 1:
```
Input: s = "()"
Output: true
Explanation: The parentheses are properly matched and closed.
```

### Example 2:
```
Input: s = "()[]{}"
Output: true
Explanation: All three types of brackets are properly matched and closed in order.
```

### Example 3:
```
Input: s = "(]"
Output: false
Explanation: The opening parenthesis '(' is closed by a bracket ']', which is incorrect.
```

### Example 4:
```
Input: s = "([)]"
Output: false
Explanation: The brackets are not closed in the correct order.
```

### Example 5:
```
Input: s = "{[]}"
Output: true
Explanation: The brackets are properly nested and closed in the correct order.
```

## Solution Approach

The key insight is to use a **stack** data structure. When we encounter:
- An **opening bracket** (`(`, `{`, `[`) → push it onto the stack
- A **closing bracket** (`)`, `}`, `]`) → check if it matches the most recent opening bracket (top of stack)

If at any point the brackets don't match or we try to close when the stack is empty, the string is invalid. At the end, the stack should be empty for a valid string.

## Python Solution

```python
def isValid(self, s: str) -> bool:
        # Element is either opening or closing bracket.
        # If first element is closing, then false.
        
        # If first element is opening, move to next element.
        # If next element is opening, move to next element. If closing, it needs to be the same type as the last element.

        stack = []
        hashMap = {')': '(', ']': '[', '}': '{'}

        for e in s:
            if not stack and e in hashMap.keys()
                return False

            # If stack is empty, add element.
            if not stack or e in hashMap.values():
                stack.append(e)
            elif e in hashMap.keys():
                if stack[-1] == hashMap[e]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False
```


## Time and Space Complexity

### Time Complexity: **O(n)**
- We iterate through the string once, where n is the length of the string
- Each push and pop operation on the stack takes O(1) time
- Overall: O(n)

### Space Complexity: **O(n)**
- In the worst case, we might push all characters onto the stack
- This happens when the string contains only opening brackets: `"((([[["`
- The stack can grow up to the size of the input string
- Overall: O(n)

## Learning Journey

I was able to solve this one in my first go as well. I think my strategy of learning broadly has been working. I feel confident that I can re-create any solutions I have already gone over, and my ability to solve new problems, while slow, is successfull. My use of built in Python methods has improved quite a bit as well. What tripped me up the most with this problem was figuring out how to compare the same types of brackets i.e. '[' and ']' are the same type. Recognizing that a dictionary's key could be set to the type broke this whole problem wide open. My confidence is through the roof.
