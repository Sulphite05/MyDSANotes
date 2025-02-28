# https://www.geeksforgeeks.org/problems/square-root/0

class Solution:
    def floorSqrt(self, n):
        st, en = 0, n
        while st <= en:
            mid = (st+en)//2
            curr = mid*mid
            if curr == n:
                return mid
            elif curr < n:
                st = mid + 1
            else:
                en = mid - 1
        return en