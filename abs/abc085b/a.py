n = int(input())

a = [0 for _ in range(n)]

for i in range(n):
    a[i] = int(input())
    
print(len(list(set(a))))


