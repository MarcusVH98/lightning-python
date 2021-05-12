import requests
import random
import time
import math

#MAX_HUE = 65534
url = "http://192.168.0.144/api/hpWNy9jfbACROBTB8diURwZQabXua0KrGcFV3pRe"

min_bri = 10
max_bri = 254
max_hue = 65535

bri = 254

lastBriHigh = True;

data = """
{
	"on": true,
	"xy": [0.7, 0.3]
}"""

# Set headers
response = requests.get(url, headers = {"Content-Type": "application/json"})

print("Setting header response: \n" + str(response))

# Turn the light on
response = requests.put(url + "/lights/1/state", data)

def setBri():
	global lastBriHigh
	global bri
	if (lastBriHigh):
		lastBriHigh = not lastBriHigh
		bri = min_bri
	else:
		lastBriHigh = not lastBriHigh
		bri = max_bri

def randomHue():
	n = 0

	while True:

		time.sleep(0.2)

		#Clamp between 0 and 1
		hue = int(random.random() * max_hue)

		if (n%2 == 0):
			setBri()

		data = """
		{
			"hue": %d,
			"bri": %d
		}""" % (hue, bri)

		response = requests.put(url + "/lights/1/state", data)
		n += 1
		#printDebug(response)

def circular():
	while True:
		time.sleep(0.1)

		#hue = random.uniform(0, 1) * 65534
		hue = int((time.time()*30000 % 65535))

		#print("x: " + str(x) + "\t" + "y: " + str(y))

		data = """
		{
			"hue": %d
		}""" % (hue)

		response = requests.put(url + "/lights/1/state", data)
		#printDebug(response)

def printDebug(res):
	print(response)
	print(response.content)

# Lightning mode
randomHue()
#circular()