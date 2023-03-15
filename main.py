import cv2 as cv
import numpy as np
import os
import time
import pyautogui
from windowcapture import WindowCapture
from vision import Vision
from random import randint
import pydirectinput

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture('Pangea')
# initialize the Vision class
vision_limestone = Vision('piec.png')
one_limestone = Vision('jeden.png')
two_limestone = Vision('dwa.png')
three_limestone = Vision('trzy.png')
four_limestone = Vision('cztery.png')

def fishing(number):
    i = 0
    while i < number:
        i += 1
        pydirectinput.keyDown('space')
        time.sleep(0.1)
        pydirectinput.keyUp('space')
        ran = randint(100, 200)
        sleeptime = ran / 1000
        time.sleep(sleeptime)
    time.sleep(8.5)
    timesleep = randint(100, 200)
    time.sleep(timesleep / 100)
    pydirectinput.press('f2')
    timesleep2 = randint(240, 350)
    time.sleep(timesleep2 / 1000)
    pydirectinput.press('space')

'''
# https://www.crazygames.com/game/guns-and-bottle
wincap = WindowCapture()
vision_gunsnbottle = Vision('gunsnbottle.jpg')
'''
loop_time = time.time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    # display the processed image
    five = vision_limestone.find(screenshot, 0.94, 'rectangles')
    one = one_limestone.find(screenshot,0.94,'rectangles')
    two = two_limestone.find(screenshot, 0.94, 'rectangles')
    three = three_limestone.find(screenshot, 0.94, 'rectangles')
    four = four_limestone.find(screenshot, 0.94, 'rectangles')
    if one != []:
        time.sleep(randint(250,500)/1000)
        fishing(1)
    if two != []:
        time.sleep(randint(250,500)/1000)
        fishing(2)
    if three != []:
        time.sleep(randint(250,500)/1000)
        fishing(3)
    if four != []:
        time.sleep(randint(250,500)/1000)
        fishing(4)
    if five != []:
        time.sleep(randint(250,500)/1000)
        fishing(5)
    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')

    # debug the loop rate
    #print('FPS {}'.format(1 / (time.time() - loop_time)))
    loop_time = time.time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')








