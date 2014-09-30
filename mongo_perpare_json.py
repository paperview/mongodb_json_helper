from datetime import datetime
from bson.objectid import ObjectId

##########################################################
# JSON helper
##########################################################
def prepare_response_json(in_json):
	if type(in_json) is list:
		for i in in_json:
			if type(i) is list or type(i) is dict:
				prepare_response_json(i)
			in_json[in_json.index(i)] = check_convert_to_str(i)
	if type(in_json) is dict:
		for k in in_json:
			if type(in_json[k]) is list or type(in_json[k]) is dict:
				prepare_response_json(in_json[k])
			in_json[k] = check_convert_to_str(in_json[k])
	return check_convert_to_str(in_json)


def check_convert_to_str(x):
	if x.__class__.__name__ is ObjectId().__class__.__name__:
		print("\n\n %s" % x)
		return str(x)
	elif type(x) is datetime:
		return x.strftime("%Y-%m-%dT%H:%M:%SZ")
	else:
		return x
