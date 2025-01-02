# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums, target) -> int:
        l = pivot = 0
        h = len(nums) - 1

        while l <= h:
            m = (l + h) // 2
            if nums[l] > nums[m]:
                h = m

            elif nums[h] < nums[m]:
                l = m + 1

            elif nums[h] == nums[m]:
                if h > 0 and nums[h - 1] <= nums[h]:
                    h -= 1
                    # in worst case, we get O(n) complexity because
                    # it is not possible to determine which side to go to
                else:
                    pivot = h
                    break
            else:
                pivot = l
                break

        low = 0
        high = len(nums) - 1

        if nums[pivot] == target:
            return True

        elif nums[pivot] < target <= nums[high]:
            low = pivot

        elif nums[low] <= target <= nums[pivot - 1]:
            high = pivot - 1

        # Second binary search to get the index
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1

            elif nums[mid] > target:
                high = mid - 1
            else:
                return True
        return False
