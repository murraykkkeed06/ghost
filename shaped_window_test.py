from tkinter import *
from PIL import ImageTk, Image
import time
import os
import random

root = Tk()

#pos_int = 1600
#img = ImageTk.PhotoImage(Image.open("girlcrying.gif"))

#img = PhotoImage(file='girlcrying.gif')

numIdx = 6

frames = [PhotoImage(file='girlcrying.gif', format='gif -index %i' %(i)) for i in 
range(numIdx)]

#frame2 = PhotoImage(file=imagefilename, format="gif -index 2")

#panel = Label(root, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")

#root.wait_visibility(root)



def update(idx): # 定时器函数
	frame = frames[idx]
	idx += 1 # 下一帧的序号：在0,1,2,3,4,5之间循环(共6帧)
	label.configure(image=frame) # 显示当前帧的图片
	root.geometry("+"+str(random.randint(1,1201))+"+"+str(random.randint(1,401)))
	#pos = pos + 1
	root.after(100, update, idx%numIdx) # 0.1秒(100毫秒)之后继续执行定时器函数(update)
	#root.geometry("+" + str(pos_int) + "+200")
	#pos_int = pos_int -1
	#if pos_int<0:
	#	pos_int = 1600	
	#root.after(100,update, idx%numIdx)

root.attributes('-alpha',0.1)

root.overrideredirect(True)

root.wm_attributes("-topmost",True)

'''
pos_int = 1600

while pos_int>0:
	pos_int = pos_int - 1
	root.geometry("+" + str(pos_int) + "+200")
''' 
#root.geometry("+400+200")

label = Label(root)
label.pack()
root.after(0, update, 0) # 立即启动定时器函数(update)


#panel = Label(root, image = img)

#panel.pack(side = "bottom", fill = "both", expand = "yes")

#root.wait_visibility(root)

root.mainloop()
