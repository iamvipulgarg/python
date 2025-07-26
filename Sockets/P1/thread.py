from threading import *
n=5
def Thread1():
    print('Thread1 Started')
    for i in range(1,n):
        print(i,'Thread1')
    print('Thread1 Ended')

def Thread2():
    print('Thread2 Started')
    for i in range(1,n):
        print(i,'Thread2')
    print('Thread2 Ended')
   
# By using Class   
class Thread3:
    def Thread3(self):
        print('Thread3 Started')
        for i in range(1,n):
            print(i,'Thread3')
        print('Thread3 Ended')

# by Extending thread class
class Thread4(Thread):
    def run(a):
        print('Thread4 Started')
        for i in range(1,5):
            print(i,'Thread4')
        print('Thread4 Ended')


print('Main Started')
th1=Thread(target=Thread1)
th2=Thread(target=Thread2)
m=Thread3()
th3=Thread(target=m.Thread3)
n1=Thread4()
n1.start()

th1.start()
th2.start()
th3.start()
for i in range(1,n):
    print(i,'Main')
print('Main Ended')