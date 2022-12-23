
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        high = int(high)
        low = int(low)
        if high % 2 != 0 :
            high = high + 1 
        elif low % 2 != 0 : 
            low = low - 1 
        allodds =int( high / 2 )
        beforelow = low / 2 
        odds = int(allodds) - int(beforelow)
        return odds        


a = Solution()
a.countOdds(low=3 , high=7)

