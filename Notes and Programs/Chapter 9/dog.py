class Dog():

	#Class constructor
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		print(self.name.title() + ' is now sitting.')

	def rollOver(self):
		print(self.name.title() + ' rolled over!')

allison_sDog = Dog('Winston', 3)
myFutureDog = Dog('Moose', 4)

print("My dog's name is " + myFutureDog.name.title() + ".")
print("My dog is " + str(myFutureDog.age) + " years old.")
allison_sDog.sit()
myFutureDog.rollOver()