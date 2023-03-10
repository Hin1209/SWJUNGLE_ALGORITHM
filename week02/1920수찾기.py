import sys

input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

m = int(input())
check_list = list(map(int, input().split()))

num_list.sort()

def find_num(start, end, target):
    
    while start <= end:
        mid = (start + end) // 2
        if num_list[mid] == target:
            return True
        elif num_list[mid] > target:
            end = mid-1
        elif num_list[mid] < target:
            start = mid+1
        
    return False

for num in check_list:
    if find_num(0, n-1, num):
        print(1)
    else:
        print(0)