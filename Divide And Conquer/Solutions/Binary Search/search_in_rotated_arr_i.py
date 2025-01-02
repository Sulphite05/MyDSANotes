# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums, target) -> int:
        l = 0
        h = len(nums) - 1

        # First binary search to get the pivot
        while l <= h:
            m = (l + h) // 2
            if nums[l] > nums[m]:
                h = m

            elif nums[h] < nums[m]:
                l = m + 1
            else:
                break

        # We do h = m instead of m-1 because m can be the pivot.
        # Pivot is where the elements start becoming sorted.
        # The least element represents the pivot. So if it's small
        # as per line 11 then mth element can be the pivot.

        low = 0
        high = len(nums) - 1

        if nums[l] == target:
            return l

        elif nums[l] < target <= nums[high]:
            low = l

        elif nums[low] <= target <= nums[l - 1]:
            high = l - 1

        # Second binary search to get the index
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1

            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1
