class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        sum_num = 0 
        multi_num = 1
        for num in n :
            sum_num += int(num)
            multi_num *= int(num)
        ans = multi_num - sum_num
        return ans

a = Solution()
ans= a.subtractProductAndSum(n=4421)
print(ans)