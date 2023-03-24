import sys
input = sys.stdin.readline

equation = input().rstrip()

nums = []
operator = [0]

point = 0
for i in range(len(equation)):
    if equation[i] == '-' or equation[i] == '+':
        operator.append(equation[i])
        nums.append(int(equation[point:i]))
        point = i+1
nums.append(int(equation[point:]))
result = nums[0] 
tmp = 0
is_minus = False
for i in range(1, len(nums)):
    if operator[i] == '+':
        if is_minus:
            tmp += nums[i]
        else:
            result += nums[i]
            is_minus = False
    elif operator[i] == '-':
        if is_minus:
            result -= tmp
        tmp = nums[i]
        is_minus = True
        
result -= tmp

print(result)