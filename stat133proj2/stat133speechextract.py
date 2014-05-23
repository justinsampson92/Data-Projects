#must be run in Python 2.7
from BeautifulSoup import BeautifulSoup
import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import time
contentdict={}

cj=CookieJar()
opener= urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheader=[('User-Agent', 'Mozzila/5.0')]

page= "file:///Users/brandonflannery/src1/stat133/stat133proj2/stat133proj2speeches.html"
file1= "/Users/brandonflannery/src1/stat133/stat133proj2/stat133proj2speeches.html"
#print(page)
sourceCodelib= opener.open(page).read()
contentlib=re.findall(r'<p>(((.|\n|/t)*)?)</p>', sourceCodelib) #this takes everything within tags			
linkslib= re.findall(r'<link.*?href="(.*?)"', sourceCodelib) #this get the links
titleslib=re.findall(r'<title>(.*?)</title>', sourceCodelib) #this gets titles
headerslib=re.findall(r'<h>(.*?)</h>', sourceCodelib)
interestlib=re.findall(r'<p>(.*?)</p>', str(contentlib))


sourceCodesoup = BeautifulSoup(open(file1))
contentsoup = sourceCodesoup.findAll('p')

def makedict():
	global contentdict
	for x in range(len(headerslib)):
		contentdict[headerslib[x]]=contentsoup[x]
	print(contentdict)
	return contentdict 


makedict()

def function():
	global contentdict
	try:
		page= "file:///Users/brandonflannery/src1/stat133/stat133proj2/stat133proj2speeches.html"
		print(page)
		sourceCode= opener.open(page).read()
		content=re.findall(r'<p>(((.|\n)*)?)</p>', sourceCode) #this takes everything within tags that ends with  __			
		links= re.findall(r'<link.*?href="(.*?)"', sourceCode) #this get the links
		titles=re.findall(r'<title>(.*?)</title>', sourceCode) #this gets titles
		headers=re.findall(r'<h>(.*?)</h>', sourceCode)
		interest=re.findall(r'<p>(.*?)</p>', str(content))
		print(type(content), type(headers))
		print(content[0][1])
		print(type(content))
		for x in range(len(content)):
			contentdict[headers[x]]=content[x]
		print(contentdict)
		for speech in content:
			print(speech)
		for header in headers:
			print(header)
		for title in titles:
			print(title) #prints out the titles, can be put into lists
		#for link in links:
			#if ".rdf" in link:
				#pass
			#else:
				#print(link) #prints all of the links, can be put into a list
			#for words in content:
				#print(words) #this prints all of the words within <p></p> tags
				# you will need to filter some things out, change content







	except Exception, SyntaxError:
		print("Error: Cannot Parse")

#function()


# FRB:
	#want text in title tag, use regular expression
	#regaular expression is the r''
	#(.*?) looks for any repetitio of characters within a certain space, and extracts it
	#.*? looks fo rany repetitions in a certain space and doesnt evaluate them



