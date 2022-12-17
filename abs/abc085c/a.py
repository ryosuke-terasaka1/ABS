n, y = map(int, input().split())

has_money = False

for i in range(n+1):
    for j in range(n+1-i):
        k = n-j-i
        if 10000*i + 5000*j + 1000*k == y:
            print(i, j, n-i-j)
            has_money = True
            break
    if has_money:
        break

if not has_money:
    print(-1, -1, -1)
