#! /usr/bin/python3
    
import pyautogui as pg
import cv2
import numpy as np
import time, os
import tkinter as tk
from sys import argv

counter = int(argv[1])
def main():
    time.sleep(3)
    start = time.time()
    # counter = int(argv[1])
    global counter
    run = True
    while run:
        
        scsh3 = pg.screenshot('s3.png', region=(749, 340, 430, 159))
        scsh = pg.screenshot('s.png', region=(1341, 966, 132, 36))
        
        if counter == 0:
            run = False

        elif np.equal(np.array(cv2.imread('res/scsh.png', cv2.IMREAD_GRAYSCALE)), np.array(cv2.imread('s.png', cv2.IMREAD_GRAYSCALE))).all():
            if np.equal(np.array(cv2.imread('res/scsh3.png', cv2.IMREAD_GRAYSCALE)), np.array(cv2.imread('s3.png', cv2.IMREAD_GRAYSCALE))).all():
                pg.press('esc')
            counter -= 1
            pg.press('right')
            print(f"Осталось {counter}")

        elif (pg.locateOnScreen('res/scsh4.png', region=(987, 552, 267, 146), confidence=.8) 
              or pg.locateOnScreen('res/scsh5.png', region=(618, 289, 64, 63), confidence=.8) 
              or pg.locateOnScreen('res/scsh6.png', region=(988, 539, 254, 93), confidence=.8)): 
            pg.press('left')
        
        os.remove('s3.png')
        os.remove('s.png')
        
    print(f'Времени затрачено {int((time.time() - start)/60)} минут и {int((time.time() - start)%60)} секунд,\nвсего {int((time.time() - start))/int(argv[1])} секунд на анкету')

def win():
    global counter
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.geometry('100x100')
    root.resizable(False, False)
    lb = tk.Label(text=f'{counter}')
    btn = tk.ttk.Button(text='start', command=main)
    lb.pack(expand=True)
    btn.pack()
    root.update()
    root.mainloop()
    
if __name__ == '__main__':
    win()
