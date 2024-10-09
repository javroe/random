def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        l = 0 # left_arr idx
        r = 0 # right_arr idx
        m = 0 # merged array idx

        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] < right_arr[r]:
                arr[m] = left_arr[l]
                l += 1
            else:
                arr[m] = right_arr[r]
                r += 1
            m += 1

        while l < len(left_arr):
            arr[m] = left_arr[l]
            l += 1
            m += 1
        
        while r < len(right_arr):
            arr[m] = right_arr[r]
            r += 1
            m += 1







arr_test = [2, 3, 5, 1, 4, 9, 7, 1, 3, 4, 1, 9, 2, 3, 4, 5, 1, 2, 3, 1, 2]

merge_sort(arr_test)

print(arr_test)