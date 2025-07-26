import pickle

p=open('a1.dat','rb')

data=pickle.load(p)
# print(data)

for i in data:
    print('Id : ', i[0], 'Name : ', i[1], 'Salary : ', i[2])
    print()
    
    
print('*'*30)

res=[];
p.seek(0)
while True:
    try:
        res=pickle.load(p)
        # res.append(pickle.load(p))
    except:
        break;
        
for i in res:
    print('Id : ', i[0], 'Name : ', i[1], 'Salary : ', i[2])
    print()