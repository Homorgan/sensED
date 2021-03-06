############################################################
# Simple Python program that repeatedly reads the Grove
# Temperature & Humidity Sensor (DHT11) connected to
# GrovePi port D8 and writes the current value to Pi Land. 
#
# To run this program from the bash command prompt,
# type this and hit Enter:
#
#    sudo python grove-dht11-piland.py
#
############################################################

import time
import requests
import grovepi

# Write the value to a specific data slot in a Pi Land room

# NOTE:  Change the room, dataslot, and devicename below to something
#        different for your own use so that everyone isn't using
#        the same data slot and overwriting each other's data.

# Pi Land settings
room      = 506                          # Room number to use (1 through 999)
slot_temp = 24                           # Data slot number to use (1 through 30)
name_temp = "Inside Temp DHT11"          # Descriptive name for your device, put '+' for space char
slot_humi = 25                           # Data slot number to use (1 through 30)
name_humi = "Inside Humidity DHT11"      # Descriptive name for your device, put '+' for space char
slot_temp_f = 23
name_temp_f = "Inside Temp F"

# Sensor settings
dht11_port = 8                           # DHT22 temp & humidity sensor is connected to port D8

# Other global variables
baseurl = "http://piland.socialdevices.io"
temp_baseurl = baseurl + "/" + str(room) + "/write/" + str(slot_temp) + "?name=" + name_temp + "&value="
tempf_baseurl = baseurl + "/" + str(room) + "/write/" + str(slot_temp_f) + "?name=" + name_temp_f + "&value="
humi_baseurl = baseurl + "/" + str(room) + "/write/" + str(slot_humi) + "?name=" + name_humi + "&value="

while True:
  
  try:

    # Read the temperature and humidity

    [temp, humi] = grovepi.dht(dht11_port, 0)               # second parameter:  0 = DHT22 sensor

    temp_url = temp_baseurl + "%0.1f" % temp + "+C"
    humi_url = humi_baseurl + "%0.1f" % humi  + "+%25"      #  %25 will display as % sign
    tempf_url = tempf_baseurl + "%0.1f" % (temp*1.8+32) + "+F"

    print temp_url
    print humi_url
    print tempf_url

    requests.get(temp_url)    # write data
    requests.get(humi_url)    # write data
    requests.get(tempf_url)

    time.sleep(2.0)           # 2 second delay

  except KeyboardInterrupt:
    print "Terminating"
    break
  except IOError:
    print "IOError, continuing"
  except:
    print "Unexpected error, continuing"

