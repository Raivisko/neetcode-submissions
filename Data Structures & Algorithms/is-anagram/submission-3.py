class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}

        for c in s:
            freq_s[c] = freq_s.get(c, 0) + 1

        for z in t:
            freq_t[z] = freq_t.get(z, 0) + 1
        
        return freq_s == freq_t