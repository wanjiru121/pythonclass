from datetime import datetime
class MpesaAccount:
    def __init__(self,name,phone_number):
        self.balance=0
        self.deposits=[]
        self.loans=[]
        self.withdrawals=[]
        self.name = name
        self.phone_number = phone_number
        self.loan=0
    def deposit(self,a):
        now = datetime.now()
        object = {"time":now,"amount":a}
        self.balance = self.balance + a
        self.deposits.append(object)
        message1 = "Hello {},confirmed you have deposited {}kshs in your account {}.Your new Mpesa balance is {}kshs".format(self.name,a,self.phone_number,self.balance)
        print(message1)
    def withdraw(self,b):
        if b<self.balance:
             now = datetime.now()
             object = {"time":now,"amount":b}
             self.withdrawals.append(object)
             self.balance = self.balance - b
             message2 = "Hello {},confirmed your withdrawal of {}kshs is successful.Your new mpesa balance is {}kshs".format(self.name,b,self.balance)
             print(message2)
        else:
             print("Not enough balance")
    def check(self):
        balance = self.balance
        message3 = "Hello {},your current mpesa balance is {}".format(self.name,self.balance)
        print(message3)
    def my_deposits(self):
        for object in self.deposits:
            time = object["time"].strftime("%A %d %B %Y %I:%M%p")
            amount = object["amount"]
            respond3="On {},you deposited {}".format(time,amount)
            print(respond3)
    def my_withdrawals(self):
        for y in self.withdrawals:
            time=y["time"].strftime("%A %d %B %Y %I:%M%p")
            amount=y["amount"]
            respond2="On {},you withdrew {}".format(time,amount)
            print(respond2)

    def my_loans(self):
        for c in self.loans:
            time = c["time"].strftime("%A %d %B %Y %I:%M%p")
            respond = "On {},you took a loan of {}kshs".format(time,self.loan)
            print(respond)
    def give_loan(self,z):
        total = 0
        for x in self.deposits:
         a = x["amount"]
         total+=a
        if len(self.deposits)>=5 and z<total/3 and self.loan==0:
            self.loan = self.loan + z
            self.balance = self.balance + z
            print("Your request for a loan of {}kshs has been accepted and is being processed and deposited in your account".format(z))
            self.deposits.append(self.loan)
        
        else:
            print("You do not qualify for a loan.Make sure to deposit more to qualify for a loan")

    def repay_loan(self,k):
        if k <= self.loan:
           self.loan = self.loan - k
           self.balance = self.balance - k
           print("you have withdrawn {}kshs to pay your loan,your outstanding loan balance is {}kshs".format(k,self.loan))
           self.withdrawals.append(self.loan)
        elif k > self.loan:
           self.loan = self.loan - k
           self.loan=0
           over = k - self.loan
           print("your loan has been fully settled.The overpayment of {} has been deposited back into your account".format(over))
           self.deposits.append(over)
           self.balance=(self.balance-self.loan + over)
    def my_statement(self):
        limerick_line = []
        for object in self.deposits:
            time = object["time"].strftime("%A %d %B %Y %I:%M%p")
            amount = object["amount"]
            respond3="On {},you deposited {}".format(time,amount)
            limerick_line.append(respond3)
        for object in self.withdrawals:
            time=object["time"].strftime("%A %d %B %Y %I:%M%p")
            amount=object["amount"]
            respond2="On {},you withdrew {}".format(time,amount)
            limerick_line.append(respond2)
        for c in self.loans:
            time = c["time"].strftime("%A %d %B %Y %I:%M%p")
            respond = "On {},you took a loan of {}kshs".format(time,self.loan)
            limerick_line.append(respond)
        for p in limerick_line:
            print(p)



