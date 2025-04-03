from keras.models import load_model
import numpy as np
import cv2
from tensorflow.keras.utils import img_to_array

# Path to models
detection_model_path = 'haarcascade_files/haarcascade_frontalface_default.xml'
emotion_model_path = 'final_model.h5'

# Load models
face_detection = cv2.CascadeClassifier(detection_model_path)
emotion_classifier = load_model(emotion_model_path, compile=False)

# Expanded emotion list
EMOTIONS = ["happy", "sad", "angry", "surprise", "fear", "neutral"]

def emotion_testing():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None
    
    print("Press 'q' to exit the webcam.")
    while True:
        ret, test_img = cap.read()
        if not ret:
            continue
        
        gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
        faces_detected = face_detection.detectMultiScale(gray_img, 1.32, 5)

        for (x, y, w, h) in faces_detected:
            cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)
            roi_gray = gray_img[y:y + w, x:x + h]
            roi_gray = cv2.resize(roi_gray, (48, 48))
            
            img_pixels = img_to_array(roi_gray)
            img_pixels = np.expand_dims(img_pixels, axis=0)
            img_pixels /= 255.0

            predictions = emotion_classifier.predict(img_pixels)
            max_index = np.argmax(predictions[0])
            predicted_emotion = EMOTIONS[max_index]

            cv2.putText(test_img, predicted_emotion, (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        resized_img = cv2.resize(test_img, (1000, 700))
        cv2.imshow('Facial Emotion Analysis', resized_img)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return predicted_emotion
