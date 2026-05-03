class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        sum_=0
        for token in tokens:
            if token.isdigit():
                stack.append(token)
            elif token in '+-/*':       
                a=int(stack.pop())
                b=int(stack.pop())
                if token == '+':
                   sum_=b+a
                   stack.append(sum_)
                elif token == '-':
                    sum_=b-a
                    stack.append(sum_)
                elif token == '*':
                    sum_=b*a
                    stack.append(sum_)
                else:
                    sum_=b*a
                    stack.append(sum_)
        print(stack)
        return sum_