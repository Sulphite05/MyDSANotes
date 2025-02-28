# https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums) -> int:
        l = 0
        h = len(nums) - 1

        while l <= h:
            m = (l + h) // 2
            if 0 < m < len(nums) - 1:
                if nums[m - 1] < nums[m] and nums[m + 1] < nums[m]:
                    return m
                elif nums[m - 1] > nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            else:
                if m == 0 and l < h:
                    if nums[h] > nums[m]: m = h
                return m

# peak will always be there, in favour of the side having the greater element
