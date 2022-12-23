class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1q ,s2q= '', ''
        for i in range(len(s1)) :
            if s1[i] != s2[i] :
                s1q += s1[i]
                s2q += s2[i]
        s2q = s2q[::-1]
        if len(s2q) == 0 :
            return True
        
        elif len(s2q) != 2 :
            return False
        elif s1q == s2q :
            return True 
        else : 
            return False 


