from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number = set(nums)
        longest = 0
        for i in number:
            if i-1 not in number:
                length = 1
                while i+1 in number:
                    i+=1
                    length+=1
                longest = max(length, longest)
        return longest

sol = Solution()
print(sol.longestConsecutive([2,20,4,10,3,4,5]))