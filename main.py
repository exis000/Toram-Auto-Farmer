import time
import keyboard
import pyautogui

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

        # Perform farming actions
        pyautogui.press("7")  # Go to view mode222222622222222222222222222222222222222222222222222222222222
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

        time.sleep(0.5)  # Sleep briefly to avoid high CPU usage

def main():
    time.sleep(2)  # Delay to change tabs or prepare
    Auto_farm()

if __name__ == "__main__":
    main()
























    
# import time
# import keyboard
# import pyautogui

# BUFF_DURATION = 10  # Duration after which buffs are reset (in minutes)
# SHORT_BUFF_SLEEP = 1  # Short sleep duration for buff casting
# LONG_BUFF_SLEEP = 4  # Long sleep duration for buff casting
# ACTION_SLEEP = 0.1  # Sleep duration between actions
# BACKWARDS_WALK_SLEEP = 0.3  # Sleep duration for walking backwards

# BUFF_KEYS = {
#     "brave": ("6", BUFF_DURATION * 60),
#     "quick_motion": ("8", BUFF_DURATION * 60),
#     "godspeed_wield": ("5", 30),  # 30 seconds duration
#     "healing_song": ("3", BUFF_DURATION * 60),  # Healing song every 10 minutes
# }

# last_cast_times = {buff: 0 for buff in BUFF_KEYS}

# def cast_buff(key: str, sleep_time: int):
#     print(f"Casting buff with key {key} at {time.strftime('%X')}")
#     keyboard.press(key)
#     time.sleep(sleep_time)
#     keyboard.release(key)

# def check_and_cast_buffs():
#     current_time = time.time()
#     for buff, (key, duration) in BUFF_KEYS.items():
#         if (current_time - last_cast_times[buff]) >= duration:
#             cast_buff(key, SHORT_BUFF_SLEEP if key == "5" else LONG_BUFF_SLEEP)
#             last_cast_times[buff] = current_time

# def perform_farming_actions():
#     pyautogui.press("7")  # Go to view mode
#     time.sleep(BACKWARDS_WALK_SLEEP)
#     pyautogui.keyDown("s")
#     time.sleep(BACKWARDS_WALK_SLEEP)  # Simulate walking backwards
#     pyautogui.keyUp("s")  # Stop walking

#     for _ in range(100):  # Adjust the range as needed
#         pyautogui.hotkey("2")  # Use cyclone
#         time.sleep(ACTION_SLEEP)

#     pyautogui.press("7")  # Exit view mode if necessary

# def auto_farm():
#     try:
#         while True:
#             check_and_cast_buffs()
#             perform_farming_actions()
#             time.sleep(0.2)  # Sleep briefly to avoid high CPU usage
#     except KeyboardInterrupt:
#         print("Auto-farming script stopped.")

# def main():
#     time.sleep(2)  # Delay to change tabs or prepare
#     print("Starting auto-farming script. Press Ctrl+C to stop.")
#     auto_farm()

# if __name__ == "__main__":
#     main()