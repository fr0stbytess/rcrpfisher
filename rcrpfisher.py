import sys
import time
import pyautogui as fisher

fishing = True


def Fishing():
    tries = 5
    try:
        while fishing:
            if tries == 0:
                tries = 5
                CollectFish()
            fisher.press("T")
            fisher.typewrite("/fish")
            fisher.press("enter")
            tries -= 1
            time.sleep(17)  # cooldown so shit won't spam out and alert admins

    except KeyboardInterrupt:
        sys.exit()
        print("Stopped.")


def CollectFish():
    fisher.press("T")
    fisher.typewrite("/fcrate store all")  # stores fishes for peace
    fisher.press("enter")

Fishing()
