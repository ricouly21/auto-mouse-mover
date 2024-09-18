import pyautogui
import time


if __name__ == "__main__":
    interval = 15
    initial_x, initial_y = pyautogui.position()
    while True:
        new_x, new_y = pyautogui.position()
        if new_x == initial_x or new_y == initial_y:
            print(f"Cursor has not moved for the last {interval} seconds ... moving cursor.")
            pyautogui.moveTo(new_x + 1, new_y + 1)
            pyautogui.moveTo(new_x, new_y)
        else:
            print("No action.")
        initial_x, initial_y = new_x, new_y
        time.sleep(interval)
