#(Question:3)
print ("Welcome To Summer Camp")
print("Log in problem for  the Summer Camp 2018")

#Creating a password for the User
#--------------------------------------------

str_input=input("Please Create your own Password :")   # user input assigning into str_input
hashed_integer=hash(str_input) # hash function converting user input(password) to a integer number 

_KEY=(hashed_integer%541) # making a key or small number 

print ("Hashed Number:",hashed_integer)
print("Password you Created ",_KEY)


count=0   # variable that is counting the user chance to enter a correct password


# Check your password to get a hidden message // maximum 3 chance to enter correct password
#--------------------------------------------------

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




