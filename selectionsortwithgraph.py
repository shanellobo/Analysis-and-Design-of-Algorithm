import random
import time
import matplotlib.pyplot as plt

def selectionsort(l):
    n=len(l)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if(l[j]<l[min]):
                min=j
            l[min],l[i]=l[i],l[min]
            
n_list = [5000, 6000, 7000, 8000, 9000, 10000]
sort_time = []

for n in n_list:
    l = [random.randint(1, 100) for _ in range(n)]
    s_t = time.time()
    selectionsort(l)
    e_t = time.time()

    sort_time.append(e_t - s_t)

print("Input sizes:", n_list)
print("Sorting times:", sort_time)


#plotting the graph
plt.plot(n_list,sort_time, marker='x')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("selection sort: Time Complexity Analysis")
plt.grid(True)
#save the plot
# plt.savefig("selection_sort_time_complexity.png", dpi=300, bbox_inches='tight')
plt.show()