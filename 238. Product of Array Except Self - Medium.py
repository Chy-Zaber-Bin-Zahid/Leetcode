from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        product = 1
        for i in range(1,len(nums)):
            product *= nums[i-1]
            answer[i] = product
        product = 1
        for i in range(len(nums)-2, -1, -1):
            product *= nums[i+1]
            answer[i] = product*answer[i]
        return answer
                        
sol = Solution()
print(sol.productExceptSelf([-1,1,0,-3,3]))