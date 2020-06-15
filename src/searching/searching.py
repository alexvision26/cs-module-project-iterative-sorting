def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return arr.index(target)
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    first = 0 #initialize beginning of array index
    last = (len(arr) - 1) #initialzie end of array index

    while first <= last: #loop through the array as long as the last iteration index is larger than or is 0
        middle = (first + last) //2 # intialize and update the current middle based on current length of first and last

        if arr[middle] == target: #returns target value
            return arr.index(target)

        else:
            if target < arr[middle]: #if target is less than the middle element, it will omit the second half (larger values), leaving less elements to iterate
                last = middle - 1
            else:
                first = middle + 1 # the inverse, if the target is larger than the middle element, omit the first half (smaller ones)

    return -1  # not found
