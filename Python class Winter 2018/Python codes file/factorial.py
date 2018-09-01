userInput = int(input("Please enter a number"))

fact = 1

for x in range(1,userInput+1):
    fact = fact *x
print("Factorial =",fact)
