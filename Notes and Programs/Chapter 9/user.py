class User():
	 def __init__(self, firstName, lastName, age, classification, idNum, major):
	 	self.firstName = firstName
	 	self.lastName = lastName
	 	self.age = age
	 	self.classification = classification
	 	self.idNum = idNum
	 	self.major = major

	 def describeUser(self):
	 	print(self.lastName.title() + ", " + self.firstName.title())
	 	print("INFORMATION:\nAGE\t\tCLASSIFICATION\t\tID\t\tMAJOR")
	 	print(str(self.age) + "\t\t" + self.classification.title() + "\t\t" + str(self.idNum) + "\t\t" + self.major.title())

	 def greetUser(self):
	 	print("Hello " + self.firstName.title() + ", welcome to the program.")

user1 = User("Allison", "Gray", 42, "freshman", 20987437, "cyber security")
user2 = User("william", "scott", 27, "senior", 20131667, "computer science")
user3 = User("ray", "deblanc", 82, "freshman", 99999999, "social work")
user4 = User("gaukhara", "kalmurzayeva", 27, "senior", 28998475, "human resources")

user1.greetUser()
user2.greetUser()
user3.greetUser()
user4.greetUser()

user1.describeUser()
user2.describeUser()
user3.describeUser()
user4.describeUser()
