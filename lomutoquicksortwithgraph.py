import random
import time
import matplotlib.pyplot as plt

# Lomuto Partition-based Quick Sort
def lomuto_partition(arr, low, high):
    pivot = arr[high]  
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        p = lomuto_partition(arr, low, high)
        quick_sort(arr, low, p - 1)  
        quick_sort(arr, p + 1, high) 

n_list = [5000, 6000, 7000, 8000, 9000, 10000]
sort_time = []
for n in n_list:
    arr = [random.randint(1, 100) for _ in range(n)]
    start_time = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    sort_time.append(time.time() - start_time)
print("Input sizes:", n_list)
print("Sorting times:", sort_time)

plt.plot(n_list, sort_time, marker='x')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Quick Sort (Lomuto Partition): Time Complexity Analysis")
plt.grid(True)
plt.show()
