import time
import keyboard
import pyautogui
import win32api, win32con
import auto_gifter

def click(x: int, y: int):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def get_center(region):
    return region.left + region.width // 2, region.top + region.height // 2

def click_image(image_path: str, confidence=0.75, region=None, double_click=False) -> bool:
    region = pyautogui.locateOnScreen(image_path, confidence=confidence, grayscale=True, region=region)
    if region is not None:
        center_x, center_y = get_center(region)
        if double_click:
            pyautogui.click(center_x, center_y)
            pyautogui.click(center_x, center_y)
        else:
            pyautogui.click(center_x, center_y)
        return True
    return False

def wait_for_image(image_path: str, confidence=0.75, timeout=5, region=None) -> bool:
    start_time = time.time()
    while time.time() - start_time < timeout:
        region = pyautogui.locateOnScreen(image_path, confidence=confidence, grayscale=True, region=region)
        if region is not None:
            return True
    return False

def discard_item():
    discard_button = "auto_gifter_images/discard.png"
    confirm_discard = "auto_gifter_images/discard_button.png"
    if click_image(discard_button, confidence=0.75):
        time.sleep(0.3)  # Allow game to catch up
        click_image(confirm_discard, confidence=0.60)
        time.sleep(0.3)  # Allow game to catch up
        return True
    return False

def Bag_cleaner():
    inventory_region = (1225, 270, 1300, 1350)
    bag_is_full = pyautogui.locateOnScreen("auto_gifter_images/bag_is_full2.png", confidence=0.60, grayscale=True, region=(50, 700, 600, 300))                     
    
    if bag_is_full is not None:
        print("Bag is full detected!")
        keyboard.press("i")
        time.sleep(0.5)  # Allow game to catch up

        items = ["auto_gifter_images/beast.png", "auto_gifter_images/cloth.png", "auto_gifter_images/mana.png",
                 "auto_gifter_images/metal_type1.png", "auto_gifter_images/metal_type2.png",
                 "auto_gifter_images/med_mats_type1.png", "auto_gifter_images/med_mats_type2.png",
                 "auto_gifter_images/med_mats_type3.png", "auto_gifter_images/med_mats_type4.png",
                 "auto_gifter_images/med_mats_type5.png", "auto_gifter_images/wood_mats.png"]

        scroll_attempts = 0
        max_scrolls = 4
        
        item_discarded = False

        while scroll_attempts < max_scrolls:
            item_found = False

            for item in items:
                while click_image(item, confidence=0.75, region=inventory_region):
                    time.sleep(0.1)
                    item_found = True
                    item_discarded = True
                    if not discard_item():
                        print("something else went wrong and cant find the discard image!")
                       
                    else:
                        print("successfully discarded an item!")
                        

            if not item_found:
                for i in range(5):  
                    pyautogui.scroll(-100)
                time.sleep(0.5)  # Allow game to catch up after scrolling
                scroll_attempts += 1

        print("Finished checking/discarding all items and scrolling")
        
        if not item_discarded:
            print("rawr")
            
            """start gifting """
            keyboard.press("c")

            click_image("auto_gifter_images/mailbox.png", region=(1300, 1100, 1000, 200))

            auto_gifter.Auto_gifter() #start auto gifting

        
        keyboard.press("Esc") # remove inventory and then continue the autofarmer

        print("CONTINUING AUTOFARMER")


if __name__ == "__main__":
    time.sleep(1)
    Bag_cleaner()






