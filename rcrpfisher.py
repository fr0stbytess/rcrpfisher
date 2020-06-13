import sys
import time
import pyautogui as fisher

fishing_status = True


def fishing():
    tries = 5
    try:
        while fishing_status:
            if tries == 0:
                tries = 5
                collect_fish()
            fisher.press("T")
            fisher.typewrite("/fish")
            fisher.press("enter")
            tries -= 1
            time.sleep(17)  # cooldown so shit won't spam out and alert admins

    except KeyboardInterrupt:
        sys.exit()
        print("Stopped.")

def collect_fish():
    fisher.press("T")
    fisher.typewrite("/fcrate store all")  # stores fishes for peace
    fisher.press("enter")

fishing()
