n = 5
sps = 5
for i in range(1, n+1):
    for s in range(0, sps):
        print(end=" ")
    for j in range(i, i+1):
        print(j, end=" ")
    if(i!=1):
        print("1")
    print()