#Assignment (2)
#Sayem Chowdhury
#Q.(2)
#----------------------
# String Encription
#----------------------------

def Encryption( St,shift):
    #prompt user for a string in lower case letter
    
    print("Please enter a string in lowercase to encrypt : ", end=" ")
    St=input()
    St=St.lower()
    print(St)
    
    #Prompting for the number (key) to shift left or right:
    
    print("Please enter the Key you want to shift the letter to the left : ", end ="")
    shift=int(input())
    
    EN=""
    ER=""
    
    for ch in St:
            if (ch==" "):
                k=ord(ch)  #for left shifting
                l=ord(ch)  #for right shifting 
            else:
                k=(ord(ch)-shift)%122
                l=(ord(ch)+shift)%122
                if (k<97):
                    k=k+26
                if (l<97):
                    l=l+96
                  
            EN=EN+chr(k)
            ER=ER+chr(l)  
            

    print("Left Shifting: ", end="")    
    print(EN)
    print("Right Shifting: ", end="")    
    print(ER)
              
Encryption("S",2) # function Call
