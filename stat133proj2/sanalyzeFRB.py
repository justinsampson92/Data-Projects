import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import time

cj=CookieJar()
opener= urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheader=[('User-Agent', 'Mozzila/5.0')]

def main():
	try:
		page= "/Users/brandonflannery/src1/stat133/stat133proj2"
		sourceCode= opener.open(page).read()
		#print(sourceCode)
		content=re.findall(r'<p>(((.|\n)*)?)</p>', sourceCode) #this takes everything within tags that ends with  __			
		links= re.findall(r'<link.*?href="(.*?)"', sourceCode) #this get the links
		titles=re.findall(r'<title>(.*?)</title>', sourceCode) #this gets titles
		interest=re.findall(r'<p>(.*?)</p>', str(content))
		for contents in interest:
			print contents
		#for title in titles:
			#print title #prints out the titles, can be put into lists
		#for link in links:
			#if ".rdf" in link:
				#pass
			#else:
				#print link #prints all of the links, can be put into a list
			#for words in content:
				#print words #this prints all of the words within <p></p> tags
				# you will need to filter some things out, change content







	except Exception, e:
		print str(e)

main()


# FRB:
	#want text in title tag, use regular expression
	#regaular expression is the r''
	#(.*?) looks for any repetitio of characters within a certain space, and extracts it
	#.*? looks fo rany repetitions in a certain space and doesnt evaluate them



