def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)

def partition(arr, left, right):
    l = left
    r = right - 1
    pivot = arr[right]

    while l < r:
        while l < right and arr[l] < pivot:
            l += 1
        while r > left and arr[r] >= pivot:
            r -= 1
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
    if arr[l] > pivot:
        arr[l], arr[right] = arr[right], arr[l]
    return l

arr = [22, 11, 88, 66, 55, 77, 33, 44]

quicksort(arr, 0, len(arr) - 1)
print(arr)