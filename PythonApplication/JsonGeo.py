import json
import urllib

serviceurl = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/geojson?'
address = 'University College Dublin'
url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
content = urllib.urlopen(url).read()
data = json.loads(content)
print data['results'][0]['place_id']