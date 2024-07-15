from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        maxLeft = height[0]
        maxRight = height[-1]
        leftPointer, rightPointer = 0, len(height)-1
        store = 0
        while leftPointer < rightPointer:
            maxValue = max(maxLeft, maxRight)
            if maxValue == maxLeft:
                calc = maxRight-height[rightPointer]
                if calc > 0:
                    store += calc
                rightPointer -= 1
                if maxRight < height[rightPointer]:
                    maxRight = height[rightPointer]
            else:
                calc = maxLeft-height[leftPointer]
                if calc > 0:
                    store += calc
                leftPointer += 1
                if maxLeft < height[leftPointer]:
                    maxLeft = height[leftPointer]
        return store
        
sol = Solution()
print(sol.trap([4,2,0,3,2,5]))