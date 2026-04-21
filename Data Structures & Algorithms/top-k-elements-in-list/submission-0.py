class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_f={}
        for num in nums:
            if num not in num_f:
                num_f[num]=1
               
            elif num in num_f:
                num_f[num]+=1
        # res=sorted(list(num_f.keys()))
        # return res[-k:]
        return sorted(num_f.keys(), key=lambda x: num_f[x])[-k:]
        

