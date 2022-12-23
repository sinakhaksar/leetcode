class Solution:
    def maximumWealth(self, accounts: list) -> int:
        sums = 0
        for i in accounts :
            if sum(i) >= sums :
                    sums = sum(i)
        return sums