class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        dict1 = {}
        dict2 = {}

        for n in range(len(s1)):
            if s1[n] not in dict2:
                dict2[s1[n]] = 1
            else:
                dict2[s1[n]] += 1

        for r in range(len(s2)):
            if s2[r] not in dict1:
                dict1[s2[r]] = 1
            else:
                dict1[s2[r]]+=1
            
            if r>=len(s1):
                dict1[s2[l]] -=1
                if dict1[s2[l]] == 0:
                    del dict1[s2[l]]
                l+=1
                
            if dict1 == dict2:
                return True
           
        return False
           
            