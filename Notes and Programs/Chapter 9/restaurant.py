class Restaurant():

	def __init__(self, restaurantName, cuisineType):
		self.restaurantName = restaurantName
		self.cuisineType = cuisineType

	def describeRestaurant(self):
		print("The name of this restaurant is " + self.restaurantName.title() + " and its cuisine type is " + self.cuisineType.title() + ".")

	def openRestaurant(self):
		print(self.restaurantName.title() + " is now open for business.")

restaurant = Restaurant("chilis", "american")
restaurant1 = Restaurant("catfish king", "fish")
restaurant2 = Restaurant("olive garden", "italian")
restaurant3 = Restaurant("pie five", "pizza")

print("Restaurant name: " + restaurant.restaurantName.title())
print("Cuisine type: " + restaurant.cuisineType.title())
restaurant.describeRestaurant()
restaurant.openRestaurant()
restaurant1.describeRestaurant()
restaurant2.describeRestaurant()
restaurant3.describeRestaurant()