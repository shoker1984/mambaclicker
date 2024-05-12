#! /usr/bin/python3

from pyautogui import screenshot, press
from cv2 import imread, IMREAD_GRAYSCALE
from time import sleep, time
from os import remove
from numpy import equal, array
import tkinter as tk
from sys import argv


def main():  # Основная функция
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.geometry('400x400+0+0')
    root.resizable(False, False)
    start_time = time()
    counter = int(argv[1])
    run = False
    lb = (tk.Label(text=f'{counter}'))
    lb.pack(expand=True)

    def start():  # for button
        sleep(2)
        nonlocal run
        nonlocal counter
        nonlocal start_time
        run = not run
        while run:
            root.update()

            img = screenshot(region=(749, 340, 430, 159))
            img.save('s3.png')
            img = screenshot(region=(1341, 966, 132, 36))
            img.save('s.png')
            img = screenshot(region=(987, 552, 267, 146))
            img.save('s4.png')
            img = screenshot(region=(633, 307, 30, 31))
            img.save('s5.png')
            img = screenshot(region=(988, 539, 254, 93))
            img.save('s6.png')

            if counter == 0:
                run = False

            elif equal(array(imread('res/scsh.png', IMREAD_GRAYSCALE)),
                          array(imread('s.png', IMREAD_GRAYSCALE))).all():
                if equal(array(imread('res/scsh3.png', IMREAD_GRAYSCALE)),
                            array(imread('s3.png', IMREAD_GRAYSCALE))).all():
                    press('esc')
                counter -= 1
                lb['text'] = f'{counter}'
                press('right')

            elif equal(array(imread('res/scsh4.png', IMREAD_GRAYSCALE)),
                          array(imread('s4.png', IMREAD_GRAYSCALE))).all():
                press('left')
            elif equal(array(imread('res/scsh5.png', IMREAD_GRAYSCALE)),
                          array(imread('s5.png', IMREAD_GRAYSCALE))).all():
                press('left')
            elif equal(array(imread('res/scsh6.png', IMREAD_GRAYSCALE)),
                          array(imread('s6.png', IMREAD_GRAYSCALE))).all():
                press('left')
            
            remove('s.png')
            remove('s3.png')
            remove('s4.png')
            remove('s5.png')
            remove('s6.png')
            
            sleep(.4)
        lb['text'] = (
        f'Времени затрачено {int((time() - start_time) / 60)} минут и '
        f'{int((time() - start_time) % 60)} секунд,'
        f'\nвсего {int((time() - start_time)) / int(argv[1])} секунд на анкету')

    btn = (tk.Button(text='start', command=start))
    btn.pack()

    lb['text'] = 'Нажмите старт'

    root.mainloop()


if __name__ == '__main__':
    main()
