from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashMap = {}
        for i in nums:
            hashMap[i] = hashMap.get(i,0) + 1
            if hashMap[i] > 1:
                return i