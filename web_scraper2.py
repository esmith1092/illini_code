import requests
import bs4

url = input('Enter your URL: ')
#requests.get retrieves the html of the website here
res = requests.get(url)
#lxml is a library that creates a new tree of tags from the website
#can use lxml or html parser
soup =bs4.BeautifulSoup(res.text, 'lxml')

#tagclass = input('Enter the tag class:')
# list = []
	# if i.text not in list:
		# print(i.text)
		# list.append(i.text)
		
# n = 0
	 
# for i in list:
	# n = n+1
	
# print("There are", n, "results")

tags = soup('a')
tag_list = []
for tag in tags:
	tag_list.append(tag.get('href', None))
	
for link in tag_list:
	if link.startswith('http://www.espn.com/college-football/player/_/id/') is True:
		name = link.split("/")[8]
		first_name = (name.split("-")[0]).upper()
		last_name = (name.split("-")[1]).upper()
		print(first_name, last_name)