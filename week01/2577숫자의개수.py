num_list = [0 for _ in range(10)]
a = int(input())
b = int(input())
c = int(input())
result = str(a * b * c)
for i in range(len(result)):
    num_list[int(result[i])] += 1
for i in range(len(num_list)):
    print(num_list[i])