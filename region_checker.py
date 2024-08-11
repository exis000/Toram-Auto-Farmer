
import pyautogui
import cv2
import numpy as np
import time
import win32api, win32con

# def fast_scroll(amount):
#     win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, amount, 0)

# time.sleep(2)
# for i in range(5):  # 5 for mid, 7 for 3/4, and 10 for scroll lowest
#     pyautogui.scroll(-100)

# time.sleep(1)
# for i in range(5):  # 5 for mid, 7 for 3/4, and 10 for scroll lowest
#     pyautogui.scroll(-100)
# # time.sleep(1)
# # for i in range(5):  # 5 for mid, 7 for 3/4, and 10 for scroll lowest
# #     pyautogui.scroll(-100)
    
def show_region(region):
    # region should be a tuple: (left, top, width, height)
    left, top, width, height = region

    # Take a screenshot of the specified region
    screenshot = pyautogui.screenshot(region=region)

    # Convert the screenshot to a format OpenCV can work with (numpy array)
    screenshot_np = np.array(screenshot)

    # Convert RGB to BGR (OpenCV uses BGR by default)
    screenshot_np = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    # Draw a rectangle around the region
    cv2.rectangle(screenshot_np, (0, 0), (width, height), (0, 255, 0), 2)

    # Display the screenshot with the region highlighted
    cv2.imshow("Region Checker", screenshot_np)
    
    # Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    time.sleep(2)
    # Example region (left, top, width, height)
    region = (750, 1250, 1000, 200)
    
    # Show the region
    show_region(region)
