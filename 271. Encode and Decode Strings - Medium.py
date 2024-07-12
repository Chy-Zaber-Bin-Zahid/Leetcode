from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return strs
        new = ""
        for i in strs:
           new+= str(len(strs)) + "#" + i
        return new
    def decode(self, s: str) -> List[str]:
        if s == []:
            return s
        store = s.split(s[0:s.index("#")+1])
        return store[1::]