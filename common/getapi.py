import urllib2
import json

def get_nodeinfo_from_API():

	api_info={}
	request = urllib2.Request('http://127.0.0.1/confine/api/node/')
	response= None
	try:
		response = urllib2.urlopen(request)
	except:
		response = None

	if(response is None):
		return None

	value = response.read()
	try:
	    page = json.loads(value)
	except:
	    return {}	
	api_info["name"] = page['name']
	api_info["curent_state"] = page['set_state']
	api_info["Errors"] = page["errors"]
	api_info["soft_version"] = page["soft_version"]
	return api_info

