#Extra Credit

vowels=('a', 'e', 'i' ,'o','u','A','E','I','O','U')
count=0

str_st=input("Please enter a word : ")
w=str_st[0]
if (len(str_st)>0):
    if w in vowels:
        wd=str_st+'way'
        print("Pig Lattin = ",wd)
    elif w not in vowels:
        # i in range (1,len(str_st)):
            #count=i
            #if str_st[i]in vowels:
            #index=i
        wd_n=str_st[1:]
        wnfinal=wd_n+str_st[0:1]+'ay'
        print("pig latin= " , wnfinal)
   
            
    #elif count==len(str_st)-1:
    else:
        print("Sorry not able to convert Pigg-Lattin")

    



                
                
        
    
        
