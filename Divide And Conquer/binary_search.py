# Before applying binary search, make sure the given list is sorted

# iterative method
def binary_search1(lst: list, val: int):
    low = 0
    high = len(lst) - 1

    while low < high:
        mid = low + (high-low)//2
        if val < lst[mid]:
            high = mid
        elif val > lst[mid]:
            low = mid + 1
        else:
            return mid
    return low


# recursive method
def binary_search2(lst: list, val: int):
    def dfs(low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if val < lst[mid]:
            high = mid - 1
        elif val > lst[mid]:
            low = mid + 1
        else:
            return mid
        return dfs(low, high)

    return dfs(0, len(lst)-1)

