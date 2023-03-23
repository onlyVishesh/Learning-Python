n = 5  # int(input())
for i in range(n):
    for j in range(n-i):
        print(n, end=" ")
        for k in range(n-j):
            print(j, end=" ")
        print(n, end=" ")
        print()
