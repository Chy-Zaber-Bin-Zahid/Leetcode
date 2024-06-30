class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ### time complexity )=O(n^2) ###
        # if len(s) == len(t):
        #     for i in range(len(s)):
        #         if s[i] in t:
        #             if s.count(s[i]) != t.count(s[i]):
        #                 return False 
        #         else:
        #             return False
        #     return True
        # else:
        #     return False
        
        ### time complexity O(n) ###
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}        
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        return count_s == count_t
  
sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))