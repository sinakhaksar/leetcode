
class Solution:    
    def arraySign(self, nums: list) -> int:
        product = 1
        for i in nums :
            if i == 0 :
                return 0
                break
            else :
                product *= i 
        product =str(product)
        if product[0] == '-':
            return -1
        else:
            return 1

