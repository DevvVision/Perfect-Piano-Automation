import pyautogui
import cv2
import numpy as np
import time
import threading
import mss

# time.sleep(3)
# def screenshot_to_1d_array(top,left,width,height):
#     # Step 1: Take a screenshot using MSS
#     with mss.mss() as sct:
#         # Define the region to capture (adjust the region as needed)
#         monitor = {"top": top, "left": left, "width": width, "height": height}
#         screenshot = sct.grab(monitor)
#
#         # Step 2: Convert the screenshot to a NumPy array
#         img = np.array(screenshot)
#
#         # Step 3: Convert the image to grayscale using OpenCV
#         gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#         # Step 4: Flatten the grayscale image to a 1D array
#         img_1d_array = gray_img.flatten()
#
#     return img_1d_array
# def key1():
#     regionkey1 = (632, 310, 5, 30)
#     while True:
#         # screenshot = pyautogui.screenshot(region=regionkey1)
#         # gray_screenshot = screenshot.convert("L")
#         # gray_array = np.array(gray_screenshot)
#         # gray_array_1d = gray_array.flatten()
#
#         gray_array_1d = screenshot_to_1d_array(310,632,5,30)
#
#         # Count pixels in the range 56 to 68 (inclusive)
#         black_pixel_count = np.count_nonzero((gray_array_1d >= 56) & (gray_array_1d <= 68))
#
#         if black_pixel_count > 0:
#             pyautogui.press('f')
#             # time.sleep(0.1)
#
# def key2():
#     regionkey2 = (732, 310, 5, 30)
#     while True:
#         # screenshot = pyautogui.screenshot(region=regionkey2)
#         # gray_screenshot = screenshot.convert("L")
#         # gray_array = np.array(gray_screenshot)
#         # gray_array_1d = gray_array.flatten()
#
#         gray_array_1d = screenshot_to_1d_array(310, 732, 5, 30)
#         # Count pixels in the range 56 to 68 (inclusive)
#         black_pixel_count = np.count_nonzero((gray_array_1d >= 56) & (gray_array_1d <= 68))
#
#         if black_pixel_count > 0:
#             pyautogui.press('g')
#             # time.sleep(0.1)
#
#
# def key3():
#     regionkey3 = (832, 310, 5, 30)
#     while True:
#         # screenshot = pyautogui.screenshot(region=regionkey3)
#         # gray_screenshot = screenshot.convert("L")
#         # gray_array = np.array(gray_screenshot)
#         # gray_array_1d = gray_array.flatten()
#         gray_array_1d = screenshot_to_1d_array(310, 832, 5, 30)
#         # Count pixels in the range 56 to 68 (inclusive)
#         black_pixel_count = np.count_nonzero((gray_array_1d >= 56) & (gray_array_1d <= 68))
#
#         if black_pixel_count > 0:
#             pyautogui.press('h')
#             # time.sleep(0.1)
#
#
# def key4():
#     regionkey4 = (932, 310, 5, 30)
#     while True:
#         # screenshot = pyautogui.screenshot(region=regionkey4)
#         # gray_screenshot = screenshot.convert("L")
#         # gray_array = np.array(gray_screenshot)
#         # gray_array_1d = gray_array.flatten(
#
#         gray_array_1d = screenshot_to_1d_array(310, 932, 5, 30)
#         # Count pixels in the range 56 to 68 (inclusive)
#         black_pixel_count = np.count_nonzero((gray_array_1d >= 56) & (gray_array_1d <= 68))
#
#         if black_pixel_count > 0:
#             pyautogui.press('j')
#             # time.sleep(0.1)
# #
# #
# # Create threads for each function
# thread1 = threading.Thread(target=key1)
# thread2 = threading.Thread(target=key2)
# thread3 = threading.Thread(target=key3)
# thread4 = threading.Thread(target=key4)
#
# # Start the threads
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()

