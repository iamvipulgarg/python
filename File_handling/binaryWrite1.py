import pickle

p=open('a1.dat','wb')

data=[]
choice = 1

while choice ==1:
    
    id=int(input('Enter Id : '))
    name=input('Enter Name : ')
    sal=int(input('Enter Salary : '))
    data.append([id,name,sal])
    choice = int(input('Enter 0 for exit : '))
pickle.dump(data,p)