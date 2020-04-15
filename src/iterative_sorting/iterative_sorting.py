
# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if(arr[j] < arr[i]):
                arr[i], arr[j] = arr[j], arr[i]
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
                arr[i], arr[i - 1] = arr[i - 1], arr[i]

        if(swapped == False):
            unsorted = False
        else:
            pass
    return arr


# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
