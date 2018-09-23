import requests
import bs4

url = input('Enter your URL: ')
#requests.get retrieves the html of the website here
res = requests.get(url)
#lxml is a library that creates a new tree of tags from the website
#can use lxml or html parser
soup =bs4.BeautifulSoup(res.text, 'lxml')
hi = soup.select('title') #selecting the title tag 

print("The title of this website is:", hi[0].getText())

tags = soup('a')
tag_list = []
for tag in tags:
	
    # # Look at the parts of a tag
    # #print('TAG:',tag)
	tag_list.append(tag.get('href', None))

		# #print(new_tag)
    # #print('Contents:',tag.contents[0])
    # #print('Attrs:',tag.attrs)
web = []	
for new_tag in tag_list:
	if (new_tag is not None and new_tag.startswith("team") is True):
			web.append(url+"/"+new_tag)
		
for item in web:
	#print(item)-code works here, prints out list of all teams pages
	res2 = requests.get(item)
	soup2 = bs4.BeautifulSoup(res2.text, 'lxml')
	#print(soup2)
	#hello = soup2.select('rank')
	#print(hello)
print(soup2)

# #looping through all of the tags on the website with the toctext tag
# tagclass = input('Enter the tag class:')
# list = []
# for i in soup.select(tagclass):
	# if i.text not in list:
		# print(i.text)
		# list.append(i.text)
		
# n = 0
# for i in list:
	# n = n+1
# print("There are", n, "results")




