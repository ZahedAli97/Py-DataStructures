# For worst case use this # [780, 12, 19, 17,  250, 19, 30, 25, 40, 1009, 320, 1009]


# Bubble Sort


def bubblesort(bubblesortedlist, lastunsorted):
    print(elements)
    while not bubblesortedlist:
        bubblesortedlist = True
        for i in range(lastunsorted):
            if elements[i] > elements[i+1]:
                elements[i], elements[i+1] = elements[i+1], elements[i]
                bubblesortedlist = False
        lastunsorted -= 1
    print(elements)


print("--> Bubble Sort :")
bubblesortedlist = False
elements = [12, 19, 17, 19, 30, 25, 40]
lastunsorted = len(elements)-1
bubblesort(bubblesortedlist, lastunsorted)


# Merge Sort


def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergesort(L)  # Sorting the first half
        mergesort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


print("--> Merge Sort :")
# mergesortedlist = False
mergeelements = [12, 19, 17, 19, 30, 25, 40]
print(mergeelements)
mergesort(mergeelements)
print(mergeelements)


# Insertion Sort


def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


print("--> Insertion Sort :")
# mergesortedlist = False
insertionlements = [12, 19, 17, 19, 30, 25, 40]
print(insertionlements)
insertionSort(insertionlements)
print(insertionlements)


# Quick Sort

# Pivot as arr[low]

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[low] = arr[low], arr[j]
    return j

# Pivot as arr[high]

# def partition(arr, low, high):
#     i = low-1
#     pivot = arr[high]
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i = i+1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return (i+1)


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)


print("--> Quick Sort :")
# mergesortedlist = False
quickelements = [12, 19, 17, 19, 30, 25, 40]
n = len(quickelements)-1
print(quickelements)
quicksort(quickelements, 0, n)
print(quickelements)


# Selection Sort

def selectionsort(arr):

    for i in range(len(arr)):
        mini = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[mini]:
                arr[j], arr[mini] = arr[mini], arr[j]

        #         mini = j
        # if mini != i:
        #     arr[i], arr[mini] = arr[mini], arr[i]


print("--> Selection Sort :")
selectionelements = [12, 19, 17, 19, 30, 25, 40]
print(selectionelements)
selectionsort(selectionelements)
print(selectionelements)
