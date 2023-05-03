def insertionSort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if j!=0:
                if arr[j] < arr[j-1]:
                    print(f"Swapping {arr[j]} and {arr[j-1]}")
                    arr[j],arr[j-1]=arr[j-1],arr[j]
                    print(arr)
    return arr

arr = [5,4,8,3,1,0,9,7,2,6]
print(f"Final Array:{insertionSort(arr)}")