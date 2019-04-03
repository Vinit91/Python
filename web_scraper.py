import requests
from bs4 import BeautifulSoup

url='https://www.youtube.com/results?search_query=python'

html = requests.get(url)

bsObj = BeautifulSoup(html.text, 'lxml')

name = bsObj.find('title').getText()

h3List = bsObj.findAll('h3',{'class':'yt-lockup-title '})

for h3 in h3List:
	print(h3.attrs)

print('\n', name)

# for h3 in bsObj.find_all('h3',{'class':'yt-lockup-title '}): 
	# #if h3['class']== 'accessible-description':
	# for h in h3:
		# h = h3.find_all('a')
		
		#print(h.attrs)
		#h3.previous_sibling("span", {"class":"accessible-description"})['aria-label']

spanList = bsObj.find_all('span',{'class','accessible-description'})


# 'style-scope ytd-video-meta-block' accessible-description || r = res.find_all(attrs={'aria-label'}) r.gettext()





for sp in spanList:
	res = sp.previous_sibling('span')
	for r in res:
		x= r.attrs
		print(x)
	# for r in res.find("span"):
		# print(r['aria-label'])
		


# for h3 in h3List:
	# print(h3List)
