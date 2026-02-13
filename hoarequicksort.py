# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]  
#     left = [x for x in arr if x < pivot] 
#     middle = [x for x in arr if x == pivot]  
#     right = [x for x in arr if x > pivot]  
#     return quick_sort(left) + middle + quick_sort(right)

# arr = [10, 7, 8, 9, 1, 5]
# sorted_arr = quick_sort(arr)
# print("unsorted array: ", arr)
# print("Sorted array:", sorted_arr)

def quick_sort(arr, low, high):
    if low < high:
        pivot = arr[low]
        i, j = low - 1, high + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                p = j
                break
            arr[i], arr[j] = arr[j], arr[i]

        quick_sort(arr, low, p)
        quick_sort(arr, p + 1, high)

arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
