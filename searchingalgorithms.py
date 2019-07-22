# For worst case use this # [780, 12, 19, 17,  250, 19, 30, 25, 40, 1009, 320, 1009]


# Linear Search


def linearsearch(arr, key):
    for i in range(len(arr)):

        if key == arr[i]:
            return i+1

    return False


print("--> Linear Search :")
selectionelements = [12, 19, 17, 19, 30, 25, 40]
print(selectionelements)
el = linearsearch(selectionelements, 30)
if el:
    print("Element found at position : ", el)


# Binary Search
# def binarySearch(arr, l, r, x):

#     # Check base case
#     if r >= l:

#         mid = l + (r - l)//2

#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid

#         # If element is smaller than mid, then it
#         # can only be present in left subarray
#         elif arr[mid] > x:
#             return binarySearch(arr, l, mid-1, x)

#         # Else the element can only be present
#         # in right subarray
#         else:
#             return binarySearch(arr, mid + 1, r, x)

#     else:
#         # Element is not present in the array
#         return -1

def binarysearch(arr, key, low, high):
    if high >= low:
        mid = low+(high-low)//2
        if key == arr[mid]:
            return mid

        elif key < arr[mid]:
            return binarysearch(arr, key, low, mid-1)
        else:
            return binarysearch(arr, key, mid+1, high)
        #mid = l + (r - l)/2
    return False


print("--> Binary Search :")
selectionelements = [12, 17, 19, 19, 25, 30, 40]
n = len(selectionelements)-1
print(selectionelements)
bel = binarysearch(selectionelements, 39, 0, n)
if bel:
    print("Element found at position : ", bel)
