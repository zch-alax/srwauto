import random
import time

import cv2, os, win32gui
import numpy
import pyautogui
import win32con
import win32ui
from PIL import ImageGrab, Image


# 按【文件内容，匹配精度，名称】格式批量聚聚要查找的目标图片，精度统一为0.95，名称为文件名
def load_imgs():
    mubiao = {}
    path = os.getcwd() + '/png'
    file_list = os.listdir(path)
    for file in file_list:
        name = file.split('.')[0]
        file_path = path + '/' + file
        # a = [cv2.imread(file_path), 0.95, name]
        mubiao[name] = file_path
    return mubiao


# 随机偏移坐标，防止游戏的外挂检测。p是原坐标(x, y)，w、n是目标图像宽高，返回目标范围内的一个随机坐标
def random_offset(p, w=40, h=20):
    a, b = p
    w, h = int(w / 3), int(h / 3)
    c, d = random.randint(-w, w), random.randint(-h, h)
    e, f = a + c, b + d
    y = [e, f]
    return y


# 随机延迟点击，防止游戏外挂检测，延迟时间范围为【x, y】秒之间
def random_delay(x=0.1, y=0.2):
    t = random.uniform(x, y)
    time.sleep(t)

def find_windows():
    srw_windows = win32gui.FindWindow(0, "BlueStacks")
    win32gui.SetForegroundWindow(srw_windows)

