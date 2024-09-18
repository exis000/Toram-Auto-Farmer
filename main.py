import time
import keyboard
import pyautogui

import auto_discard


BUFF_DURATION = 10  # Duration after which buffs are reset (in minutes)
SHORT_BUFF_SLEEP = 1.5  # Short sleep duration for buff casting
LONG_BUFF_SLEEP = 4  # Long sleep duration for buff casting
ACTION_SLEEP = 0.1  # Sleep duration between actions
BACKWARDS_WALK_SLEEP = 0.3  # Sleep duration for walking backwards

def Cast_buff(key: str, Sleep_time: int):
    print(f"Casting buff with key {key} at {time.strftime('%X')}")
    keyboard.press(key)
    time.sleep(Sleep_time)
    keyboard.release(key)

def Auto_farm():
    last_brave_time = 0
    last_quick_motion_time = 0
    last_healing_song_time = 0
   

    while True:
        current_time = time.time()

        # Check and cast Brave Aura if enough time has passed
        if (current_time - last_brave_time) >= (BUFF_DURATION * 60):
            Cast_buff("6", LONG_BUFF_SLEEP)
            last_brave_time = current_time  # Update last_brave_time to current time

        # Check and cast Quick Motion if enough time has passed
        if (current_time - last_quick_motion_time) >= (BUFF_DURATION * 60):
            Cast_buff("8", LONG_BUFF_SLEEP)
            last_quick_motion_time = current_time  # Update last_quick_motion_time to current time


        # Check and cast Healing Song if enough time has passed (BUFF_DURATION minutes)
        if (current_time - last_healing_song_time) >= (BUFF_DURATION * 60):
            print("Casting Healing Song")
            Cast_buff("3", SHORT_BUFF_SLEEP)
            last_healing_song_time = current_time  # Update last_healing_song_time to current time

        pyautogui.press("7")  # Go to view mode

        time.sleep(BACKWARDS_WALK_SLEEP)

        # Optimize backward walking
        pyautogui.keyDown("s")

        time.sleep(BACKWARDS_WALK_SLEEP)  # Simulate walking backwards
        
        pyautogui.keyUp("s")  # Stop walking

        # Perform cyclone action multiple times
        for _ in range(100):  # Adjust the range as needed
            pyautogui.hotkey("2")  # Use cyclone
            time.sleep(ACTION_SLEEP)

        pyautogui.press("7")  # Exit view mode if necessary

        # Sleep briefly to avoid high CPU usage

        auto_discard.Bag_cleaner()

        time.sleep(1)

        



        """
        Auto_farmer needed improvements
        1)make it run smoothly with less bugs
        2)replace time.sleep?
        3)have a clean exit through the code whenever u want to stop it or it should stopcc
        
        """
     

if __name__ == "__main__":
    time.sleep(2)  # Delay to change tabs or prepare
    Auto_farm()
    
















