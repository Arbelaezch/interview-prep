def maxSubArray(nums):
        max_sum = nums[0]
        
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)
                
        return max_sum