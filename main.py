import pyautogui, time

def rightswipe(xc,yc):
	pyautogui.click(x=xc, y=yc, button='left')

x = 1

while(x == 1):
	rightswipe(975, 665)
	time.sleep(0.25)
	pyautogui.press('esc')
