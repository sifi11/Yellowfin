import pyautogui
import datetime

def grab_screen():
    try:
        file_name = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

        image = pyautogui.screenshot()

        image.save(file_name)

        return file_name

    except Exception as e:
        return None


# file = grab_screen()
