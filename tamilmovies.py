import requests
from bs4 import BeautifulSoup
import re

'''This script takes a movie as an input and prints the Movie torrent download links'''

def fetch_download(url):					#Function to fetch the torrent download link from the web page
        data = requests.get(url)
        soup_data = BeautifulSoup(data.content, 'html.parser')
        elements = soup_data.find_all('a', title='Download attachment')

        return elements[0]['href']

movie = input("Which Tamil movie do you want? ")		#Takes movie input as string
movie = movie.lower().split()					#Splits into different words(if more than one)
movie = "-".join(movie)
pattern = r"-"+movie+"-"
results = []
flag = 0
count = 0

for i in range(1,150):
	if i==1:
		url = "http://tamilrockers.ws/index.php/forum/115-tamil-new-dvdrips-hdrips-bdrips-movies/?prune_day=100&sort_by=Z-A&sort_key=last_post&topicfilter=all"
	else:
		url = "http://tamilrockers.ws/index.php/forum/115-tamil-new-dvdrips-hdrips-bdrips-movies/page-"+str(i)+"?prune_day=100&sort_by=Z-A&sort_key=last_post&topicfilter=all"
	
	data = requests.get(url)
	soup_data = BeautifulSoup(data.content, 'html.parser')
	elements = soup_data.find_all('a', class_='expander closed')

	for link in elements:
		if re.search(pattern,link['href']):
			flag = 1
			if count < 4:
				results.append(fetch_download(link['href']))
				count+=1
			else:
				break
		else:
			continue

	if flag == 1:
		if count == 1:
			continue
		else:
			break

for link in results:
	print(link)

