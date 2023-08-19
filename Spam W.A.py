import pyautogui
import time

pyautogui.moveTo(1080,220) #Kordinat Layar
pyautogui.click() #clik Mouse

for i in range(5): #jumlah spamSpam
    pyautogui.write("Spam")
    time.sleep(0.1)
    pyautogui.press("Enter")