from tkinter import *
from PIL import ImageTk, Image
import time
import os
import random

root = Tk()

filepath = os.path.dirname(os.path.realpath(__file__))

numIdx =  12

frames = [PhotoImage(file=filepath+'\img\ghost4.gif', format='gif -index %i' %(i)) for i in range(numIdx+1)]

#frames = [PhotoImage(file='abc.gif', format='gif -index %i' %(i)) for i in range(numIdx)]

def update(idx): # 定时器函数
	frame = frames[idx]
	idx += 1 # 下一帧的序号：在0,1,2,3,4,5之间循环(共6帧)
	label.configure(image=frame) # 显示当前帧的图片
	#root.geometry("680*382")
	#root.geometry("+400+100")
	#root.geometry("+"+str(random.randint(1,1201))+"+"+str(random.randint(1,401)))
	#time.sleep(random.randint(0,1))
	#pos = pos + 1
	root.after(100, update, idx%numIdx) # 0.1秒(100毫秒)之后继续执行定时器函数(update)
	

#root.attributes('-alpha',0.1)

root.overrideredirect(True)

root.wm_attributes("-topmost",True)

root.geometry("+800+400")

label = Label(root)

label.pack()

root.after(0, update, 0) # 立即启动定时器函数(update)


time.sleep(6)

root.mainloop()
