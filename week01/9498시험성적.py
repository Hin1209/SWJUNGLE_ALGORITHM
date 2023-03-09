score = {10 : "A", 9 : "A", 8 : "B", 7 : "C", 6 : "D"}
n = int(input()) // 10
if n in score:
    print(score[n])
else:
    print("F")