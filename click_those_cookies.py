# Attempts to auto-click certain Cookie Clicker items:
# - The big cookie
# - The item that causes the golden cookie to appear
# - The golden cookie

import itertools
import os
from time import sleep

import pyautogui


def locate_item(item):
    clicks_ = {
        "cookie_big.png": 8_000,
        "cookie_bonus.png": 2,
    }

    old_loc = pyautogui.position()
    new_loc = pyautogui.locateOnScreen(f"./data/{item}", grayscale=True, )
    if new_loc is not None:
        loc = new_loc[0]/2, new_loc[1]/2
        pyautogui.click(loc, clicks=clicks_.get(item, 0), interval=0.005)
        pyautogui.moveTo(old_loc[0], old_loc[1])

    sleep(1)


if __name__ == "__main__":
    items = [item for item in os.listdir('./data') if item.endswith(".png")]

    for item in itertools.cycle(items):
        locate_item(item)
