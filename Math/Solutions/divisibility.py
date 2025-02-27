# Count Substrings Divisible By Last Digit
# https://leetcode.com/contest/weekly-contest-436/problems/count-substrings-divisible-by-last-digit/description/
# Kept me awake for days

from collections import defaultdict


class Solution:
    def countSubstrings(self, s: str) -> int:
        # 1 is divisible by all
        # 2 is divisible by all
        # 3 is divisible if not(sum of digits%3)
        # 4 is divisible if not(last 2 digits)%4
        # 5 is divisible by all
        # 6 is divisible if 3 is satisfied
        # 7 is divisible if not(num - (last digit*2))%7
        # 8 is divisible if not(last 3 digits)%4
        # 9 is divisible if not(sum of digits%9)

        d_3 = defaultdict(int)
        d_9 = defaultdict(int)

        d_3[0] = 1
        d_9[0] = 1

        summ = 0
        ans = 0

        for i, num in enumerate(s):

            num = int(num)
            summ += num

            if num in (1, 2, 5):
                ans += (i + 1)

            elif num in (3, 6):
                ans += d_3[summ % 3]

            elif num == 4:

                if i > 0 and not (int(s[i - 1:i + 1]) % 4):
                    ans += i
                ans += 1

            elif num == 8:
                if i > 0 and not (int(s[i - 1:i + 1]) % 8):
                    ans += 1
                if i > 1 and not (int(s[i - 2:i + 1]) % 8):
                    ans += (i - 1)
                ans += 1

            elif num == 9:
                ans += d_9[summ % 9]

            d_3[summ % 3] += 1
            d_9[summ % 9] += 1

        d_7 = defaultdict(int)
        curr = 0
        n = len(s)

        for i in range(n - 1, -1, -1):
            if s[i] == '7':
                d_7[curr % 7] += 1

            digit = n - i
            get = pow(10, digit, 7)
            get *= int(s[i]) % 7
            curr = (curr + get) % 7
            ans += d_7[curr]

        return ans

