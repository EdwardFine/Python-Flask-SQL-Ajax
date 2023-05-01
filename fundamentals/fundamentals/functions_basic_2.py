def countdown(start):
    countdown = []
    for i in range(start,-1,-1):
        countdown.append(i)
    return countdown

print(countdown(5))

def print_and_return(arr):
    print(arr[0])
    return arr[1]

print(print_and_return([1,2]))

def first_plus_length(arr):
    return arr[0]+len(arr)

print(first_plus_length([1,2,3,4,5]))

def value_greater_than_second(arr):
    greaterArr=[]
    if len(arr)<2:
        return False
    for i in arr:
        if i > arr[1]:
            greaterArr.append(i)
    print(len(greaterArr))
    return greaterArr

print(value_greater_than_second([5,2,3,2,1,4]))

def this_length_that_value(size,value):
    arr = []
    for i in range(size):
        arr.append(value)
    return arr

print(this_length_that_value(4,7))
print(this_length_that_value(6,2))