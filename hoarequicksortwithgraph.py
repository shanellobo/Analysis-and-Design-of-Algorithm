import random
import time
import matplotlib.pyplot as plt

# Hoare Partition-based Quick Sort
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

# Performance analysis
n_list = [5000, 6000, 7000, 8000, 9000, 10000]
sort_time = []

for n in n_list:
    l = [random.randint(1, 100) for _ in range(n)]
    s_t = time.time()
    quick_sort(l, 0, len(l) - 1)
    e_t = time.time()
    sort_time.append(e_t - s_t)

print("Input sizes:", n_list)
print("Sorting times:", sort_time)

# Plotting the time complexity
plt.plot(n_list, sort_time, marker='x')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Quick Sort (hoare Partition): Time Complexity Analysis")
plt.grid(True)
plt.show()
