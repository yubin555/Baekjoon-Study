a = int(input())
for i in range(a):
    R, S = input().split()
    result = ''
    for w in S:
        result += w * int(R)
    print(result)