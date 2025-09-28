import cv2
import os

haar_file = cv2.data.haarcascades + "/" + 'haarcascade_frontalface_default.xml'
datasets = 'dataset' # All the faces data will be present this folder
sub_data = "tim_pics" # These are sub data sets of folder, for my faces I've used my name

current_directory = os.path.dirname(os.path.abspath(__file__))
datasets = os.path.join(current_directory, "dataset")
# Parent Directory
if not os.path.isdir(datasets):
    os.mkdir(datasets)
# Sub Directory
path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.mkdir(path) 

(width, height) = (130, 100)    # defining the size of images   
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)    # Use camera 0

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

count = 1
while count <31:
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite(f"{path}/{count}.png", face_resize)
        count += 1
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()
