import time
import pyautogui as pag

if __name__ == '__main__':
    DATA = pag.locateOnScreen("chrome.PNG")
    print(DATA)
    center = pag.center(DATA)
    print(center)
    pag.moveTo(center, duration=2)
    pag.doubleClick()