import keyboard
import pyautogui
import cv2
import numpy as np
import win32con
import win32api
import random
import time

# Get screen size
screen_width, screen_height = pyautogui.size()
# Calculate the center of the screen
center_x, center_y = screen_width // 2, screen_height // 2
# Define a range around the center (e.g., within 100 pixels of the center)
range_x = (center_x - 400, center_x + 400)
range_y = (center_y - 400, center_y + 400)

def random_center_click():
    # Generate a random coordinate within the defined range
    random_x = random.randint(*range_x)
    random_y = random.randint(*range_y)

    # Click at the random coordinate
    pyautogui.click(random_x, random_y)



def screen_capture(region=None):
    if region is not None:
        # Capture the region of the screen defined by the coordinates
        screen_shot = pyautogui.screenshot(region=region)
    else:
        # Capture the entire screen
        screen_shot = pyautogui.screenshot()
    
    # Convert the screenshot to an OpenCV format
    screen_shot = cv2.cvtColor(np.array(screen_shot), cv2.COLOR_RGB2BGR)
    return screen_shot

def random_click_within_box(box, margin = 3):
    x, y = get_random_point_within_box(box, margin)
    click(x, y)
    sleep_long()
    
    # Sleep______
def sleep_short():
    time.sleep(random.uniform(0.1, 0.25))    
    
def sleep_medium():
    time.sleep(random.uniform(0.25, 0.75))

def sleep_long():
    time.sleep(random.uniform(1.0, 1.5))
    
def sleep_very_long():
    time.sleep(random.uniform(5.0, 7.0))
    
def find_image_on_screen(template_path, threshold=0.8):
    return  pyautogui.locateOnScreen(template_path, confidence=0.8) 

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep_short()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
def get_random_point_within_box(box, margin = 3):
    left, top, width, height = box
    right = left + width
    bottom = top + height
    
    # Adjust the box coordinates by the margin
    adjusted_left = left + margin
    adjusted_top = top + margin
    adjusted_right = right - margin
    adjusted_bottom = bottom - margin

    # Ensure the box dimensions are valid after adjusting with the margin
    if adjusted_right <= adjusted_left or adjusted_bottom <= adjusted_top:
        raise ValueError("Box is too small for the given margin.")

    # Generate random coordinates within the adjusted box
    x = random.randint(adjusted_left, adjusted_right)
    y = random.randint(adjusted_top, adjusted_bottom)

    return x, y


# Example usage
sunshine_path = './sunshine.png'
hearts_path = './hearts.png' 
heart_click_count = 0
sunshine_click_count = 0
loop_count = 0
start_time = time.time()

print("\nSunshine Garden Auto Collector")
print("Hold 'q' to quit")
print("==============================================\n")

while True:
    # Check if 'q' is pressed to quit
    if keyboard.is_pressed('q'):
        print("Quitting...")
        break
    sleep_long()
    hearts_location = find_image_on_screen(hearts_path)
    if (hearts_location is not None):
        sleep_long()
        random_click_within_box(hearts_location)
        heart_click_count += 1
        print("+1 heart")
        sleep_long()
        random_center_click()

    sleep_long()
    sunshine_location = find_image_on_screen(sunshine_path)
    if (sunshine_location is not None):
        sleep_long()
        random_click_within_box(sunshine_location)
        sunshine_click_count += 1
        print("+1 sunshine")
        
    # Check if 'q' is pressed to quit
    if keyboard.is_pressed('q'):
        print("Quitting...")
        break
    
    sleep_very_long()
    loop_count += 1
    
print("Total hearts collected: " + str(heart_click_count))
print("Total sunshine collected: " + str(sunshine_click_count))
print("Total loops: " + str(loop_count))
# Calculate and print the elapsed time
elapsed_time = time.time() - start_time
print(f"The script ran for {elapsed_time:.2f} seconds.")
