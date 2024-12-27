# https://leetcode.com/problems/accounts-merge/description/

from collections import defaultdict
from typing import List
from DSU.disjoint_set_union import DSU


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d = defaultdict(list)
        final = []
        for row in accounts:
            d[row[0]].append(row[1:])

        for key in d:
            if len(d[key]) > 1:
                child = defaultdict(lambda: [0, 0])  # par, ind
                rev = dict()
                num = 0
                for i, acc in enumerate(d[key]):
                    for a in acc:
                        if a not in child:
                            child[a][0] = num
                            rev[num] = a
                            num += 1
                            child[a][1] = i

                l = len(child)
                dsu = DSU(l)
                for acc in d[key]:
                    prev = acc[0]
                    for curr in acc[1:]:
                        dsu.union(child[prev][0], child[curr][0])
                        prev = curr

                ans = defaultdict(set)
                for acc in d[key]:
                    for a in acc:
                        p = dsu.find(child[a][0])
                        ans[p].add(a)

                for k in ans:
                    final.append([key] + (sorted(list(ans[k]))))
            else:
                final.append([key] + (sorted(list(set(d[key][0])))))
        return final
