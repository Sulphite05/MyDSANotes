n = int(input())
lst = list(map(int, input().split()))
print(n*(n+1)//2 - sum(lst))
