#pattern 2
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
n = int(input("enter number of rows: "))
for i in range(n , 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()