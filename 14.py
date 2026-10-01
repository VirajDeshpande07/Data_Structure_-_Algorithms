#print the following pattern
#         A
#      A     C
#    A         E
#  A  B  C D E F G
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        if j == 0:
            print("A", end="")
        elif j == 2*i:
            print(chr(65 + 2*i), end="")
        else:
            print(" ", end="")
    print()