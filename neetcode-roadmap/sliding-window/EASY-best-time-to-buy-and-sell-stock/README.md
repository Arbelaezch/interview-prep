# Best Time to Buy and Sell Stock

**LeetCode #121 - Easy**

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

**Example 1:**
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

## Why This Problem is Important to Understand

### Fundamental Algorithm Concepts
This problem teaches several crucial programming concepts:

**Single-Pass Optimization**: Demonstrates how to solve a problem efficiently in one pass through the data, avoiding the brute force O(n²) approach of checking every buy-sell pair.

**Greedy Algorithm Principles**: Shows how making locally optimal choices (always tracking the minimum price seen so far) leads to a globally optimal solution.

**State Tracking**: Illustrates the technique of maintaining running information about the best choice seen so far, which is applicable to many other problems.

## Solution and Complexity Analysis

```python
def maxProfit(self, prices: List[int]) -> int:
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0

    for current_price in prices[1:]:

        min_price = min(current_price, min_price)

        current_profit = current_price - min_price

        max_profit = max(max_profit, current_profit)
    
    return max_profit
```

### Algorithm Explanation

The solution uses a **greedy approach** with **running minimum tracking**:

### Key Insight
We don't need to track both buy and sell days explicitly. Instead, we:
- Always maintain the lowest price seen so far (optimal buy point)
- For each day, calculate what profit we'd get if we sold that day
- Keep track of the best profit we've seen

### Complexity Analysis

**Time Complexity: O(n)**
- Single pass through the prices array
- Each operation inside the loop is O(1)
- No nested loops or recursive calls

**Space Complexity: O(1)**
- Only using a constant amount of extra space
- Two variables (`min_price` and `max_profit`) regardless of input size
- No additional data structures that grow with input

### Why This Beats Brute Force

**Brute Force Approach** (checking every buy-sell pair):
```python
# DON'T DO THIS - O(n²) solution
def maxProfitBruteForce(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit
```

- Time Complexity: O(n²)
- Space Complexity: O(1)

Our optimized solution achieves the same result in O(n) time by recognizing that we only need to track the minimum price seen so far, not all possible buy points.

## Pattern Recognition

This problem exemplifies the **"Running Minimum/Maximum"** pattern, which appears in many other problems:
- Maximum subarray sum (Kadane's algorithm)
- Best time to buy and sell stock with multiple transactions
- Maximum difference between two elements in an array

Understanding this pattern helps solve a whole class of optimization problems efficiently.
