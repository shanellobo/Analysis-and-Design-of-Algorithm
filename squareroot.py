num = float(input("Enter a number: "))
guess = num / 2 

for i in range(10):
    guess = (guess + num / guess) / 2
    print("guesses" , guess)

print("Square root of",num,"is:", guess)