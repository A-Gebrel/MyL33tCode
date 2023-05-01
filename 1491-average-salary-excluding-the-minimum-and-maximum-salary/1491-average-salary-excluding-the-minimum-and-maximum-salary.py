class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop(0)
        salary.pop()
        total = 0
        for i in salary:
            total += i
        total = total / len(salary)
        return total