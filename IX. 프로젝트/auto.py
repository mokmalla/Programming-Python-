#pyAutoGUI
#pop install pyautogui
import time
import pyautogui as pag

if __name__ == '__main__':
    # while True:
    #     x, y = pag.position() #좌표 구하기
    #     print("x : {}\ty : {}".format(x, y), end="\r")
    #pag.moveTo(32,285, duration = 2)   #~까지 이동
    #pag.move(100,200, duration=2)      #~만큼 ㅣㅇ동
    # pag.click()
    # pag.click()
    #pag.click(clicks=2)
    #pag.doubleClick()  #더블클릭
    #pag.dragTo(0,0, duration=2)    #드래그 duration 있어야함
    # pag.click(32,285, duration = 2)
    # pag.rightClick()  #오른쪽 버튼
    pag.doubleClick(32,285, duration=1)
    #TODO: pag.scroll(432,200)
    time.sleep(1) #크롬이 열리기를 기다려야 함
    pag.typewrite("ticket.interpark.com")
    pag.press("enter")
    #pag.press("hangul")    #한/영키
    # pag.typewrite("dkdldb")  #아이유 영어로