def f1():
	print('hi from function')
# global
d= 'H'
def f2(c,n):
	for i in range(n):
		print(d,end='')
	print()

def f3():
    b=a+10
    print(b)
    
    
def f4():
    print(a)

a=10
f3()
f4()
# f1()
# f2('*',20)
# f2('@',50)


def add(a,b,c=20,d=30):
    print('Sum  : ', a+b+c+d)

add(10,20)


def argsAdd(*n):
    sum = 0
    for i in n:
        sum = sum+i
        
    print('sum :', sum)
    
argsAdd(10,20)
argsAdd(10,20,30)
argsAdd(10,20,30,40)
argsAdd(10,20,30,40,50)