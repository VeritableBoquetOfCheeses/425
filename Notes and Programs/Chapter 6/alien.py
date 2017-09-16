alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

aliens = []

for thirtyAliens in range(30):
	newAlien = {'color': 'green', 'points': 5}
	aliens.append(newAlien)



"""
#print(alien_0)
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
#print(favorite_languages)
allison = {'firstName': 'Allison', 'lastName': 'Gray', 'age': 32, 'city': 'Austin'}

for attributes in allison:
	print(allison[attributes])

for key, value in allison.items():
	print(key, value)

for values in allison.keys():
	print(values)
"""