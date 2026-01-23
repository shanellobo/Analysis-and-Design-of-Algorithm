n = int(input("Enter the number of elements: "))
l = []

for i in range(n):
    l.append(int(input(f"Enter elements {i+1}: ")))

for i in range(len(l)):
    for j in range(0, len(l) - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

print("Sorted list:", l)