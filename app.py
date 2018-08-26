import time
import requests
import onionGpio

pin_light = onionGpio.OnionGpio(1)
pin_fan = onionGpio.OnionGpio(0)

pin_light.setOutputDirection(0)
pin_fan.setOutputDirection(0)

request = requests.get('https://chatbot-420.herokuapp.com/')
json = request.json()
pin_light.setValue(json['light'])
pin_fan.setValue(json['fan'])

while True:
	request = requests.get('https://chatbot-420.herokuapp.com/')
	json = request.json()
	
	pin_light.setValue(json['light'])
	pin_fan.setValue(json['fan'])
	
	print "Fan is "+(pin_fan.getValue())
	print "Light is "+(pin_light.getValue())
