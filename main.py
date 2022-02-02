import sys
import time

import cv2
import pyautogui
from PIL import ImageGrab

import action

# 检测系统
print("操作系统:", sys.platform)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pyautogui.FAILSAFE = False

    # 捕获窗口
    action.find_windows()
    # 获取关键图
    imgs = action.load_imgs()

    # 对相应关键图操作鼠标点击进行操作
    # while pyautogui.locateCenterOnScreen(imgs["ddtubiao"]) is None:
    #     continue
    # else:
    #     sop = pyautogui.locateCenterOnScreen(imgs["ddtubiao"])
    #     pyautogui.moveTo(sop)
    #     pyautogui.click(clicks=5, interval=1)
    #
    # while pyautogui.locateCenterOnScreen(imgs["kaishiyemian"]) is None:
    #     continue
    # else:
    #     sop = pyautogui.locateCenterOnScreen(imgs["kaishiyemian"])
    #     pyautogui.moveTo(sop)
    #     pyautogui.click(clicks=3, interval=1)
    #
    # while pyautogui.locateCenterOnScreen(imgs["chujianniu"]) is None:
    #     continue
    # else:
    #     sop = pyautogui.locateCenterOnScreen(imgs["chujianniu"])
    #     pyautogui.moveTo(sop)
    #     pyautogui.click()
    #
    # while pyautogui.locateCenterOnScreen(imgs["huodong"]) is None:
    #     continue
    # else:
    #     sop = pyautogui.locateCenterOnScreen(imgs["huodong"])
    #     pyautogui.moveTo(sop)
    #     pyautogui.click()
    while True:
        while pyautogui.locateCenterOnScreen(imgs["jiangli4"]) is None:
            continue
        else:
            sop = pyautogui.locateCenterOnScreen(imgs["jiangli4"])
            pyautogui.moveTo(sop)
            pyautogui.click(clicks=12, interval=1)

        while pyautogui.locateCenterOnScreen(imgs["zhuisui"]) is None:
            continue
        else:
            sop = pyautogui.locateCenterOnScreen(imgs["no"])
            pyautogui.moveTo(sop)
            pyautogui.click()

        while pyautogui.locateCenterOnScreen(imgs["chuji1"]) is None:
            continue
        else:
            sop = pyautogui.locateCenterOnScreen(imgs["yes"])
            pyautogui.moveTo(sop)
            pyautogui.click()
        time.sleep(60)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
