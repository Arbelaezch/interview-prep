def maxSubArray(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    
    for i in range(1, len(nums)):
        # At each step, decide whether to start a new subarray or extend the existing one
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum