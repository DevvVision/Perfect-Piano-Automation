Perfect Piano Game Automation
This project automates the gameplay of Perfect Piano using Python. The automation detects on-screen visual cues and simulates key presses to achieve a high score. The script leverages the power of OpenCV, PyAutoGUI, NumPy, and MSS to capture specific regions of the screen, process the pixel data, and press the corresponding keys in real-time.

Key Features
Real-time Screen Monitoring: The script continuously monitors predefined screen regions.
Key Press Simulation: Based on the pixel data, it simulates key presses ('f', 'g', 'h', 'j').
Automated Game Play: The script simulates perfect key presses to play the game automatically.
Multithreading: The program uses multithreading to monitor multiple regions and simulate key presses simultaneously.
How It Works
The script monitors different regions of the screen to detect changes in pixel intensity.
When a specific intensity range (indicating the need to press a key) is detected in the region, it simulates a key press.
The program uses OpenCV to process the images and PyAutoGUI to simulate the key presses based on the detected pixels.
Requirements
Before running the code, ensure you have the following Python libraries installed:

pyautogui
cv2 (OpenCV)
numpy
mss
threading (Python's standard library)
You can install the required libraries using pip:

bash
Copy code
pip install pyautogui opencv-python numpy mss
How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/YourUsername/Perfect-Piano-Automation.git
Navigate to the project directory:

bash
Copy code
cd Perfect-Piano-Automation
Run the script:

bash
Copy code
python perfect_piano_automation.py
The script will start monitoring specific regions of the screen and simulate the key presses based on the detected visual cues.

Scoring Achieved
This automation has successfully achieved a score of 7200 in the Perfect Piano game. The high score demonstrates the effectiveness of this automation for consistent, high-level gameplay.

Notes
You may need to adjust the region coordinates in the script to fit the screen resolution or window size of Perfect Piano.
The automation relies on specific pixel intensities; therefore, if the game's visuals change (e.g., different themes or designs), the pixel intensity thresholds might need adjustments.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
OpenCV: For image processing.
PyAutoGUI: For simulating key presses.
MSS: For efficient screen capturing.
