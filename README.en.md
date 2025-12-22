# AI Virtual Mouse - Hand Gesture Mouse & Volume Control 🖱️🔊✋

This project is a Python application that allows you to control the **mouse cursor** and **computer volume** using hand gestures via your computer's webcam. It uses **OpenCV** and **MediaPipe** libraries to distinguish between right and left hands, allowing you to manage the mouse with your right hand and volume levels with your left hand.

## 🌍 Language / Dil
[🇹🇷 Türkçe Oku](README.md) | [🇺🇸 Read in English](README.en.md)

## 🌟 Features

- **Dual Hand Support:** Detects right and left hands separately and assigns different tasks to each.
- **Mouse Control (Right Hand):**
  - **Cursor Movement:** Move the cursor using your index finger.
  - **Clicking:** Perform a click by bringing your index and middle fingers together.
- **Volume Control (Left Hand):** Adjust the computer volume by changing the distance between your left hand's thumb and index finger.
- **Smoothening:** Reduces jitter for a more stable and precise user experience.

## 🛠️ Libraries Used

The following Python libraries are required for this project to run:

- `opencv-python`: For image processing.
- `mediapipe`: For hand tracking and landmark detection.
- `pyautogui`: For mouse and keyboard control.
- `pycaw`: For Windows audio system control.
- `comtypes`: Required for the Pycaw library to function.
- `numpy`: For mathematical operations.

## 🚀 Installation

1. Clone or download this repository to your computer:
  ```bash
  git clone https://github.com/rdvan45keskin/AiVirtualMouseProject.git
  ```
2. Navigate to the project directory and install the required libraries:
  ```bash
  pip install opencv-python mediapipe pyautogui numpy pycaw comtypes
  ```

## 🎮 How to Use?

Show your hands to the camera when it opens. The system works as follows:

### 👉 Right Hand: Mouse Mode
* **Movement:** If only your **index finger** is up, the mouse cursor follows your finger.
* **Clicking:** If both your **index and middle fingers** are up, it enters "Clicking Mode". When you bring these two fingers close together (perform a click), a mouse click is executed.

### 👈 Left Hand: Volume Mode
* **Volume Adjustment:** You control the volume using your left hand's **thumb and index finger**.
* Opening the fingers increases the volume, closing them decreases it.
* **Volume Lock:** When you close your pinky finger, the volume level is locked at the current setting.

You can press the `q` key to exit the program.

## ⚙️ Settings

You can adjust the sensitivity by changing the following variables inside the `AiVirtualMouseProject.py` file:

* **`frameR`**: Frame Reduction amount (To reach the entire screen without moving your hand too much).
* **`smoothening`**: Smoothening level of the cursor movement.

## 📂 File Structure

* `AiVirtualMouseProject.py`: The main application file.
* `HandTrackingModule.py`: Helper module for hand/finger tracking and distinguishing between right/left hands.

