from car import Car

myNewCar = Car('audi', 't4 quatro', 2016)
print(myNewCar.getDescriptiveName())
myNewCar.odometerReading = 23
myNewCar.readOdometer()