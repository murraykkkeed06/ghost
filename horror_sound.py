from playsound import playsound
from time import sleep
from random import randint

playlist = ['sound/bone.mp3','sound/grount.mp3','sound/bell.mp3']

while True:
	
	playsound(playlist[randint(0,2)])
	sleep(randint(0,2))
	#playsound('sound/bell.mp3')
