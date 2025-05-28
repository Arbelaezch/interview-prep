class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0]
        for num in nums:
            self.prefixSum.append(self.prefixSum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right+1] - self.prefixSum[left]