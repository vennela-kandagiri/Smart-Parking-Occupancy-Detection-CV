🚗 Smart Parking Occupancy Detection System (Computer Vision)

A computer vision–based smart parking system that detects free and occupied parking slots from a fixed-camera video feed using image processing.
This project demonstrates how real-world parking systems work when camera position is fixed and parking slots are static.


📌 Problem Statement

Finding available parking spaces in large parking areas is time-consuming and inefficient.
Manual monitoring is impractical, and sensor-based solutions are expensive.
This project provides a vision-based solution that:
Detects parking slot occupancy
Updates availability dynamically
Works with a single fixed camera

🎯 Key Features

📹 Works with parking lot video input
🟩 Green slots → Free parking
🟥 Red slots → Occupied parking
🔄 Dynamic updates when cars enter or leave
🧠 Pixel-based occupancy detection (robust for top-down views)
🖥️ Optimized visualization (scaled display for large videos)
💾 Output video generation (result.mp4)

🛠️ Technology Stack

Python
OpenCV
NumPy


No heavy deep-learning models are required for reliable occupancy detection in fixed-camera setups.
