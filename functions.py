def countdown(num):
    arr=[]
    for i in range(num,-1,-1):
        arr.append([i])
    return arr
#print(countdown(5))

def recursive_countdown(num, arr=[]):
    if num>=0:
        arr.append(num)
        if num==0:
            return arr
        else:
            return recursive_countdown(num-1,arr)
#print(recursive_countdown(7))

def print_and_return(arr):
    print(arr[0])
    return arr[1]
#print(print_and_return([1,2]))

def first_plus_length(arr):
    return int(arr[0])+len(arr)
#print(first_plus_length(["1",1,2,3,4,5,7]))

def values_greater_than_second(arr):
    if len(arr)<2:
        return False
    arr2=[i for i in arr if i>arr[1]]
    print(len(arr2))
    return arr2
#print(values_greater_than_second([1,2,5,2,3,-4]))

def this_length_that_value(len,val):
    #return [val for _ in range(len)]
    return [val]*len
print(this_length_that_value(5,2))