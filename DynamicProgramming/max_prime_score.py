from heapq import heappop, heappush
from math import sqrt
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        MOD = 10 ** 9 + 7
        scores = []
        heap = []
        n = len(nums)

        # STEP 2: Find score
        for i, num in enumerate(nums):
            heappush(heap, [-num, i])
            primes = set()
            while num > 1:
                p = sieve[num]
                primes.add(p)
                num //= p
            scores.append(len(primes))

        nxt = [n] * n
        prev = [-1] * n

        stack = []

        # STEP 3: Use monotonic stack to find pre and post array indices
        for i in range(n):
            while stack and scores[stack[-1]] < scores[i]:
                top = stack.pop()
                nxt[top] = i
            if stack:
                prev[i] = stack[-1]
            stack.append(i)

        # STEP 4: Find total sub arrs
        sub_arr = [0] * n
        for i in range(n):
            sub_arr[i] = (nxt[i] - i) * (i - prev[i])

        # STEP 5: Compute result
        ans = 1
        while k and heap:
            num, ind = heappop(heap)
            num = -num

            ops = min(sub_arr[ind], k)
            ans = (ans * pow(num, ops, MOD)) % MOD
            k -= ops

        return ans


# STEP 1: calculate sieve
sieve = [1, 1] + [-1] * 10 ** 5
n = len(sieve)
for i in range(2, int(sqrt(n))):
    if sieve[i] == -1:
        for j in range(i, n, i):
            if sieve[j] == -1: sieve[j] = i
