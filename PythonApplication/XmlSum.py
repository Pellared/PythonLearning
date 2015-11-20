import xml.etree.ElementTree as ET
import urllib

data = urllib.urlopen('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_172404.xml').read()
tree = ET.fromstring(data)
numbers = tree.findall('.//count')
print sum([int(x.text) for x in numbers])
