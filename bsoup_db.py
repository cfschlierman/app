from bs4 import BeautifulSoup
import sqlite3

# pulls elements we want from overall html
# raw
raw_title = soup.findAll("span", {"class": "indexed-biz-name"})
soup = BeautifulSoup(str(raw_title))
data_pretty = soup.prettify()
event_data = open("event_data.txt", "r+")
event_data.write(str(data_pretty))


# raw > data
soup = BeautifulSoup(data_pretty)
data_title = soup.a.text
# print data_title

# http://www.sixfeetup.com/blog/an-introduction-to-beautifulsoup < this should help


# raw > data
# soup = BeautifulSoup(event_data.read())

for link in soup.find_all('a'):
	text = link.text.strip()
	print text

for link in soup.find_all('a'):
	url = link.get('href')
	print url
	
	
	

# we can call this function when we run a selenium script to add the data to the db
 
conn = sqlite3.connect("db/database.db")
cursor = conn.cursor()
 
cursor.execute("""CREATE TABLE events
                  (title text, link text, date text) 
               """)
	
# need to make variables 'title' 'link' 'date' 'category' 'location'
# import them in from the beautifulsoup file?
cursor.executemany("INSERT INTO events VALUES (?,?,?)", title, link, date)
conn.commit()	
