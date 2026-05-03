class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        sum_=0
        for token in tokens:
            try:
                 stack.append(int(token))
            except ValueError:
                pass
            if token in '+-/*':       
                a=stack.pop()
                b=stack.pop()
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
                    sum_=int(b/a)
                    stack.append(sum_)
        print(stack)
        return sum_