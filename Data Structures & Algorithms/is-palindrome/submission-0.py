class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum=[c for c in s.lower() if c.isalnum()]
        left=0
        right=len(alnum)-1
        print(alnum)
        while left<right:
            if alnum[left]!=alnum[right]:
                return False
            left+=1
            right-=1
            
        return True