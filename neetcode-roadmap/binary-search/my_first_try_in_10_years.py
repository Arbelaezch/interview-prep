from math import floor

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
            - Ordered in ascending order
        :type target: int
        :rtype: int
            - Return just the index
            - Return -1 if not found

        Must be O(log n)
        """

        index = floor(len(nums)/2)

        while nums[index] != target:
            if index == 0 or index == (len(nums)-1):
                return -1
            if nums[index] > target:
                index = floor(len(nums[0:index])/2)
            elif nums[index] < target:
                index = index + floor(len(nums[index:]/2))

        return index