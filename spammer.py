import pyautogui as auto
from time import sleep

spam = input("Enter what you want to spam: ")
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
print("Spam go brrrrrrrrrr")

while True:
    auto.write(spam)
    auto.press('enter')