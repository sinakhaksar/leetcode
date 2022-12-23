


class Solution:
    def largestPerimeter(self, nums: list) -> int:
        nums.sort()
        nums.reverse()
        for i in range(len(nums)):
            if nums[2] + nums[1] > nums[0] :
                ans = nums[2] + nums[1] + nums[0]
                return ans
                break
            elif len(nums) > 3 :
                nums.remove(nums[0])
            else: 
                return 0 


a = Solution()
ans = a.largestPerimeter(nums=list)
print(ans)