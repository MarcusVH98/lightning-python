import requests
import random
import time

url = "http://192.168.0.144/api/hpWNy9jfbACROBTB8diURwZQabXua0KrGcFV3pRe"

data = """
{
	"on": true,
	"xy": [0.7, 0.3]
}"""

# Set headers
response = requests.get(url, headers = {"Content-Type": "application/json"})

print(response)

# Turn the light on
response = requests.put(url + "/lights/1/state", data)

while True:

	time.sleep(1)

	x = random.uniform(0,1)
	y = random.uniform(0,1)

	print("x: " + str(x) + "\t" + "y: " + str(y))

	data = """
	{
		"on": true,
		"xy": [%f, %f]
	}""" % (x, y)

	response = requests.put(url + "/lights/1/state", data)
 
# Send data
#response = requests.put(url + "/lights/1/state", data)

#print(response)
#print(response.content)