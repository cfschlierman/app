from BeautifulSoup import BeautifulSoup

event_data = open("event_data.txt", "r")


# raw > data
soup = BeautifulSoup(event_data.read())
# data_title = soup.a.text


for link in soup.find_all('a'):
	url = link.get('href')
	text = link.text.strip()
	print text
	print url