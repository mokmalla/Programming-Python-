import time
import pyautogui as pag

if __name__ == '__main__':
    #메모장 프로그램 실행하자
    pag.doubleClick(315, 750)
    time.sleep(1)

    #hell world 치자
    pag.typewrite("hello world")

    #두 줄 내리자
    pag.press("enter")
    pag.press("enter")

    #반갑구나 세상아 치자
    pag.press("hangul")
    pag.typewrite("qksrkqrnsk tptkddk")

    #helloworld 저장하자
    pag.hotkey("ctrl", "s")
    # pag.press("hangul")
    pag.typewrite("vkdlTjs dPwp")
    pag.press("enter")