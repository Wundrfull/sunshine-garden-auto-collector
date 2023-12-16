import keyboard
import pyautogui
import cv2
import numpy as np
import win32con
import win32api
import random
import time

def random_click_near_center(screen_width, screen_height, range_x=200, range_y=200):
    center_x, center_y = screen_width // 2, screen_height // 2
    random_x = random.randint(center_x - range_x, center_x + range_x)
    random_y = random.randint(center_y - range_y, center_y + range_y)
    perform_click(random_x, random_y)

def perform_click(x, y):
    original_position = pyautogui.position()
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    random_sleep(0.1, 0.25)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    random_sleep(0.1, 0.25)
    pyautogui.moveTo(*original_position)

def random_sleep(min_time, max_time):
    time.sleep(random.uniform(min_time, max_time))

def find_image(template_path, threshold=0.8):
    # Take a screenshot of the entire screen
    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    
    # Load the template image
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    template_height, template_width = template.shape[:2]

    # Perform template matching
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # Check if the maximum match value is greater than or equal to the threshold
    if max_val >= threshold:
        # Return the region (left, top, width, height)
        return (max_loc[0], max_loc[1], template_width, template_height)
    else:
        return None

def random_click_in_box(box, margin=3):
    x, y = get_random_point_in_box(box, margin)
    perform_click(x, y)
    random_sleep(1.0, 1.5)

def get_random_point_in_box(box, margin=3):
    left, top, width, height = box
    adjusted_box = (left + margin, left + width - margin, top + margin, top + height - margin)
    if adjusted_box[1] <= adjusted_box[0] or adjusted_box[3] <= adjusted_box[2]:
        raise ValueError("Adjusted box dimensions are invalid.")
    return random.randint(*adjusted_box[:2]), random.randint(*adjusted_box[2:])

# Initialize
screen_width, screen_height = pyautogui.size()
sunshine_path, hearts_path = './sunshine.png', './hearts.png'
heart_count, sunshine_count, loop_count = 0, 0, 0
start_time = time.time()

print("\nSunshine Garden Auto Collector\nHold 'q' to quit\n" + "="*45)

try:
    while True:
        if keyboard.is_pressed('q'):
            break
        
        random_sleep(2.0, 3.5)
        for template_path, stat_name in [(hearts_path, "heart"), (sunshine_path, "sunshine")]:
            if (image_location := find_image(template_path)) is not None:
                random_sleep(1.0, 1.5)
                print(f"+1 {stat_name}")
                random_click_in_box(image_location)

                # Update the respective counts directly
                if stat_name == "heart":
                    heart_count += 1
                elif stat_name == "sunshine":
                    sunshine_count += 1

                random_click_near_center(screen_width, screen_height)

        loop_count += 1

except KeyboardInterrupt:
    print("Script interrupted by user.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    elapsed_time = time.time() - start_time
    print(f"\nTotal hearts collected: {heart_count}")
    print(f"Total sunshine collected: {sunshine_count}")
    print(f"Total loops: {loop_count}")
    print(f"The script ran for {elapsed_time:.2f} seconds.")
