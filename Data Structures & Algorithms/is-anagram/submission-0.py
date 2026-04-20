class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq={}
        for str in s:
            if str not in s_freq:
                s_freq[str]=1    
            else:
                s_freq[str]+=1
                
        t_freq={}
        for str in t:
            if str not in t_freq:
                t_freq[str]=1
            else:
                t_freq[str]+=1

        return s_freq==t_freq
        