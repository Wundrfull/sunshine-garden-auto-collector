
# E7 Sunshine Garden Auto Collector

This script automates the task of collecting 'hearts' and 'sunshines' in E7 Sunshine event. It's designed to work with a screen resolution of 2560x1440p but can be adapted for other resolutions (Needs pics of sunshine/heart icons in your resolution).

## Installation

To run this script, you need to install Python and certain Python libraries. You can install these using pip:

`pip install keyboard pyautogui opencv-python numpy pywin32` 

## Usage

1.  Ensure the `sunshine.png` and `hearts.png` template images are in the same directory as the script.
2.  Ensure you have installed python libraries.
3.  Position your application window according to the script's expectation (centered on main 2560x1440p resolution screen).
4.  Run the script in console. E.g.  `python .\AutoCollectSunshineGarden.py`
6.  To stop the script, press 'q' again.

## Disclaimer
- If the script is not working for you, replace the images `sunshine.png` and `hearts.png` with your own.
-   The script might require you to replace the `sunshine.png` and `hearts.png` images with ones captured from your screen resolution for optimal performance.
-   The script's efficiency and accuracy can vary based on the system's performance and the application's visual layout. 
- You can tweak the timings to maximize efficiency, but I left some delay to add RNG.