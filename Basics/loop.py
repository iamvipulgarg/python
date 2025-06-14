# a = range(10)
# print(1 in a)


# for i in range(1,10):
    # print(i)
    
    
# for i in range(1,5):
    # for j in range(1,i+1):
        # print(j,end='')
    # print()
    
    
# for i in range (1,6):
    # for j in range(1,6):
        # if i==1 or j==1 or i==3 or (j==5 and i < 4) :
            # print('*',end='')
        # else:
            # print(' ',end='')
    # print()

# for i in range(1,6):
    # for j in range (5,0,-1):
        # if j > i-1:
            # print(j,end='')
    # print()

s = 0


for i in range(1,100000):
    a=i
    cn=len(str(a))
    s=0

    while a>0:
        b = a%10
        s=s+ b**cn
        a=a//10
    if s==i:
        print(i,'armstong')
    
 