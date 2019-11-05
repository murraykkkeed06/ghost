import pyautogui
import os
from time import sleep

#pyautogui.position()


#pyautogui.moveTo(100,100,2)


#button7location = pyautogui.locateOnScreen('calc7key.png')
#print(button7location[0])

filepath = os.path.dirname(os.path.realpath(__file__))	

#print(filepath+'img/close.png')

while True:

	try:
		rebtn = pyautogui.locateOnScreen(filepath + 
'\img\close.png',confidence=0.9)

		x = rebtn[0]
		y = rebtn[1]

		pyautogui.moveTo(x,y,2)

		pyautogui.click()
	except:
	
		print("no remove button found")




#rebtn = pyautogui.locateOnScreen(filepath+'\img\close.png',confidence=0.9)
#print(filepath)

#print("test")
