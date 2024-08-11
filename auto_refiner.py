import pyautogui
import time
import keyboard

def get_center(region):
    return region.left + region.width // 2, region.top + region.height // 2

def click_image(image_path:str, confidence=0.75, sleep_duration=0.5, region=None) -> bool :
    region = pyautogui.locateOnScreen(image_path, confidence=confidence, grayscale=True, region=region)
    if region is not None:
        center_x, center_y = get_center(region)
        pyautogui.click(center_x, center_y)
        time.sleep(sleep_duration)
        return True
    return False

def auto_refiner():
    keyboard.press("p")
    time.sleep(0.5)  # Adjust the sleep duration based on actual needs

    if not click_image("auto_refine_images/char_skills.png", confidence=0.95):
        return  # Exit if char skills image is not found

    if not click_image("auto_refine_images/use_ex_skills.png", confidence=0.85):
        return  # Exit if ex skills image is not found

    if not click_image("auto_refine_images/smith_skills.png", confidence=0.75):
        return  # Exit if smith skills image is not found

    if not click_image("auto_refine_images/refine_eq.png", confidence=0.75):
        return  # Exit if refine equipment image is not found

    while True:
        if not click_image("auto_refine_images/mithril_ore.png", confidence=0.75):
            print("You have run out of ores!")
            break

        if not click_image("auto_refine_images/equipment_to_refine.png", confidence=0.75):
            break

        if not click_image("auto_refine_images/dont_use.png", confidence=0.75):
            break

        while True:
            if not click_image("auto_refine_images/start_refinement.png", confidence=0.75):
                break

            time.sleep(4.8)  # Adjust based on the actual refinement time

            if click_image("auto_refine_images/complete.png", confidence=0.75, sleep_duration=1):
                continue  # Go to the next refinement
            else:
                break  # Exit if the refinement is not complete
if __name__ == "__main__":
    time.sleep(2) #switching tabsp
    auto_refiner()




