"""A class that can be used to represent a car."""
class Car():

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometerReading = 0

	def getDescriptiveName(self):
		longName = str(self.year) + ' ' + self.make + ' ' + self.model
		return longName.title()

	def readOdometer(self):
		print('This car has ' + str(self.odometerReading) + ' miles on it.')

	def updateOdometer(self, mileage):
		if mileage >= self.odomoterReading:
			self.odometerReading = mileage
		else:
			print("You can't roll back the odometer!")

	def incrementOdometer(self, mileage):
		if mileage >= 0:
			self.odometerReading += mileage
		else:
			print("You can't subtract driven miles from the odometer!")
"""
class ElectricCar(Car):

	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.batterySize = 70

	def describeBattery(self):
		print("The battery capacity is " + str(self.batterySize) + " kWH.")
"""