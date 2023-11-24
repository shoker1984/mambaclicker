#! /usr/bin/python3
    
import pyautogui as pg
import time
from sys import argv


time.sleep(3)
run = True
start = time.time()
counter = int(argv[1])
while run:
    if pg.locateOnScreen('res/scsh2.png') or counter == 0:
        run = False
    elif pg.locateOnScreen('res/scsh.png', region=(1345, 965, 124, 38), confidence=.2):
       if pg.locateOnScreen('res/scsh3.png', region=(749, 340, 430, 159), confidence=.3):
             pg.press('esc')
       counter -= 1
       pg.press('right')
       print(f"Осталось {counter}")
    elif pg.locateOnScreen('res/scsh3.png', confidence=.9):
       pg.press('esc')
    else: pg.press('left')
print(f'Времени затрачено {int((time.time() - start)/60)} минут и {int((time.time() - start)%60)} секунд,\nвсего {int((time.time() - start))/int(argv[1])} секунд на анкету')

