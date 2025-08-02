class Bank:
    def __init__(self):
        self.acc_no = input("Enter Account no : ")
        self.name = input("Enter Name : ")
        self.amt = int(input("Enter Amount : "))
    
    def enquiry(self):
        print("Acc : ", self.acc_no)
        print("Name : ", self.name)
        print("AMT : ", self.amt)
        
    def deposite(self):
        dep_amt = int(input("Enter Amount to deposite : "))
        if dep_amt > 0:
            self.amt = self.amt + dep_amt
    
    def withdrawl(self):
        amt = int(input("Enter Amount to withdrawl : "))
        if (amt > 0 ) and (self.amt > amt):
            self.amt = self.amt - amt
        else:
            print('Invalid Amt')
data=[]

while True:
    print("0: Enquiry & exit : ")
    print("1: New Record : ")
    print("2: Deposite : ")
    print("3: Withdrawl : ")
    print("4: Delete Account : ")
    print("*"*30)
    choice = int(input("Enter you Choice : "))
    if choice == 0:
        for b1 in data:
            b1.enquiry()
            print("*"*20)
        break
    elif choice == 1:
        b1=Bank()
        data.append(b1)
    elif choice == 2:
        acc = input("Enter Acc No : ")
        for i in data:
            if i.acc_no == acc:
               i.deposite()
    elif choice == 3:
        acc = input("Enter Acc No : ")
        for i in data:
            if i.acc_no == acc:
               i.withdrawl()
    elif choice == 4:
        acc = input("Enter Acc No : ")
        for i in data:
            if i.acc_no == acc:
               data.remove(i)
                
    
# for i in range(3):
    # b1=Bank()
    # data.append(b1)
    
# for b1 in data:
    # b1.enquiry()
    # print("*"*20)