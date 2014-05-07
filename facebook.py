import requests
from xml import parse_sitemap

def graph(url):
	graph = 'http://graph.facebook.com/'
	endpoint =   graph + url
	r = requests.get(endpoint)
	return r.json()

if __name__ == '__main__':
	sitemap =  parse_sitemap('http://www.swellpath.com/post-sitemap.xml')
	for page in sitemap:
		print graph(page[0])

