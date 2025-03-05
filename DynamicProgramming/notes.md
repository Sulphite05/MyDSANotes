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

Recursive -> Memoization -> Tabulation(Bottom-up) DP(Using matrices)

## Variations of DP
- Knapsack
- Fibonacci
- Longest Common Subsequence
- Longest Increasing Subsequence
- Kadane's Algorithm
- Matrix Chain Multiplication
- DP on trees
- DP on grid
- Others

### 1. `Knapsack Problem`

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

###### i. 0/1 Knapsack Problem
For recursive solution:

- Think of the smallest valid input for base case
- In case of knapsack, the smallest input is no input. Weight of sack = 0 or n = 0 so we return 0.
- Otherwise there are two cases
  1. Either the current weight is less than equal to the available capacity of the bag(return max of using current weight and not using the current weight)
  2. Or it is greater(Leave the current weight and move to the next)

For memoization:
- We can create a  matrix or simply use a dictionary in recursive solution.
- For the matrix, we need to decide the value of i, j
- We create the matrix for values that change in your recursive solution
- We use the highest dimensions that can accommodate all the changing values
- Initialise with -1
- For every recursive call, I check if there is a value present otherwise I store the result
- The bad thing about this code is the increase in stack size

For Bottom-Up DP(Base case to complete input):
- Initialise a matrix of size w*n(capacity of knapsack * Total items)
- The base condition of recursion becomes the matrix initialisation here
- i.e. The first row and column will be initialised with 0(What we wanted to return in base condition)
- The other slots ae sub-problems
- dp[w][n] is the final result
- In recursive solution, we start from w and n but here we start from base condition then move forward(Bottom-up).
- We simply translate the recursive calls to indexing the DP matrix as all the calls are pre-computed as we move forward.

###### i. Unbounded Knapsack Problem
- Multiple occurrences of the same item is allowed unlike 0/1 where an item could be included only once.
- instead of calling n-1(moving to next element after adding current element), I can call n again but after adding value of current n.
- That's it! :)
- e.g. see rodCutting.py
