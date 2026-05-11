class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict={}
        l=0
        res = 0
        for r in range(len(s)):
            if s[r] not in dict:
                dict[s[r]]=1
            else:
                dict[s[r]]+=1

            max_freq=max(dict.values())
            # replace = window - max_freq
            if( (r - l + 1) - max_freq)>k:
                dict[s[l]] -= 1
                l+=1
            window=len(s[l:r+1])
            res = max(res, window)
            # print(dict, window, max_freq, s[l:r+1])
        return res
            
            
