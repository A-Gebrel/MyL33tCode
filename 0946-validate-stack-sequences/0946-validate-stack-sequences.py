class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for item in pushed:
            stack.append(item)
            while(len(stack) != 0 and stack[-1] == popped[i]):
                stack.pop()
                i += 1
        return len(stack) == 0