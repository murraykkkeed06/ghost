import ctypes
import os


dirpath = os.path.dirname(os.path.realpath(__file__))

path = dirpath + '\img\desktop.jpg'

ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
