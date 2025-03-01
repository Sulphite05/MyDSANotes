> _Those who can't remember the past are condemned to repeat it._
# Dynamic Programming ft Aditya Verma
DP is enhanced recursion. Period.

## How to identify DP?
Since DP is like recursion, the identification is also the same.

- You are given a choice at every step to proceed further
- If such a problem is overlapping, then we use DP
- You're asked for optimal solution(maximum, minimum, highest, lowest, longest, shortest etc)
1. Choice
2. Optimality

Recursive -> Memoization -> Top down DP(Using matrices)

## Variations of DP
- 0/1 Knapsack
- Unbounded knapsack
- Fibonacci
- Longest Common Subsequence
- Longest Increasing Subsequence
- Kadane's Algorithm
- Matrix Chain Multiplication
- DP on trees
- DP on grid
- Others

### 1. `0/1 Knapsack Problem`

#### Problems
- Subset sum
- Equal sum partition
- Count of subset sum
- Minimum subset sum difference
- Target sum
- Number of subsets with given difference

#### Description
What is a knapsack? Any bag with a fixed weight. We want to maximise the value we keep in our bag.


Knapsack has 3 types. 
- Fractional knapsack which comes in greedy as you can add items in fractions as well
- 0/1 Knapsack means adding the whole item or not at all so this comes in DP(choice and optimality)
- Unbounded Knapsack means even after using the item once, it can be used again(unlimited supply of items)

For recursive solution:
- Think of the smallest valid input for base case
- In case of knapsack, the smallest input is no input. Weight of sack = 0 or n = 0 so we return 0.

