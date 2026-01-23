n = int(input("Enter the number of elements: "))
l = []

for i in range(n):
    l.append(int(input(f"Enter elements {i+1}:")))

for i in range(len(l)):
    min_index = i
    for j in range(i + 1, len(l)):
        if l[j] < l[min_index]:
            min_index = j
    l[i], l[min_index] = l[min_index], l[i]

print("Sorted list:", l)