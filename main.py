import pyautogui as pag
import time

time.sleep(5)
text = 'hello'
times = 10
for i in range(times):
    pag.write(f'{text}')
    pag.press('Enter')
    time.sleep(0.5)
