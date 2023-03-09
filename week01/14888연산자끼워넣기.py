from itertools import permutations

def operate(a, b, op):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    elif op == 3:
        if a < 0:
            return -(-a//b)
        return a // b

n = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))
num_operator = []
for i in range(4):
    for j in range(operator[i]):
        num_operator.append(i)
ope = list(permutations(num_operator))
d_op = set()
for i in range(len(ope)):
    d_op.add(ope[i])
min = 0
max = 0
f = 0
for i in d_op:
    result = num[0]
    for j in range(n-1):
        result = operate(result, num[j+1], i[j])
    if f == 0:
        min = result
        max = result
        f += 1
    else:
        if min > result:
            min = result
        if max < result:
            max = result
print(max)
print(min)