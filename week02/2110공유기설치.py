import sys

input = sys.stdin.readline

n, c = map(int, input().split())

house = [int(input()) for _ in range(n)]
house.sort()

def find_maximum_dist(start, end, cnt):
    max_distance = 0
    while start <= end:
        mid = (start + end) // 2
        tmp_cnt = 1
        last_position = house[0]
        idx = 1
        while tmp_cnt < cnt and idx < n:
            if house[idx] - last_position >= mid:
                tmp_cnt += 1
                last_position = house[idx]
            else:
                idx += 1
        
        if tmp_cnt == cnt and idx < n:
            max_distance = max(max_distance, mid)
            start = mid+1
        elif tmp_cnt < cnt and idx == n:
            end = mid-1
                
    return max_distance

print(find_maximum_dist(1, 1000000000, c))