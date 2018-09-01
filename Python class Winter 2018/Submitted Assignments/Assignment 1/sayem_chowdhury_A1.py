#Assignment 1
#Name: Sayem Chowdhury
#----------------------
#(Question:1)
#---------------------
#Significant constants Variables
print("Problem (1)")
TAX_RATE=0.10             #Dont Change this variable through the program
STD_DEDUCTION=6000        #Dont Change this variable through the program
DD_PER_DEPENDENT=1500     #Dont Change this variable through the program

#User input Variables
#---------------------
gross_income=float(input("Please Enter the Gross Income: "))
num_of_dependents=int(input("Please Enter the number of dependents: "))

#Calculations
#------------------
#taxable income = (gross income) - (the standard deduction) - (a deduction for each dependent)
#income tax = (is) a fixed percentage of the taxable income

taxable_income=(gross_income)-(STD_DEDUCTION)-(DD_PER_DEPENDENT*num_of_dependents)

if (taxable_income<0):
    print("No Taxable Income is Eligible for the Client ")
elif(taxable_income>0):
    income_tax = (TAX_RATE)*(taxable_income)
    print("Taxable Income = ",taxable_income)
    print("Income TAX = ", income_tax)
    
print("\n")
#--------------------------------------------------------
#(Question:2)
print("Problem (2)")
#input variables
num1=float(input("Please Enter the first number :"))
num2=float(input("Please Enter the second number :"))

product=(num1*num2)
largest_number=max(num1,num2)

print("Product of the two number is:", product)
print("The Largest Number is:",largest_number)

print("\n")

#--------------------------------------------------

#(Question:3)
print("problem 3")

str_input=input("Please Create your own Password :")
hashed_integer=hash(str_input)
_KEY=(hashed_integer%541)
print ("Hashed Number:",hashed_integer)
print("Password you Created ",_KEY)

count=0
while count<3:
    password=input("Please Enter the Password:")
    hashed_User_password=hash(password)
    user_KEY=(hashed_User_password%541)
    print ("Password Entered",user_KEY)
    if (user_KEY==_KEY):
        print("Correct Password Entered")
        print("""Secret message is:
                you are really awesome 

                                 Thank you!""")
        break;
    count=count+1
    if (count==1):
        print("You have left 2 more chance")
    elif (count==2):
        print("This is your last Chance")

#---------------------------------------------------


        
        



    






