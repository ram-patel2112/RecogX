import cv2
from ultralytics import YOLO

class PhoneDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect_phone(self, frame, frame_count):
        if frame_count % 2 != 0:
            return False

        results = self.model(frame)

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])

                if cls == 67 and conf > 0.3:
                    cv2.putText(frame, "Phone Detected! Process Rejected",
                                (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.8,
                                (0, 0, 255),
                                2)
                    return True

        return False