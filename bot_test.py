import pyautogui
import time
import random

def move_mouse():
    while True:
        # Get current mouse position
        x, y = pyautogui.position()

        # Move slightly in a random direction
        dx = random.randint(-10, 10)
        dy = random.randint(-10, 10)
        pyautogui.moveTo(x + dx, y + dy, duration=0.2)

        print(f"Moved mouse to ({x + dx}, {y + dy})")

        # Wait for 60 seconds
        time.sleep(60)

if __name__ == "__main__":
    print("Mouse mover bot started. Press Ctrl+C to stop.")
    move_mouse()