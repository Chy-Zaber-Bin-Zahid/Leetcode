class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.replace(" ","").lower()
        # if s == "":
        #     return True
        # for i in s:
        #     if (ord(i) < 97 or ord(i) > 122) and (ord(i) < 48 or ord(i) > 57):
        #         s = s.replace(i,"")
        # startIdx = 0
        # endIdx = len(s)-1
        # for _ in s:
        #     if startIdx == endIdx or startIdx > endIdx:
        #         break
        #     if s[startIdx] == s[endIdx]:
        #         startIdx+=1
        #         endIdx-=1
        #     else:
        #         return False
        # return True 

        #less time complexity
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))


sol = Solution()
print(sol.isPalindrome("0f"))