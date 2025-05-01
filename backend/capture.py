import pyautogui
import datetime
from PIL import Image

def capture_screen(filename="screenshot.png", size = (960,540)):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"screenshots/{filename.split('.')[0]}_{timestamp}.png"
    screenshot = pyautogui.screenshot()
    screenshot_resized = screenshot.resize(size, Image.LANCZOS)
    screenshot_resized.save(path)
    return path

if __name__ == "__main__":
    capture_screen()