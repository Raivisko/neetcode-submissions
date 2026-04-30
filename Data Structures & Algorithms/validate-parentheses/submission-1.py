class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for c in s:
            if c in '({[':
                stack.append(c)
            elif len(stack)>0 and c in ')]}':
                stack.pop()
        return len(stack) == 0
