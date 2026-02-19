import cv2
import dlib
import random
import time
import numpy as np
import face_recognition
import winsound

from config import *
from face.face_loader import load_known_faces
from face.liveness import eye_aspect_ratio, calculate_distance
from detection.phone_detector import PhoneDetector
from attendance.attendance_manager import save_attendance

# Load models
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(SHAPE_PREDICTOR_PATH)

known_face_encodings, known_face_names = load_known_faces(STUDENTS_DIR)
phone_detector = PhoneDetector(YOLO_MODEL_PATH)

cap = cv2.VideoCapture(0)

def register_new_face(frame):
    name = input("Enter Name: ")
    path = f"{STUDENTS_DIR}/{name}.jpg"
    cv2.imwrite(path, frame)
    print("✅ Face Registered Successfully")

def run_verification():
    required_blinks = random.randint(2, 3)
    completed_blinks = 0
    start_time = time.time()
    frame_count = 0

    print(f"Blink {required_blinks} times!")

    while completed_blinks < required_blinks:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        if phone_detector.detect_phone(frame, frame_count):
            print("❌ Phone detected!")
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, face_locations)

        for encoding in encodings:
            matches = face_recognition.compare_faces(
                known_face_encodings,
                encoding,
                tolerance=0.5
            )

            if True in matches:
                name = known_face_names[
                    known_face_encodings[matches.index(True)].tobytes()
                ]
                print(f"✅ Recognized {name}")
                save_attendance(name, ATTENDANCE_FILE)
                break

        cv2.imshow("RecogX", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_verification()