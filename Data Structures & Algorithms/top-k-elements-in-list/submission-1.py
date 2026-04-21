import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_f={}
        for num in nums:
            if num not in num_f:
                num_f[num]=1
               
            elif num in num_f:
                num_f[num]+=1
        heap=[]
        for num, freq in num_f.items():
            heapq.heappush(heap, (-freq, num))
        heapq.heapify(heap)
        list=[]
        for num in range(k):
            num=heapq.heappop(heap)[1]
            list.append(num)
        return list
        