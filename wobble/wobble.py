import pyautogui, time, random
# disables failsafe mode to prevent program from crashing if screen is locked
pyautogui. FAILSAFE = False
while True:
    x = random.randint(100,900)
    y = random.randint(100,900)
    pyautogui.moveTo(x,y,3)
    time.sleep(1)
