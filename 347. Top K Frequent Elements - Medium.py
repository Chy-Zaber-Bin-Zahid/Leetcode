from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        output = []
        for i in nums:
            hashMap[i] = hashMap.get(i, 0) + 1
        sorted_items = list(dict(sorted(hashMap.items(), key=lambda item: item[1], reverse=True)).keys())
        for j in range(k):
            output.append(sorted_items[j])
        return output
    
sol = Solution()
print(sol.topKFrequent([4,1,-1,2,-1,2,3], 2))