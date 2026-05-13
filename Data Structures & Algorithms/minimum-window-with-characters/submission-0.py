class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s): return ''
        
        dict1 = {}
        dict2 = {}
        
        for n in range(len(t)):
            if t[n] not in dict1:
                dict1[t[n]] = 1
               
            else:
                dict1[t[n]] += 1
        need=len(dict1)        
        print(dict1, need)

        l = 0
        have=0
        length = float('inf')
        resl=0
        resr=0

        for r in range(len(s)):
            if s[r] not in dict2 and s[r] in t:
                dict2[s[r]] = 1
                if dict2[s[r]] == dict1.get(s[r], 0):
                    have += 1
            elif s[r] in dict2 and s[r] in t:
                dict2[s[r]]+=1
                if dict2[s[r]] == dict1.get(s[r], 0):
                    have += 1
            # if have==need:
            while have==need:
                res = (l, r)
                resl=res[0]
                resr=res[1]
                length = min(length, resr-resl+1)
                print(res, length)
                if s[l] in dict2:
                    dict2[s[l]] -=1
                    if dict2[s[l]] == 0:
                        have-=1
                l+=1
                print(l, dict2)
        if length<float('inf'):
            return s[resl:resr+1]
        return ''
                
        print(dict2, have)     