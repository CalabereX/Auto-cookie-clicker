# 🍪 Auto Cookie Clicker – Steam Edition

A autoclicker for the Steam version of *Cookie Clicker*. Built with Python, it smartly detects when the game is running, pauses automatically when you move the mouse, and exits cleanly with a single key.

Made for players who want to farm hard without losing control.

---

## 🕹️ Key Features

- **Auto-clicking only when Cookie Clicker is running**
- **Pauses when the mouse is moved (so it doesn't get in your way)**
- **Press `ESC` to safely stop the script**
- **Modular, clean and maintainable design**

---

## 📁 Project Structure
auto-cookie-clicker/

├── assets/

├── src/

│ ├── autoclicker.py # Main clicker logic

│ ├── utils.py # Game process detection

│ └── config.py # Configurable parameters


---

## ⚙️ Requirements

Install the required libraries via pip:


pip install pyautogui mouse keyboard psutil

---

## Used Libraries

- pyautogui – Mouse control.

- mouse – Mouse movement detection.

- keyboard – Keyboard input handling.

- psutil – Checks if Cookie Clicker.exe is running.

