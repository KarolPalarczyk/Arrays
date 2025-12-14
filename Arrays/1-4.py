###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4,3]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
middle = int(len(arr)/2)
print('Sum of firts and last value', (arr[1]+arr[-1]))
print('middle value', arr[middle])
all =""
for i in arr:
    print(i, end=" ")
