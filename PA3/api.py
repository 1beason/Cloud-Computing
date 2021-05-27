from flask import Flask, json, abort, make_response, request

# The temperature to be gotten and set via the funtions below
SETPOINT = 0 # intitialize to 0 for now

# temp of the room (just hard coding for now)
TEMP = 70

JSON_DS = [{"id" : 1, "value": TEMP}, {"id": 2, "value": SETPOINT}]
 

# define the actual app module
api = Flask(__name__)

""" get_temp() function gets the temp
    endpoint: /ThermsAreUs/api/v1.0/current-temp
    not to be confused with get setpoint
"""
@api.route('/ThermsAreUs/api/v1.0/current-temp', methods=['GET'])
def get_temp():
	
	return json.dumps({'temp': JSON_DS[0]})  # return hard coded temp of the room


""" get_setpoint() function gets the current setpoint
    endpoint: /ThermsAreUs/api/v1.0/current-setpoint
"""
@api.route('/ThermsAreUs/api/v1.0/current-setpoint', methods=['GET'])
def get_setpoint():

	return json.dumps({'setpoint': JSON_DS[1]}) # return the appropriate part of our json ds


""" set_setpoint() but with a PUT method for setting the setpoint
    same endpoint as above
"""
@api.route('/ThermsAreUs/api/v1.0/current-setpoint', methods=['PUT'])
def set_setpoint():
	print(request)
	if not request.json:
		print("request was not json")
		abort(400)
	if 'id' in request.json and request.json['id'] != 2:
		print("id wasnt in the json or it wasnt 2")
		abort(400)
	if 'value' in request.json and not isinstance(request.json['value'], int):
		print("value wasnt in json or it wasnt type int")
		abort(400)
	JSON_DS[1]['value'] = request.json.get('value', request.json['value'])
	SETPOINT = JSON_DS[1]['value']
	return json.dumps({'success': True})


""" error handler """
@api.errorhandler(404)
def not_found(error):
	return make_response(json.dumps({'error': 'Not found'}), 404)

@api.errorhandler(400)
def bad_request(error):
	return make_response(json.dumps({'error': 'Bad request'}), 400)


if __name__ == '__main__':
	api.run(debug=True, host="0.0.0.0")
