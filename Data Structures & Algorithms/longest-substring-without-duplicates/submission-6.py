class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        length = 0
        parb=set()
        
        for r in range (len(s)):
            
            print(parb, length, s[r], s[l], len(s))
            while s[r] in parb:         # if s[r] in parb:
                parb.remove(s[l])       #   parb.remove(s[l]) --> nav fakts, ka s[l] ir tas kas jaiznem, varbut ir vairaki elementi pec kartas kas jaiznem tapec vajag ciklu
                l += 1                  #   l += 1
            parb.add(s[r])
            length = max(length, len(parb))              # else:
        return length                   #   parb.add(s[r])