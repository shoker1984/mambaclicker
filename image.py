#! /usr/bin/python3

import pyautogui as pg
import cv2
import numpy as np
import time, os
import tkinter as tk
import time
from sys import argv


def main():
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

            img = pg.screenshot(region=(749, 340, 430, 159))
            img.save('s3.png')
            img = pg.screenshot(region=(1341, 966, 132, 36))
            img.save('s.png')
            img = pg.screenshot(region=(987, 552, 267, 146))
            img.save('s4.png')
            img = pg.screenshot(region=(618, 289, 64, 63))
            img.save('s5.png')
            img = pg.screenshot(region=(988, 539, 254, 93))
            img.save('s6.png')

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

            elif np.equal(np.array(cv2.imread('res/scsh4.png', cv2.IMREAD_GRAYSCALE)),
                          np.array(cv2.imread('s4.png', cv2.IMREAD_GRAYSCALE))).all():
                pg.press('left')
            elif np.equal(np.array(cv2.imread('res/scsh4.png', cv2.IMREAD_GRAYSCALE)),
                          np.array(cv2.imread('s4.png', cv2.IMREAD_GRAYSCALE))).all():
                pg.press('left')
            elif np.equal(np.array(cv2.imread('res/scsh5.png', cv2.IMREAD_GRAYSCALE)),
                          np.array(cv2.imread('s5.png', cv2.IMREAD_GRAYSCALE))).all():
                pg.press('left')
            elif np.equal(np.array(cv2.imread('res/scsh6.png', cv2.IMREAD_GRAYSCALE)),
                          np.array(cv2.imread('s6.png', cv2.IMREAD_GRAYSCALE))).all():
                pg.press('left')

            # os.remove('s3.png')
            # os.remove('s.png')
            time.sleep(.5)
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
