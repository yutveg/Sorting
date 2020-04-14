# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if(arr[j] < arr[i]):
                current_val = arr[i]
                arr[i] = arr[j]
                arr[j] = current_val
        # TO-DO: swap

    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    unsorted = True

    while unsorted == True:
        swapped = False
        for i in range(1, len(arr)):
            if(arr[i] < arr[i - 1]):
                swapped = True
                cur_val = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = cur_val

        if(swapped == False):
            unsorted = False
        else:
            pass
    return arr


print(bubble_sort([1, 9, 3, 4, 7, 8, 2, 13, 29, 12, 5]))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
