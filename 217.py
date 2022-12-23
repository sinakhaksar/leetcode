class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s_nums = set()
        for i in nums :
            if i in s_nums:
                return True
            else :
                s_nums.add(i)
        
