# Q = 1480
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        rus = []
        for i in range(len(nums)) : 
            jam = sum(nums[: i +1])
            rus.append(jam)
        return rus
