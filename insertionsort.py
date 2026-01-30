import random
l = []

for i in range(10):
    l.append(random.randint(1, 100)) 
print("Original list:", l)

for i in range(1, len(l)):
    key = l[i]
    j = i - 1
    while j >= 0 and l[j] > key:
        l[j + 1] = l[j]
        j = j - 1
    l[j + 1] = key

print("Sorted list:", l)