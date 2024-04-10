#! /usr/bin/python3

import pyautogui as pg
import cv2
import numpy as np
import time, os
import tkinter as tk
import time
from sys import argv


def main(): #Основная функция
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.geometry('400x400+0+0')
    root.resizable(False, False)
    # time.sleep(3)
    start_time = time.time()
    counter = int(argv[1])
    run = False
    lb = (tk.Label(text=f'{counter}'))
    lb.pack(expand=True)

    def start():  # for button
        time.sleep(2)
        nonlocal run
        nonlocal counter
        nonlocal start_time
        run = True
        while run:
            root.update()

            pg.screenshot('s3.png', region=(749, 340, 430, 159))
            pg.screenshot('s.png', region=(1341, 966, 132, 36))

            if counter == 0:
                run = False

            elif np.equal(np.array(cv2.imread('res/scsh.png', cv2.IMREAD_GRAYSCALE)),
                          np.array(cv2.imread('s.png', cv2.IMREAD_GRAYSCALE))).all():
                if np.equal(np.array(cv2.imread('res/scsh3.png', cv2.IMREAD_GRAYSCALE)),
                            np.array(cv2.imread('s3.png', cv2.IMREAD_GRAYSCALE))).all():
                    pg.press('esc')
                counter -= 1
                lb['text'] = f'{counter}'
                pg.press('right')

            elif (pg.locateOnScreen('res/scsh4.png', region=(987, 552, 267, 146), confidence=.8)
                  or pg.locateOnScreen('res/scsh5.png', region=(618, 289, 64, 63), confidence=.8)
                  or pg.locateOnScreen('res/scsh6.png', region=(988, 539, 254, 93), confidence=.8)):
                pg.press('left')

            os.remove('s3.png')
            os.remove('s.png')
        lb['text'] = (
            f'Времени затрачено {int((time.time() - start_time) / 60)} минут и '
            f'{int((time.time() - start_time) % 60)} секунд,'
            f'\nвсего {int((time.time() - start_time)) / int(argv[1])} секунд на анкету')

    btn = (tk.Button(text='start', command=start))
    btn.pack()

    lb['text'] = 'Нажмите старт'

    root.mainloop()


if __name__ == '__main__':
    main()
