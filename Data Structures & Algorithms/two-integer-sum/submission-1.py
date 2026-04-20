class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for index, num in enumerate(nums):
            diff=target-num
            if diff not in dict:
                dict[num]=index 
            else:
                return [dict[diff], index]     