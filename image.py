#! /usr/bin/python3
    
import pyautogui as pg
import time
from sys import argv


def main():
    time.sleep(3)
    start = time.time()
    counter = int(argv[1])
    run = True
    while run:  
        if counter == 0:
            run = False
        elif pg.locateOnScreen('res/scsh3.png', region=(749, 340, 430, 159), confidence=.8):
                pg.press('esc')
        elif pg.locateOnScreen('res/scsh.png', region=(1341, 966, 132, 36), confidence=.8):
            counter -= 1
            pg.press('right')
            print(f"Осталось {counter}")
        elif (pg.locateOnScreen('res/scsh4.png', region=(987, 552, 267, 146), confidence=.8) 
              or pg.locateOnScreen('res/scsh5.png', region=(618, 289, 64, 63), confidence=.8) 
              or pg.locateOnScreen('res/scsh6.png', region=(988, 539, 254, 93), confidence=.8)): 
            pg.press('left')
        
    print(f'Времени затрачено {int((time.time() - start)/60)} минут и {int((time.time() - start)%60)} секунд,\nвсего {int((time.time() - start))/int(argv[1])} секунд на анкету')
    
    
if __name__ == '__main__':
    main()
