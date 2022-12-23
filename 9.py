

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        cheek = x[::-1]
        if cheek == x :
            return True
        else:
            return False
