

import requests
import random
from random import randint
import time
import re
def hex_generator(ints):	
	hex_maker="a:b:c:d:e:f:0:1:2:3:4:5:6:7:8:9"
	
	hex_array=[]
	hex_splitter=hex_maker.split(":")
	
				
	for hex in range(ints):
		hex_picker = randint(0,len(hex_splitter)-1)
		hex_array.append(hex_splitter[hex_picker])
			
	return "".join(hex_array)
print("How many times do you want the URL to be tested?")
		
times = input(">>> ")
while not times.isdigit():
	times =input(">>> ")


cached_strings = []
sleep_time = []
for recursive in range(int(times)):
	hex_string = hex_generator(16)
	cached_strings.append(hex_string)
	recursive +=1
	print("Cached Hex Values ["+str(recursive)+"/"+str(times)+"]")
	if(int(recursive) == int(times)):
		print("Delay between each request\nRange: 0-100")
		sleep = input(">>> ")
		while not sleep.isdigit():
			sleep = input(">>> ")
		if(int(sleep) > 100):
			print("Input must be less than 100")
			sleep = input(">>> ")
		sleep_time.append(sleep)
i = 0
for separate in cached_strings:
	i +=1
	
	delay = "".join(sleep_time)
	delay = int(delay)
	
	r = requests.get('http://logs.omegle.com/'+separate)
	print("["+str(i)+"/"+str(len(cached_strings))+"]http://logs.omegle.com/"+separate+" : "+str(r.status_code))
	time.sleep(delay)
	
