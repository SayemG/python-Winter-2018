EmployeeNames=['Moussa','Shayan','Aaron','Mustafa','Shafiq','Sayem','Adeeba','Salwa','Erica']

'''
for element in EmployeeNames:
    print(element)
	
print("----------------")
for i in range(0,len(EmployeeNames)):
    print(EmployeeNames[i])

print("----------------")	
for i in range(len(EmployeeNames)-1,-1,-1):#start index=8, ending= -1 [8 to -1 excluding -1]
    print(EmployeeNames[i],i)
'''
  
print("----------------")
#********
for i in range(-1, -1* len(EmployeeNames)-1,-1):
    print(EmployeeNames[i])
print("----------------")
#*****************
for element in EmployeeNames[::-1]:
    print(element)
	
	

