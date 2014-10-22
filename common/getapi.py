import urllib2
import json

def get_nodeinfo_from_API():

	api_info={}
	request = urllib2.Request('http://[fdf5:5351:1dfd:b0::2]/confine/api/node/')
	response= None
	try:
		response = urllib2.urlopen(request)
	except:
		response = None

	if(response is None):
		return None

	value = unicode(str(response.read()), errors='ignore')
	page = json.loads(value)
	api_info["name"] = page['name']
	api_info["curent_state"] = page['set_state']
	api_info["Errors"] = page["errors"]
	api_info["soft_version"] = page["soft_version"]
	return api_info

