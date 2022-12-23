class Solution:
    def canMakeArithmeticProgression(self, arr: list) -> bool:
        arr.sort()
        arr = arr[::-1]
        ref = arr[-2] - arr[-1]
        if len(arr) > 2 :
            for i in range(len(arr) -2) :
                sub = arr[i] - arr[i+1]
                if sub != ref :
                    return False
                    break
            else:
                return True
        else:
            return True
            