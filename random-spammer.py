import pyautogui as auto
from time import sleep
import random

a = auto.prompt()
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
print("Spam go brrrrrrrrrr")

while True:
    loll = random.randint(1, 100)
    lol = random.randint(1, 100)
    auto.typewrite(str(f"[{loll}] {a} [{lol}]"))
    auto.press('enter')
