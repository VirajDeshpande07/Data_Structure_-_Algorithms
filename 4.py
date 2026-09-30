# find smallest, second smallest, largest and second largest number in a list
arr = [10,8,6,4,22,29,15,19,27]

max = min = arr[0]
smin = smax = arr[0]
for num in arr:
    if num>max:
        smax = max
        max=num
    elif (max>smax and num!=max):
        smax=num
    if num<min:
        smin=min
        min=num
    elif (num<min and num!=min ):
        smin=num
print("Smallest number is : ",min)
print("Second smallest number is: ",smin)
print("Largest number is : ",max)
print("Second Largest number is : ",smax)


