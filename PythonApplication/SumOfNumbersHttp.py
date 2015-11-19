import re
import urllib

html = urllib.urlopen('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_172407.html').read()
numbers = []
numbers += re.findall('<span class="comments">([0-9]+)</span>', html)
print sum([int(x) for x in numbers])