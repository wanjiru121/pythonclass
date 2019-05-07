def tens():
	list = [1,2,3,4,5,6,7,8,9]
	newList = []
	for x in list:
		y = x*10
		newList.append(y)
	print(newList)
def squares():
	list = [2,4,6,8,10,12]
	squared = [g*g for g in list]
	print(squared)
def sorted():
	list1=[9,1,4,7,3]
	list2=[5,2,6,8,0]
	list3=list1+list2
	list3.sort()
	print(list3)
def range_sum(n):
	x = sum(range(1,n+1))
	print(x)
def largest(list):
	x = max(list)
	print(x)
def smallest(list):
	x = min(list)
	print(x)
def my_modulus():
	m = dict()
	for x in range(10,20):
		m[x]=x%3
	print(m)
def balance():
	student1={"name":"Irene","balance":1000}
	student2={"name":"Pauline","balance":2000}
	student3={"name":"Naima","balance":3000}
	student4={"name":"Rose","balance":1000}
	students=[student1,student2,student3,student4]
	for student in students:
		sms = "Hello {}, your balance is {}".format(student["name"],student["balance"])
		print(sms)

