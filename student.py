class Student:
	def __init__(self,first_name,second_name,age):
		self.first_name	= first_name	
		self.second_name = second_name	
		self.age = age
	def full_name(self):
		name = "{} {}".format(self.first_name,self.second_name)	
		print(name)
	def year_of_birth(self):
		return	2019 - self.age	
	def initials(self):
		inits = self.first_name	[0] + self.second_name[0]
		return	inits	

