class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "+":
                num1 = stack[-1]
                num2 = stack[-2]
                # stack.append(num2)
                # stack.append(num1)
                stack.append(int(num1)+int(num2))
            elif i == "D":
                num = stack.pop()
                stack.append(num)
                stack.append(int(num)*2)
            elif i == "C":
                stack.pop()
            else:
                stack.append(i)
                
        total = 0
        for i in stack:
            total += int(i)
        return total