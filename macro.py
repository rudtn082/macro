from PIL import Image, ImageGrab
import pytesseract
import time
import pyperclip
import pyautogui

#=== Please fix following===

x1 = 1019
y1 = 576

width = 75
height = 30

emptyBoxX = 1018
emptyBoxY = 623
#===========================vv

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR/tesseract.exe'

time.sleep(2)

while True:
    pyautogui.click(263,453, interval=0.5)
    ImageGrab.grab(bbox=(x1, y1, x1 + width, y1 + height)).save("capture.png", "png")
    txt = pytesseract.image_to_string(Image.open('capture.png'))
    pyperclip.copy(txt)
    pyautogui.click(emptyBoxX, emptyBoxY, interval=0.2)
    pyautogui.hotkey('ctrl','v', interval=0.2)
    pyautogui.press('enter', interval=0.5)
    pyautogui.press('enter', interval=0.5)





