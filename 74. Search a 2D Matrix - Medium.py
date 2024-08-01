from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        spread = []
        for i in matrix:
            spread += i
        l, r = 0, len(spread)-1
        while r >= l:
            m = (l+r) // 2
            if spread[m] > target:
                r = m-1
            elif spread[m] < target:
                l = m+1
            else:
                return True
        return False 

sol = Solution()
print(sol.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]],15))