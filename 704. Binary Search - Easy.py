from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        midIndex = r // 2
        while r >= l:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[midIndex] == target:
                return midIndex
            else:
                if nums[midIndex] > target:
                    r = midIndex-1
                else:
                    l = midIndex+1
                midIndex = (r+l) // 2
        return -1


sol = Solution()
print(sol.search([-1,0,3,5,9,12],13))