#
# time.sleep(3)
# # def screenshot_to_1d_array(top,left,width,height):
# #     # Step 1: Take a screenshot using MSS
# #     with mss.mss() as sct:
# #         # Define the region to capture (adjust the region as needed)
# #         monitor = {"top": top, "left": left, "width": width, "height": height}
# #         screenshot = sct.grab(monitor)
# #
# #         # Step 2: Convert the screenshot to a NumPy array
# #         img = np.array(screenshot)
# #
# #         # Step 3: Convert the image to grayscale using OpenCV
# #         gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #
# #         # Step 4: Flatten the grayscale image to a 1D array
# #         img_1d_array = gray_img.flatten()
# #
# #     return img_1d_array
# def key1():
#     regionkey1 = (632, 310, 5, 30)
#     while True:
#         # screenshot = pyautogui.screenshot(region=regionkey1)
#         # gray_screenshot = screenshot.convert("L")
#         # gray_array = np.array(gray_screenshot)
#         # gray_array_1d = gray_array.flatten()
#         with mss.mss() as sct:
#             # Define the region to capture (adjust the region as needed)
#             monitor = {"top": 310, "left": 632, "width": 5, "height": 30}
#             screenshot = sct.grab(monitor)
#
#             # Step 2: Convert the screenshot to a NumPy array
#             img = np.array(screenshot)
#
#             # Step 3: Convert the image to grayscale using OpenCV
#             gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#             # Step 4: Flatten the grayscale image to a 1D array
#             img_1d_array = gray_img.flatten()
#             black_pixel_count = np.count_nonzero((img_1d_array >= 56) & (img_1d_array <= 68))
#             if black_pixel_count > 10:
#                 pyautogui.press('f')
#         # gray_array_1d = screenshot_to_1d_array(310,632,5,30)
#
#         # Count pixels in the range 56 to 68 (inclusive)
#         # black_pixel_count = np.count_nonzero((gray_array_1d >= 56) & (gray_array_1d <= 68))
#
#         # if black_pixel_count > 10:
#         #     pyautogui.press('f')
#             # time.sleep(0.1)
#
# def key2():
#     regionkey2 = (732, 310, 5, 30)
#     while True:
#         with mss.mss() as sct:
#             # Define the region to capture (adjust the region as needed)
#             monitor = {"top": 310, "left": 732, "width": 5, "height": 30}
#             screenshot = sct.grab(monitor)
#
#             # Step 2: Convert the screenshot to a NumPy array
#             img = np.array(screenshot)
#
#             # Step 3: Convert the image to grayscale using OpenCV
#             gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#             # Step 4: Flatten the grayscale image to a 1D array
#             img_1d_array = gray_img.flatten()
#             black_pixel_count = np.count_nonzero((img_1d_array >= 56) & (img_1d_array <= 68))
#             if black_pixel_count > 10:
#                 pyautogui.press('g')
#
#
# def key3():
#     regionkey3 = (832, 310, 5, 30)
#     while True:
#         with mss.mss() as sct:
#             # Define the region to capture (adjust the region as needed)
#             monitor = {"top": 310, "left": 832, "width": 5, "height": 30}
#             screenshot = sct.grab(monitor)
#
#             # Step 2: Convert the screenshot to a NumPy array
#             img = np.array(screenshot)
#
#             # Step 3: Convert the image to grayscale using OpenCV
#             gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#             # Step 4: Flatten the grayscale image to a 1D array
#             img_1d_array = gray_img.flatten()
#             black_pixel_count = np.count_nonzero((img_1d_array >= 56) & (img_1d_array <= 68))
#             if black_pixel_count > 10:
#                 pyautogui.press('h')
#
# def key4():
#     regionkey4 = (932, 310, 5, 30)
#     while True:
#         with mss.mss() as sct:
#             # Define the region to capture (adjust the region as needed)
#             monitor = {"top": 310, "left": 932, "width": 5, "height": 30}
#             screenshot = sct.grab(monitor)
#
#             # Step 2: Convert the screenshot to a NumPy array
#             img = np.array(screenshot)
#
#             # Step 3: Convert the image to grayscale using OpenCV
#             gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#             # Step 4: Flatten the grayscale image to a 1D array
#             img_1d_array = gray_img.flatten()
#             black_pixel_count = np.count_nonzero((img_1d_array >= 56) & (img_1d_array <= 68))
#             if black_pixel_count > 10:
#                 pyautogui.press('j')
#
# # Create threads for each function
# thread1 = threading.Thread(target=key1)
# thread2 = threading.Thread(target=key2)
# thread3 = threading.Thread(target=key3)
# thread4 = threading.Thread(target=key4)
#
# # Start the threads
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()




# v3?


