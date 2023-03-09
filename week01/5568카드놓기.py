from itertools import permutations 

n = int(input())
k = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
    
candidates = permutations(range(n), k)

res = set()
for candidate in candidates:
    tmp_num = ""
    for idx in candidate:
        tmp_num += str(nums[idx])
    res.add(tmp_num)

print(len(res))