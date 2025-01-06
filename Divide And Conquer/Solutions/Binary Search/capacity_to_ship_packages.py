# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights, days: int) -> int:
        def feasible(maxi):
            summ = 0
            day = 1
            for weight in weights:
                summ += weight
                if summ > maxi:
                    summ = weight
                    day += 1
                if day > days or weight > maxi: return False
            return day <= days

        en = sum(weights)
        st = en // days
        while st < en:
            mid = (st + en) // 2
            if feasible(mid): en = mid
            else: st = mid + 1
        return st
