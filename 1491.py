

class Solution:
    def average(self, salary= list) -> float:
        high = max(salary)
        low = min(salary)
        salary.remove(high)
        salary.remove(low)
        count , sum_num = 0 ,0
        for i in salary:
            sum_num += i 
            count += 1 
        ave = sum_num / count
        return ave
