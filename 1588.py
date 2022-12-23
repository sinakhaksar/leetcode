

class Solution:
    def sumOddLengthSubarrays(self, arr: list) -> int:
        sumer = 0
        for i in range(0, len(arr)):
            n = 2 * i + 1 
            for i in range(0, len(arr)):
                aval = i
                a = arr[aval : aval + n]
                if len(a) == n:
                    sumer += sum(a)
        return sumer
        