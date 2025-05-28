def containsDuplicate(self, nums: List[int]) -> bool:
        i = 0
        j = i+1
        length = len(nums)

        while i < length:
            while j < length:
                if nums[i] == nums[j]:
                    return True

                j += 1
            i +=1
            j = i + 1


        return False