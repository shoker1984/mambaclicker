#! /usr/bin/python3
    
import pyautogui as pg
from PyQt6 import QtWidgets, uic, QtCore
import time
import form1
from sys import argv

class MainForm(QtWidgets.QMainWindow, form1.Ui_Form):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

def main():
    time.sleep(3)
    run = True
    start = time.time()
    counter = int(argv[1])
    # app = QtWidgets.QApplication(argv)
    # win = MainForm()
    # win.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)
    # win.lb_count.setText(str(counter))
    # win.show()
    # app.exec()
    while run:
        
        if counter == 0:
            run = False
        elif pg.locateOnScreen('res/scsh3.png', region=(749, 340, 430, 159), confidence=.8):
                pg.press('esc')
        elif pg.locateOnScreen('res/scsh.png', region=(1341, 966, 132, 36), confidence=.8):
            counter -= 1
            pg.press('right')
            print(f"Осталось {counter}")
        # elif pg.locateOnScreen('res/scsh3.png', confidence=.9):
            #    pg.press('esc')
        # elif pg.locateOnScreen('res/scsh3.png', region=(749, 340, 430, 159), confidence=.8):
        #          pg.press('esc')
        
        elif pg.locateOnScreen('res/scsh4.png', region=(987, 552, 267, 146), confidence=.8) or pg.locateOnScreen('res/scsh5.png', region=(618, 289, 64, 63), confidence=.8) or pg.locateOnScreen('res/scsh6.png', region=(988, 539, 254, 93), confidence=.8): 
            pg.press('left')
            # counter -= 1
        # win.lb_count.setText(str(counter))
        
    print(f'Времени затрачено {int((time.time() - start)/60)} минут и {int((time.time() - start)%60)} секунд,\nвсего {int((time.time() - start))/int(argv[1])} секунд на анкету')
    
    
if __name__ == '__main__':
    main()