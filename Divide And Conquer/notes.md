# Notes on Divide and Conquer Approach
## Applications
- Binary Search
- Find min/max problems
- Merge sort
- Quick sort
- Strassen's matrix multiplication

---

## Steps

- DAC(P)
   1. if small(P)
      1. Solve(P)
   2. else
      1. Divide P into P1, P2, P3...
      2. Apply DAC(P1), DAC(P2), DAC(P3)...
      3. Combine (DAC(P1), DAC(P2), DAC(P3)...)

---

## Optimization Techniques

### Collapsing Find
- Reduces the time complexity for finding the parent to nearly constant time O(4)
- Achieved through the **inverse Ackermann function**.

### Union by Rank vs. Union by Size
- **Union by Rank**:
  - Ranks parents by the depth of their deepest child.
  - Becomes less intuitive after path compression as ranks do not change.
- **Union by Size**:
  - Ranks parents by the number of children.
  - Preferred method due to better consistency with path compression.

# Resources for Disjoint Set Union (DSU)

## 1. TakeUForward (TUF)
- [Disjoint Set (Union by Rank, Union by Size, Path Compression)](https://takeuforward.org/data-structure/disjoint-set-union-by-rank-union-by-size-path-compression-g-46/)  
- A detailed article explaining the concepts of DSU with:
  - Union by Rank
  - Union by Size
  - Path Compression
  - Examples and code snippets.

## 2. Abdul Bari (YouTube)
- [Disjoint Set Data Structure](https://youtu.be/wU6udHRIkcc?si=D7JSlRKqhCM3a7pc)  
- A comprehensive video tutorial covering the basics and implementation of DSU.
- Great for visual learners and beginners.

# Practice Questions
- [GFG: Minimum Spanning Tree](https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1)
- [LC: Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)
- [LC: Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/)
- [LC: Accounts Merge](https://leetcode.com/problems/accounts-merge/description/)
- [LC: Making A Large Island](https://leetcode.com/problems/making-a-large-island/description/)
- [GFG: Number Of Islands](https://www.geeksforgeeks.org/problems/number-of-islands/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=number-of-islands)