class MpesaAccount:
	def __init__(self,name,phone_number,balance):
		self.name = name
		self.phone_number = phone_number
		self.balance = balance
	def deposit(self,a):
		deposit = a
		self.balance = self.balance + a
		message1 = "Hello {},confirmed you have deposited {}kshs in your account {}.Your new Mpesa balance is {}kshs".format(self.name,a,self.phone_number,self.balance)
		print(message1)
	def withdraw(self,b):
		b<self.balance
		self.balance = self.balance - b
		message2 = "Hello {},confirmed your withdrawal of {}kshs is successful.Your new mpesa balance is {}kshs".format(self.name,b,self.balance)
		print(message2)
	def check(self):
		balance = self.balance
		message3 = "Hello {},your current mpesa balance is {}".format(self.name,self.balance)
		print(message3)
