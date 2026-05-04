class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # y=3x+3, y=2x+5, y=x+7
        x=zip(position, speed) #x=[[p, s] for p, s in zip(position, speed)]
        desc_pos=sorted(x)[::-1]
        stack=[]
        for n in desc_pos:
            pos, v = n
            time= (target-pos)/v
            if not stack:
                stack.append(time)
            elif stack[-1] < time:
                stack.append(time)
        print(stack)
        return len(stack)