from PIL import ImageDraw, ImageFont
import pyautogui
import time
import os
from screeninfo import get_monitors


def screenshot_with_timestamp(output_folder='screenshots', output_file=None):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    monitors = get_monitors()
    for monitor in monitors:
        screen_width, screen_height = monitor.width, monitor.height
        screenshot = pyautogui.screenshot(region=(monitor.x, monitor.y, screen_width, screen_height))
        draw = ImageDraw.Draw(screenshot)
        font = ImageFont.load_default()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        text_bbox = draw.textbbox((0, 0), timestamp, font)

        text_position = ((screen_width - text_bbox[2]) // 2, 10)

        draw.text(text_position, timestamp, fill=(255, 255, 255), font=font)

        if output_file is None:
            output_file = f"{output_folder}/screenshot_{timestamp}.png"
        else:
            output_file = f"{output_folder}/{output_file}"

        screenshot.save(output_file)

    if len(monitors) == 1:
        print(f"{len(monitors)} monitor.\n"+"screenshot is save")
    else:
        print(f"{len(monitors)} monitors.\n"+"screenshots is save")


screenshot_with_timestamp(output_folder='screenshots', output_file='screenshot.png')
