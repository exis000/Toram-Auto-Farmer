import pyautogui
import time
import keyboard

def get_center(region):
    """Calculate the center of the image to click."""
    return region.left + region.width // 2, region.top + region.height // 2

def wait_for_image(image_path: str, confidence=0.75, timeout=5, region=None) -> bool:
    """
    Waits for an image to appear on the screen within a specified timeout.
    
    :param image_path: Path to the image file.
    :param confidence: The confidence level to match the image.
    :param timeout: The maximum time to wait for the image (in seconds).
    :param region: The region on the screen to search for the image.
    :return: True if the image is found within the timeout, otherwise False.
    """
    start_time = time.time()
    while time.time() - start_time < timeout: # this checks how much time has elapse and the image is still not found
        region = pyautogui.locateOnScreen(image_path, confidence=confidence, grayscale=True, region=region)
        if region is not None:
            return True
    return False

def click_image(image_path: str, confidence=0.75,region=None, timeout=5, double_click=False, ) -> bool:
    """
    Clicks on an image if found within the timeout.

    :param image_path: Path to the image file.
    :param confidence: The confidence level to match the image.
    :param timeout: The maximum time to wait for the image (in seconds).
    :param double_click: If True, performs a double click.
    :param region: The region on the screen to search for the image.
    :return: True if the image is clicked, otherwise False.
    """
    if wait_for_image(image_path, confidence, timeout, region):#so the waitforimage func comes first to check if its there then this func
        region = pyautogui.locateOnScreen(image_path, confidence=confidence,region=region, grayscale=True,)
        if region is not None:
            center_x, center_y = get_center(region)
            if double_click:
                pyautogui.click(center_x, center_y)
                pyautogui.click(center_x, center_y)
            else:
                pyautogui.click(center_x, center_y)
            return True
    return False

def gift_item():
    selecting_player_to_gift_images = [# str(imagePATH),(CONFIDENCE),(REGION)
        ("auto_gifter_images/send_gift_mail.png", 0.90, (1300, 750, 1000, 200)), 
        ("auto_gifter_images/send_gift_friend.png", 0.75, (800, 1100, 1000, 400)),
        ("auto_gifter_images/player_to_gift.png", 0.75, (800, 1100, 1000, 200)),
        ("auto_gifter_images/select_gift.png", 0.90, (700, 700, 1000, 200))
    ]

    sending_the_summershell_images = [#SAME HERE
        ("auto_gifter_images/max_button.png", 0.90, (1750, 650, 200, 200)),
        ("auto_gifter_images/confirm_select.png", 0.75, (1000, 1000, 700, 200)),
        ("auto_gifter_images/confirm_gift.png", 0.75, (400, 600, 700, 200)),
        ("auto_gifter_images/send_gift.png", 0.90, (750, 1325, 1000, 200)),
        ("auto_gifter_images/click_OK_button.png", 0.75, (750, 1250, 1000, 200))
    ]

    summershell = "auto_gifter_images/summershell.png"

    
    scroll_attempts = 0 # same dito i found out na di naman pala need ng scroll since
    max_scrolls = 3       #nag adjust inventory pag nawala item :pein
    gifting_limit = 100 #idk if need pa to
    gifted_count = 0

    while scroll_attempts < max_scrolls:
        theres_still_summershell = False
        if gifted_count < gifting_limit:
            # Process selecting player to gift images loop in the list 
            for image, confidence, region in selecting_player_to_gift_images:#looping through the tuples and items inside
                if not click_image(image, confidence=confidence, region=region):
                    print(f"Error: {image} not found or an issue occurred")
                    return

            # Check for the summershell and handle gifting
            if click_image(summershell, timeout=1, double_click=True):
                theres_still_summershell = True
                gifted_count += 1
                # Send the summershell
                time.sleep(0.7) #sleep so that the game can catch up
                for img, confidence, region in sending_the_summershell_images:
                    if not click_image(img, confidence=confidence, region=region):
                        print("theres summershell but the image is not found or an error occured")
                        continue #continue if the image is not found when there is summer shell just reset
                time.sleep(1)#sleep so that the game can catch up
            else:
                # Scroll if summershell is not found
                for _ in range(5):
                    pyautogui.scroll(-100)
                    scroll_attempts += 1
                break  # Break out of the inner loop if not found to start the outer loop again

            # Ensure to continue the outer loop if there is no `summershell` found
            if not theres_still_summershell:
                print("No summershell found after scrolling")
                scroll_attempts += 1
                continue  # Continue with the outer while loop

        else:
            print("Gifting limit reached or max scrolls reached")
            break
# Start gifting process

discard_condition = False

if not discard_condition:
    # Start the gifting process
    keyboard.press("c")
    if wait_for_image("auto_gifter_images/mailbox.png", timeout=5):  # Wait for mailbox to appear
        click_image("auto_gifter_images/mailbox.png", timeout=5, region=(1300, 1100, 1000, 200))
        gift_item()