# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # pre-allocating for our master array (the array to return)
    elements = len(arrA) + len(arrB)
    master = [None] * elements
    # creating our initial indexes
    a_index = 0
    b_index = 0
    master_index = 0

    # loop to use when in progress of both arrA and arrB
    while(a_index < len(arrA) and b_index < len(arrB)):

        if(arrA[a_index] < arrB[b_index]):
            master[master_index] = arrA[a_index]
            master_index += 1
            a_index += 1
        else:
            master[master_index] = arrB[b_index]
            master_index += 1
            b_index += 1

    # loop to use while in progress of only arrA 
    while(a_index < len(arrA)):
        master[master_index] = arrA[a_index]
        master_index += 1
        a_index += 1

    # loop to use while in progress of only arrB
    while(b_index < len(arrB)):
        master[master_index] = arrB[b_index]
        master_index += 1
        b_index += 1

    return master


arrA = [4, 5, 6, 7]

arrB = [1, 8, 9]
# print(merge(arrA, arrB))
arrC = [2, 1, 6, 3]
# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # if our array is one item we end recursion and return it to parent function
    if(len(arr) <= 1):
        return arr

    # otherwise 
    # we split the array in half
    arr1 = arr[len(arr)//2:]
    arr2 = arr[:len(arr)//2]
    # recurse on the now two arrays
    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)
    # call helper function to return the product once arr1 and arr2 are returned
    return merge(arr1, arr2)


print(merge_sort(arrC))
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO
    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
