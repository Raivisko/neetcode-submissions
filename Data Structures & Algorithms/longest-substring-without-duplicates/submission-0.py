class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        length = 0
        parb=set()
        
        for r in range (len(s)):
            length = max(length, len(parb))
           
            while s[r] in parb:         # if s[r] in parb:
                parb.remove(s[l])       #   parb.remove(s[l]) --> nav fakts, ka s[l] ir tas kas jaiznem, varbut ir vairaki elementi pec kartas kas jaiznem tapec vajag ciklu
                l += 1                  #   l += 1
            parb.add(s[r])              # else:
        return length                   #   parb.add(s[r])