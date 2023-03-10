import sys

input = sys.stdin.readline

n, k = map(int, input().split())

levels = [int(input()) for _ in range(n)]

def find_maximum_level(start, end, target):

    max_level = 0
    while start <= end:
        mid = (start + end) // 2

        need_level = 0
        for level in levels:
            if level < mid:
                need_level += (mid - level)
        
        if need_level == target:
            return mid
        elif need_level < target:
            start = mid+1
            max_level = max(max_level, mid)
        elif need_level > target:
            end = mid-1
        
    return max_level

print(find_maximum_level(1, int(1e9)+2, k))