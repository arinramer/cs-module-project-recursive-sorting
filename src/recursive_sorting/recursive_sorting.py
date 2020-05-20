# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []
    # Your code here
    while (len(arrA) > 0) & (len(arrB) > 0):
        if arrA[0] <= arrB[0]:
            merged_arr.append(arrA[0])
            arrA = arrA[1:]
        else:
            merged_arr.append(arrB[0])
            arrB = arrB[1:]
    

    return merged_arr + arrA + arrB


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    length = len(arr)

    if length <= 1:
        return arr
    if length == 2:
        if arr[0] < arr[1]:
            return arr
        else:
            return [arr[1], arr[0]]
    mid_index = length//2
    arr1 = arr[:mid_index]
    arr2 = arr[mid_index:]
    sorted1 = merge_sort(arr1)
    sorted2 = merge_sort(arr2)
    return merge(sorted1, sorted2)


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1
    if arr[mid] <= arr[start2]:
        return

    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2

            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value

            start += 1
            mid += 1
            start2 += 1


def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r:
        m = l + (r - l) // 2
        merge_sort_in_place(arr,l,m)
        merge_sort_in_place(arr,m+1,r)
        merge_in_place(arr,l,m,r)
    return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
