import pymouse, pykeyboard, os, sys
from pymouse import *
from pykeyboard import PyKeyboard

# 操作鼠标键盘事件练习

mouse = PyMouse()
keyboard = PyKeyboard()

print(mouse.position()) # 可获取鼠标当前坐标

# mouse.click(646,35, n=2) # 点击， n点击次数

mouse.click(646, 341)
# keyboard.type_string('hhhhhhhhh')
keyboard.press_key('a')
