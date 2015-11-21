import json
import urllib

content = urllib.urlopen('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_172408.json').read()
data = json.loads(content)
numbers = [ c['count'] for c in data['comments'] ]
print sum([int(x) for x in numbers])
