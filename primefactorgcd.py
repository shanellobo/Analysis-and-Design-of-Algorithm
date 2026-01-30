def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input("Enter a number: "))
i = 2
last_gcd = 1
print("Prime factors of",n, "are:", end=" ")
while n > 1:
    if gcd(n, i) == i:
        print(i ,end=" ")
        last_gcd = i
        n = n // i
    else:
        i += 1
        
print("\nGCD used in factorization:", last_gcd)