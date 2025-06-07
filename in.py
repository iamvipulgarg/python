d1 = {}
while True:
    name = input('Enter Name :')
    if name == '':
        break;
    else:
        if name in d1:
            print('Record Exist ******************')
            print(name, "DOB : ",d1[name])
        else:
            dob = input('Enter DOB :')
            d1[name]=dob
    
print('Data :- ' , d1)

# a=float (input("Enter value "))
# b=float (input("Enter value "))
# c=a+b
# print(c)

# print(type(b))
# print(type(c))


# int()
# float()
# str()