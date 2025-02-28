# https://leetcode.com/problems/koko-eating-bananas/
from math import ceil


class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        low = sum(piles) // h
        high = max(piles)
        piles.sort(reverse=True)
        while low <= high:
            mid = (low + high) // 2
            c = 0
            if mid:
                for pile in piles:
                    c += ceil(pile / mid)
                    if c > h: break
                else:
                    high = mid - 1
                    continue
            low = mid + 1
        return low




