import urllib
from BeautifulSoup import *

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Darby.html' 
for _ in range(7):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[17].get('href', None)
print url