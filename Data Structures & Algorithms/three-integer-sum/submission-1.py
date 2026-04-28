class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        right = len(nums) - 1
        sorted_nums = sorted(nums)
        result = set()
        for i in range(len(sorted_nums)):
            fixed = sorted_nums[i]
            left = i + 1
            right = len(sorted_nums) - 1
            while left < right:
                sums = sorted_nums[left] + sorted_nums[right]
                if -fixed > sums:
                 right-= 1
                elif -fixed < sums:
                    left += 1
                else:
                    # un tagad addojam seta?
                    result.add(tuple([fixed, sorted_nums[left], sorted_nums[right]]))
                    left+=1
                    right-=1
        print(sorted_nums)
        print(result)
        return [list(t) for t in result]