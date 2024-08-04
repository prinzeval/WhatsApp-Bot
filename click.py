import pyautogui
import time

print("Move your mouse to the 'Save as' menu option in the context menu within 5 seconds...")
time.sleep(5)
print(pyautogui.position())
