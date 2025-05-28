from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        length = len(nums)
        x = 0
        y = 0

        while nums[x] < range(len(nums)):
            while nums[y] < range(len(nums)):
                if nums[x] + nums[y] == target:
                    return [x, y]       
            x += 1
            y = x + 1