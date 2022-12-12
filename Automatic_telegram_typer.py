import pyautogui
import time
time.sleep(4)
count=0
while count <=1000:
    pyautogui.typewrite("Hello")
    pyautogui.press("enter")
    count=count+1
