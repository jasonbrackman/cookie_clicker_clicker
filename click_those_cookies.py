# Attempts to auto-click certain Cookie Clicker items:
# - The big cookie
# - The item that causes the golden cookie to appear
# - The golden cookie

import itertools
import os

import pyautogui


def locate_item(item):
    clicks_ = {
        "cookie_big.png": 4000,
        "cookie_golden.png": 2,
        "cookie_cause_golden.png": 1,
    }

    old_loc = pyautogui.position()
    new_loc = pyautogui.locateOnScreen(f"./data/{item}", grayscale=True, )
    new_loc = new_loc if new_loc is not None else (254, 884)

    loc = new_loc[0]/2, new_loc[1]/2
    pyautogui.click(loc, clicks=clicks_.get(item, 4_000), interval=0.007)
    pyautogui.moveTo(old_loc[0], old_loc[1])


if __name__ == "__main__":
    items = [item for item in os.listdir('./data') if item.endswith(".png")]

    for item in itertools.cycle(items):
        locate_item(item)
