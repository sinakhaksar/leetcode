

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)) : 
            b = nums[i + 1 :]
            a = nums[:i]
            if sum(a) == sum(b) :
                return i
                break
        else :
            return -1
