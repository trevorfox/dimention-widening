import requests
from BeautifulSoup import BeautifulStoneSoup as Soup

def parse_sitemap(url):
	resp = requests.get(url)
	
	# we didn't get a valid response, bail
	if 200 != resp.status_code:
		return False
	
	# BeautifulStoneSoup to parse the document
	soup = Soup(resp.content)
	
	# find all the <url> tags in the document
	urls = soup.findAll('url')
	
	# no urls? bail
	if not urls:
		return False
	
	# storage for later...
	out = []
	
	#extract what we need from the url
	for u in urls:
		loc = u.find('loc').string
		prio = u.find('priority').string
		change = u.find('changefreq').string
		last = u.find('lastmod').string
		out.append([loc, prio, change, last])
	return out
