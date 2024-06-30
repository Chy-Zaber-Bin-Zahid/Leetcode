from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for idx, i in enumerate(nums):
            if (target - i) in hashMap:
                return [idx, hashMap[target - i]]
            hashMap[i] = hashMap.get(nums[idx], idx) 

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))