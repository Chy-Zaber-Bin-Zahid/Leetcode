from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        l, r = 0, len(nums)-1
        while r>=l:
            m = (l+r) // 2
            if nums[m] > target and nums[l] <= target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                return nums[m]
            

sol = Solution()
print(sol.search([3,4,5,6,1,2], 1))