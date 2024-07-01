from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
f = open('user.out', 'w')
for strs in map(loads, stdin):
    w = defaultdict(list)
    for s in strs:
        w[''.join(sorted(s))].append(s)
    print(str(w.values())[12:-1].replace("'", '"').replace(" ", ""), file=f)
exit()

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))