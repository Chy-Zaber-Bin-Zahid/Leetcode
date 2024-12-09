from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = 0
        for i in range(m, m+n):
            if nums1[i] == 0:
                nums1[i] = nums2[j]
                j+=1
        j = 0
        while j < len(nums1)-1:
            if nums1[j] > nums1[j+1]:
                temp = nums1[j]
                nums1[j] = nums1[j+1]
                nums1[j+1] = temp
                j = 0
            else:
                j+=1
        return nums1




sol = Solution()
print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))