time.sleep(3)
# def screenshot_to_1d_array(top,left,width,height):
#     # Step 1: Take a screenshot using MSS
#     with mss.mss() as sct:
#         # Define the region to capture (adjust the region as needed)
#         monitor = {"top": top, "left": left, "width": width, "height": height}
#         screenshot = sct.grab(monitor)
#
#         # Step 2: Convert the screenshot to a NumPy array
#         img = np.array(screenshot)
#
#         # Step 3: Convert the image to grayscale using OpenCV
#         gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#         # Step 4: Flatten the grayscale image to a 1D array
#         img_1d_array = gray_img.flatten()
#
#     return img_1d_array
def key1():
    regionkey1 = (632, 310, 5, 30)
    with mss.mss() as sct:
        # screenshot = pyautogui.screenshot(region=regionkey1)
        # gray_screenshot = screenshot.convert("L")
        # gray_array = np.array(gray_screenshot)
        # gray_array_1d = gray_array.flatten()
        monitor = {"top": 310, "left": 632, "width": 5, "height": 30}
        while True:
            # Define the region to capture (adjust the region as needed)
            screenshot = sct.grab(monitor)
            # Step 2: Convert the screenshot to a NumPy array
            img = np.array(screenshot)

            # Step 3: Convert the image to grayscale using OpenCV
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Step 4: Flatten the grayscale image to a 1D array
            img_1d_array = gray_img.flatten()
            black_pixel_count = np.count_nonzero((img_1d_array >= 56) & (img_1d_array <= 68))
            if black_pixel_count > 10:
                pyautogui.press('f')
        # gray_array_1d = screenshot_to_1d_array(310,632,5,30)

        # Count pixels in the range 56 to 68 (inclusive)
        # black_pixel_count = np.count_nonzero((gray_array_1d >= 56) & (gray_array_1d <= 68))

        # if black_pixel_count > 10:
        #     pyautogui.press('f')
            # time.sleep(0.1)

def key2():
    regionkey2 = (732, 310, 5, 30)
    monitor = {"top": 310, "left": 732, "width": 5, "height": 30}
    with mss.mss() as sct:
        while True:
            # Define the region to capture (adjust the region as needed)
            screenshot = sct.grab(monitor)

            # Step 2: Convert the screenshot to a NumPy array
            img = np.array(screenshot)

            # Step 3: Convert the image to grayscale using OpenCV
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Step 4: Flatten the grayscale image to a 1D array
            img_1d_array = gray_img.flatten()
            black_pixel_count = np.count_nonzero((img_1d_array >= 56) & (img_1d_array <= 68))
            if black_pixel_count > 10:
                pyautogui.press('g')


def key3():
    regionkey3 = (832, 310, 5, 30)
    monitor = {"top": 310, "left": 832, "width": 5, "height": 30}
    with mss.mss() as sct:
        while True:
            # Define the region to capture (adjust the region as needed)
            screenshot = sct.grab(monitor)

            # Step 2: Convert the screenshot to a NumPy array
            img = np.array(screenshot)

            # Step 3: Convert the image to grayscale using OpenCV
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Step 4: Flatten the grayscale image to a 1D array
            img_1d_array = gray_img.flatten()
            black_pixel_count = np.count_nonzero((img_1d_array >= 56) & (img_1d_array <= 68))
            if black_pixel_count > 10:
                pyautogui.press('h')

def key4():
    regionkey4 = (932, 310, 5, 30)
    monitor = {"top": 310, "left": 932, "width": 5, "height": 30}
    with mss.mss() as sct:
        while True:
            # Define the region to capture (adjust the region as needed)
            screenshot = sct.grab(monitor)
            # Step 2: Convert the screenshot to a NumPy array
            img = np.array(screenshot)

            # Step 3: Convert the image to grayscale using OpenCV
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Step 4: Flatten the grayscale image to a 1D array
            img_1d_array = gray_img.flatten()
            black_pixel_count = np.count_nonzero((img_1d_array >= 56) & (img_1d_array <= 68))
            if black_pixel_count > 10:
                pyautogui.press('j')

# Create threads for each function
thread1 = threading.Thread(target=key1)
thread2 = threading.Thread(target=key2)
thread3 = threading.Thread(target=key3)
thread4 = threading.Thread(target=key4)

# Start the threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()

