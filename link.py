from bs4 import BeautifulSoup
import urllib
import re
def searx(url):
 baseurl="https://www.youtube.com/results?search_query="
 search=url
 searchind=""
 for i in search.split():
  searchind=searchind+i
 page=urllib.request.urlopen(baseurl+searchind)
 soup = BeautifulSoup(page, 'html.parser')
 links = soup.find_all('a')
 for link in links:
  if "/watch?" in link['href']:
    return link['href']
    break
  
def plstry(url):
  string="None"
  while string == "None":
        string=str(searx(url))
  return string
