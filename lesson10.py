import cv2
vid = cv2.VideoCapture("videoplayback.mp4")

car_cascade = cv2.CascadeClassifier("cars.xml")
while True:
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Video', frame)
    key = cv2.waitKey(10)
    if key == 27: break

cv2.destroyAllWindows()
vid.release()