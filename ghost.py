import pyautogui

pyautogui.position()


#pyautogui.moveTo(100,100,2)


#button7location = pyautogui.locateOnScreen('calc7key.png')
#print(button7location[0])

try:
	rebtn = pyautogui.locateOnScreen('img/close.PNG',confidence=0.9)

	x = rebtn[0]
	y = rebtn[1]

	pyautogui.moveTo(x,y,2)

	pyautogui.click()
except:
	
	print("no remove button found")



#rebtn = pyautogui.locateOnScreen('img/close.PNG',confidence=0.9)
