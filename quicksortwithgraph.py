import random
import time
import matplotlib.pyplot as plt

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot] 
    middle = [x for x in arr if x == pivot]  
    right = [x for x in arr if x > pivot]  
    return quick_sort(left) + middle + quick_sort(right)

n_list = [5000, 6000, 7000, 8000, 9000, 10000]
sort_time = []

for n in n_list:
    l = [random.randint(1, 100) for _ in range(n)]
    s_t = time.time()
    quick_sort(l)
    e_t = time.time()
    sort_time.append(e_t - s_t)

print("Input sizes:", n_list)
print("Sorting times:", sort_time)

plt.plot(n_list,sort_time, marker='x')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Quick Sort: Time Complexity Analysis")
plt.grid(True)
#plt.savefig("bubble_sort_time_complexity.png", dpi=300, bbox_inches='tight')
plt.show()