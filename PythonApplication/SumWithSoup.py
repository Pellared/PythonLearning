import urllib
from BeautifulSoup import *

html = urllib.urlopen('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_172407.html').read()
soup = BeautifulSoup(html)
tags = soup('span')
print sum([int(x.contents[0]) for x in numbers])