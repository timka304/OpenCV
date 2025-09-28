import cv2
import os
import numpy as np

current_directory = os.path.dirname(os.path.abspath(__file__))
datasets = os.path.join(current_directory, "dataset")

haar_file = cv2.data.haarcascades + "/" + 'haarcascade_frontalface_default.xml'
print("Recognising Face Please Be in sufficient Light Conditions...")

(images, labels, names, id) = ([], [], {}, 0)

if not os.path.exists(datasets):
    print("Dataset not found")
    exit()

for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            try:
                path = os.path.join(subjectpath, filename)
                face = cv2.imread(path, 0)
                if face is not None:
                    images.append(face)
                    labels.append(id)
                else:
                    print(f"Image {path} is not valid")
            except Exception as e:
                print(f"Error reading image {path}: {e}")
        id += 1

if len(images) == 0:
    print("No images found in dataset")
    exit()

(width, height) = (130, 100)
images = np.array(images)
labels = np.array(labels)

try:
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(images, labels)

except Exception as e:
    print(f'Error creating or training the model: {e}')
    exit()


except AttributeError:
    print("OpenCV Face Recogntion Module not found. Please install opencv-contrib-python.")
    print("You can install it using pip:")
    print("pip install opencv-contrib-python")
    exit()


face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)

while True:
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        prediction = model.predict(face_resize)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if prediction[1] < 500:
            cv2.putText(im, '%s - %.0f' % (names[prediction[0]], prediction[1]), (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
        else:
            cv2.putText(im, 'not recognized', (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
    
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27:
        break