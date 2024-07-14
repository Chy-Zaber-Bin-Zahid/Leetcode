from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lastIdx = len(numbers) - 1
        firstIdx = 0
        for _ in numbers:
            if numbers[firstIdx]+numbers[lastIdx] == target:
                return [firstIdx+1, lastIdx+1]
            elif numbers[firstIdx]+numbers[lastIdx] > target:
                lastIdx-=1
            else:
                firstIdx+=1

sol = Solution()
print(sol.twoSum([0,0,3,4], 0))