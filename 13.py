
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1, 'V':5,
        'X':10, 'L':50, 'C':100,
        'D': 500,'M':1000 }
        a = 0
        n= len(s)
        for i in range(n) : 
            if i != n -1: 
                si = int(dict.get(s[i]))
                sii = int(dict.get(s[i+1]))
                if si >= sii : 
                    a += si
                else : 
                    a += (sii - si)
                    a -= sii
            elif i == n-1 :
                a += dict.get(s[i])
        return a 


        