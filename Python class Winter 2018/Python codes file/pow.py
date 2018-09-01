# calculate pow(x,y)

x = int(input("please enter x"))
y = int(input("please enter y"))

result = 1 

for i in range(y):
    result *= x
print(result)