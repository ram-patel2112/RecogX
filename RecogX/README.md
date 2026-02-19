# 🎓 RecogX – Intelligent Attendance System using Face Recognition

RecogX is an AI-powered attendance management system that uses real-time Face Recognition, Blink-Based Liveness Detection, and Phone Detection to securely record attendance.  

The system is designed to prevent spoofing attempts (such as using printed photos or mobile screens) and ensure that only physically present individuals are marked as present.

This project combines multiple computer vision techniques and deep learning models to create a smart and secure attendance solution.

---

# 📌 Problem Statement

Traditional attendance systems suffer from multiple issues:

- Proxy attendance
- Manual errors
- Time consumption
- Lack of security verification
- Spoofing using photos

RecogX addresses these problems by integrating biometric verification and AI-based object detection to ensure secure attendance logging.

---

# 🧠 System Overview

RecogX works in multiple stages:

1. Face Detection  
2. Face Recognition  
3. Blink-Based Liveness Verification  
4. Phone Detection (Anti-Cheating Mechanism)  
5. Face Distance Monitoring  
6. Attendance Logging in Excel  

Each stage ensures authenticity and prevents fraudulent attendance marking.

---

# 🚀 Key Features

## ✅ 1. Real-Time Face Recognition

The system uses the `face_recognition` library built on top of deep learning models to:

- Extract facial encodings
- Compare them with stored student encodings
- Identify the person in real time

Encodings are generated from images stored inside the `students/` directory.

---

## 👁️ 2. Blink-Based Liveness Detection (Anti-Spoofing)

To prevent spoofing using printed photos or static images:

- Eye landmarks are detected using dlib’s 68 facial landmark model.
- Eye Aspect Ratio (EAR) is calculated.
- The system randomly asks the user to blink 2–3 times.
- Only after successful blinking is verification completed.

This ensures that the detected face is a live human.

---

## 📱 3. Phone Detection using YOLOv8

The system integrates YOLOv8 (You Only Look Once) object detection model to detect mobile phones.

If a phone is detected during verification:

- The process is immediately rejected.
- Attendance is not marked.

This feature makes RecogX suitable for exam environments.

---

## 📏 4. Face Distance Monitoring

The system calculates approximate face distance using:

Distance = (Reference Width × Focal Length) / Face Width in Pixels

If the user is too close to the camera:

- The system prompts the user to move back.
- Verification pauses until proper distance is maintained.

---

## 📊 5. Automatic Attendance Logging

Once verification succeeds:

- Student name
- Date
- Time

Are automatically stored in:

attendance.xlsx


The file is updated dynamically using Pandas.

---

# 🛠️ Technologies Used

- Python  
- OpenCV (Real-time video processing)  
- dlib (Facial landmark detection)  
- face_recognition (Face encoding & comparison)  
- YOLOv8 by Ultralytics (Object detection)  
- Pandas (Data handling)  
- NumPy (Mathematical operations)  

---

# 📂 Project Structure

RecogX/
│
├── main.py
├── config.py
│
├── face/
│ ├── face_loader.py
│ ├── liveness.py
│
├── detection/
│ └── phone_detector.py
│
├── attendance/
│ └── attendance_manager.py
│
├── students/
├── requirements.txt
├── README.md
└── .gitignore