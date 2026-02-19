import numpy as np

def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    return (A + B) / (2.0 * C)

def calculate_distance(face_width_pixels, reference_width, focal_length):
    return (reference_width * focal_length) / face_width_pixels