from datetime import datetime
from bson.objectid import ObjectId

##########################################################
# JSON helper
##########################################################
#response json helper
def prepare_response_json(in_json):
	for k in in_json:
		if type(in_json[k]) is dict:
			prepare_response_json(in_json[k])
		elif type(in_json[k]) is list:
			for item in in_json[k]:
				if type(item) is not float and type(item) is not str:
					prepare_response_json(item)
		elif in_json[k].__class__.__name__ is ObjectId().__class__.__name__:
			in_json[k] = str(in_json[k])
		elif type(in_json[k]) is datetime:
			in_json[k] = in_json[k].strftime("%Y-%m-%dT%H:%M:%SZ")
	return in_json