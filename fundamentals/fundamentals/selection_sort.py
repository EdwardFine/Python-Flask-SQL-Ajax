def selectionSort(arr):
    for i in range(len(arr)):
        smallest=arr[i]
        smallestIndex = i
        for j in range(i,len(arr)):
            if arr[j]<smallest:
                print(f"New smallest is {arr[j]}")
                smallest = arr[j]
                smallestIndex = j
        if smallest == arr[i]:
            print(f"{smallest} in correct position.")
        else:
            print(f"Swapping {arr[i]} and {smallest}")
            arr[i],arr[smallestIndex] = arr[smallestIndex],arr[i]
        print(f"New Array: {arr}")
    return arr



arr = [5,4,8,3,1,0,9,7,2,6]
print(f"Final Array: {selectionSort(arr)}")