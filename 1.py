
nums = [2,7,11,15]
target = 9

# bad code : 

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)) :
            for b in range(len(nums)) : 
                if i != b : 
                    if nums[i] + nums[b] == target : 
                        return(i,b)
                        quit()   



#good code : 

class Solution:
    def twoSum(self, nums, target):
        numMap = dict()
        print('numMap is :', numMap)
        for i in range(len(nums)):
            print("i is :", i)
            complement = target - nums[i]
            print("complement is :", complement)
            if complement in numMap:
                print([numMap[complement], i])
            numMap[nums[i]] = i



nums = [2,7,11,15]
target = 9
