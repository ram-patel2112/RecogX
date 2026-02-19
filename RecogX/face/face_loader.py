import os
import face_recognition

known_face_encodings = []
known_face_names = {}

def load_known_faces(students_dir):
    global known_face_encodings, known_face_names

    known_face_encodings.clear()
    known_face_names.clear()

    if not os.path.exists(students_dir):
        os.makedirs(students_dir)

    for file in os.listdir(students_dir):
        if file.endswith(".jpg") or file.endswith(".png"):
            name = os.path.splitext(file)[0]
            image_path = os.path.join(students_dir, file)

            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)

            if encodings:
                known_face_encodings.append(encodings[0])
                known_face_names[encodings[0].tobytes()] = name
                print(f"✅ Loaded {name}")
            else:
                print(f"⚠ No face found in {file}")

    return known_face_encodings, known_face_names