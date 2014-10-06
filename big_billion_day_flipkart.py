import urllib
import webbrowser
import mechanize
from bs4 import BeautifulSoup

def clone(soup, tag):
   newtag = soup.new_tag(tag.name)
   for attr in tag.attrs:
      newtag[attr] = tag[attr]
   return newtag

try:
	html = urllib.urlopen("http://flipkart.com/").read()
	soup = BeautifulSoup(html)
	important = soup.find(id="steal")
	flag = 0
	if important:
		if important['data-outofstock'] == 'false':
			deals = soup.find_all("div", {"class":"pu-offer"})
			for i in deals:
				if "Flat at Rs" in i.string:
					price = i.string[17:]
					if int(price) < 100:
						flag = flag + 1
						a = clone(soup, i.parent)
						print "http://flipkart.com" + a.get('href')
						webbrowser.open("http://flipkart.com" + a.get('href'))
				elif "Just at Re." in i.string:
					price = i.string[17:]
					if int(price) < 100:
						flag = flag + 1
						a = clone(soup, i.parent)
						print "http://flipkart.com" + a.get('href')
						webbrowser.open("http://flipkart.com" + a.get('href'))
			if (flag == 0):
				print "No products less than Rs. 100"
		else:
			print "Out of stock"
	else:
		print "No steal deals"
except:
	print "Could not open"