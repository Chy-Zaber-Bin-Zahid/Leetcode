from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftPointer, rightPointer = 0, len(height)-1
        answer = 0
        while leftPointer < rightPointer:
            left, right = height[leftPointer], height[rightPointer]
            if left >  right:
                area = right*(rightPointer-leftPointer)
                if answer < area:
                    answer = area
                rightPointer-=1 
            else:
                area = left*(rightPointer-leftPointer)
                if answer < area:
                    answer = area
                leftPointer+=1
        return answer


sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))