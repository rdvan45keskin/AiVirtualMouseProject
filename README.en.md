# AI Virtual Mouse - Hand Gesture Control 🖱️✋

This project is a Python application that allows you to control the mouse cursor with hand gestures using your computer's webcam. It detects hands and fingers using **OpenCV** and **MediaPipe**, and converts these gestures into mouse commands using **PyAutoGUI**.

## 🌍 Language / Dil
[🇹🇷 Türkçe Oku](README.md) | [🇺🇸 Read in English](README.en.md)

## 🌟 Features

- **Contactless Control:** Works with just a webcam, no extra hardware needed.
- **Cursor Movement:** Control the cursor by moving your index finger.
- **Clicking:** Perform a "Click" action by bringing your index and middle fingers together (pinching).
- **Smoothening:** Reduces jitter for a more stable and precise mouse experience.
- **Frame Reduction:** The active area is limited, allowing you to reach the entire screen without moving your hand too much.

## 🛠️ Libraries Used

The following Python libraries are required for this project:

- `opencv-python`: For image processing.
- `mediapipe`: For hand tracking and landmark detection.
- `pyautogui`: For controlling the mouse and keyboard.
- `numpy`: For mathematical operations and coordinate conversions.

## 🚀 Installation

1. Clone or download this repository to your computer:
   ```bash
   git clone https://github.com/rdvan45keskin/AiVirtualMouseProject.git
    ```
2. Navigate to the project directory and install the required libraries:
  ```bash
  pip install opencv-python mediapipe pyautogui numpy
  ```

## 🎮 How to Use?

1. Run the `AiVirtualMouseProject.py` file:
   ```bash
   python AiVirtualMouseProject.py
    ```
2. Show your hand to the camera when it opens. The system works in two modes:

   * **Moving Mode:** If only your **index finger** is up, the mouse cursor follows your finger.
   * **Clicking Mode:** If both your **index and middle fingers** are up, it enters "Clicking Mode". When you bring these two fingers close together (distance decreases), a mouse click is performed.

3. You can press `q` to exit the program.

## ⚙️ Settings

You can adjust the sensitivity by changing the following variables inside `AiVirtualMouseProject.py`:

* **`frameR`**: Frame Reduction amount. Increasing this value allows you to reach the corners of the screen with less hand movement.
* **`smoothening`**: Determines the smoothness of the cursor movement. Higher values make the cursor smoother but may add slight delay.

## 📂 File Structure

* `AiVirtualMouseProject.py`: The main application file.
* `HandTrackingModule.py`: Helper module for hand and finger tracking operations.


