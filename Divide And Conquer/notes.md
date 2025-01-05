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
# Binary Search

## When to use Binary Search?

- Array is sorted
- You need to find an optimal solution 
- Array problem requires division in half at every step

## Resources for Binary Search

### 1. TakeUForward (TUF)
- [Binary Search explained](https://takeuforward.org/data-structure/binary-search-explained/)  
- A detailed article explaining the concepts of binary search

### 2. Abdul Bari (YouTube)
- [Iterative Binary Search](https://youtu.be/C2apEw9pgtw?si=TsYxyG3druzepIws)  
- [Recursive Binary Search](https://youtu.be/uEUXGcc2VXM?si=tZoKSV2PuOACHIAJ) 

### 3. LeetCode Discuss
- [Zhijun Liao's post on BS variables](https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems)

## Practice Questions
- [LC: Find Peak Element](https://leetcode.com/problems/find-peak-element/)
- [LC: Search in rotated array i](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [LC: Search in rotated array ii](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)
- [GFG: Square root](https://www.geeksforgeeks.org/problems/square-root/0)
- [LC: Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
- [LC: Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)
