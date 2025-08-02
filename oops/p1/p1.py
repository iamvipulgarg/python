"""
class Top:
	def m1(self):
		print('m1 inside Top class')
		print(id(self))
		
t1 = Top()
t1.m1()
print(id(t1))

t2= Top()
t2.m1()

class Check:
    def chk(self):
        print('chk inside Check')
        
c1=Check()
c1.chk()

"""

class Student:
    def ls(self):
        self.l1=[]
        
    def add(self,roll,name):
        self.roll= roll
        self.name= name
        dic = {'Roll No':self.roll, 'Name' : self.name}
        self.l1.append(dic)
        
    def show(self):
        # print('Roll No : ',self.roll)
        # print('Name : ',self.name)
        for i in self.l1:
            print(i)
s1=Student()
s1.ls()
s1.add(100,'Vipul Garg')
s1.add(101,'Vipul')
s1.add(102,'Garg')
s1.show()