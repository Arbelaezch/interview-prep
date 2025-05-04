def twoSum(nums, target):
    hash_map = {}
    
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach target
        complement = target - num
        
        # Check if the complement exists in our hash map
        if complement in hash_map:
            # Return both indices if found
            return [hash_map[complement], i]
        
        # If not found, add the current number and index to hash map
        hash_map[num] = i
    
    return []