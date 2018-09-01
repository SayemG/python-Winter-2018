#Assignment (2)
#Sayem Chowdhury
#Q.(2)
#----------------------

#counting the total number of words in file:
#-------------------------------------------
f=open("myfile.txt", "r")
count=0;
for line in f:
    word_list=line.split()
    for word in word_list:
        count= count+1

print("The total number of words is : ", count)
f.close()
#------------------------------------------------------
#Counting the frequency of words in file
#-------------------------------------------------------
import collections
f=open("myfile.txt", "r")
word_count = collections.Counter()
for line in f:
    word_count.update(line.split()) #"update()" method, updates the dictionary with elements from
                                    #a dictionary object 
                                    #If update() is called without passing parameters,
                                    #the dictionary remains unchanged.

    
#print(word_count)
for p,q in word_count.items():
    print (p, q)

f.close()
#-----------------------------------------

#counting sentense in file
#-----------------------------------------
f=open("myfile.txt", "r")
text=f.read()
#print(text)
sentence=text.count('.')+text.count('?')+text.count('!')
print("sentence counted =", sentence)
f.close()
#-------------------------------------------------------------

