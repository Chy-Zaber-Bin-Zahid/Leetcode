from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        hashMap = {}
        for s in strs:
            key = tuple(sorted(s))
            if key in hashMap:
                hashMap[key].append(s)
            else:
                hashMap[key] = [s]
        return list(hashMap.values())

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))