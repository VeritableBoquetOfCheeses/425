#####CARE OF THE SYNTAX | THIS IS WRITTEN FOR PYTHON 2.7#####


#Importing the requests module, which is a library that contains code to make API calls to websites with Python
import requests

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#Make an API call to GitHub the store and print the result

"""
--> https://api.github.com/ | directs the request to the part of GitHub's website that responds to API calls
--> search/repositories | directs a search of all repositories to be conducted
--> ? | signifies that an argument will be passed immediately afterwards
--> q= | this character stands for query; MUST USE q, error will result otherwise
--> language:python | duh
--> &sort=stars | & adds an additional argument, which in this case is to sort by number of stars the projects have
"""
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'


#get() returns a Response object that's stored in the variable r
r = requests.get(url)

#status_code is a data member of the object request called 'r'
print 'Status code: ', r.status_code

"""
--> json | JavaScript Object Notation: data interchange format
	-> creates a dictionary (key-value pair data type; like hash table in java)
		> keys
			. total_count
				- total repositories found from search of GitHub for java projects
			. items
				- data for each repository returned to Response 
			. incomplete_results
				- boolean value determining any error during request 
"""
response_dict = r.json()

print 'Total Repositories: ', response_dict['total_count']

repo_dicts = response_dict['items']
print 'Repositories Returned: ', len(repo_dicts)

repo_0_dict = repo_dicts[0]
print len(repo_0_dict)

#All attributes of the first returned repository
	#print repo_0_dict.keys()


#Refer to p. 386-387
names, stars = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')














