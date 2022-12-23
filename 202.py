class Solution:
    def isHappy(self, n: int) -> bool:
        ss = 1000
        n = str(n)
        counter = 0  
        while counter <= ss :
            counter += 1 
            ans = 0
            for i in n :
                ans += int(i)** 2 
            n = str(ans) 
            if n == '1' :
                return True
                break
            elif counter == ss :
                return False
                break
