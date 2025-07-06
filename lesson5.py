import cv2
import numpy as np

eye = cv2.imread('images/bubbles.png', cv2.IMREAD_COLOR)
cv2.imshow('Original', eye)

# gray_eye = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Grayscale', gray_eye)

# detected_circles = cv2.HoughCircles(gray_eye, cv2.HOUGH_GRADIENT, dp = 1, minDist=20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40)

# if detected_circles is not None:
#     detected_circles = np.uint16(np.around(detected_circles))
#     for pt in detected_circles[0, :]:
#         a, b, r = pt[0], pt[1], pt[2]
#         cv2.circle(gray_eye, (a, b), r, (0, 255, 0), 2)
#         cv2.circle(gray_eye, (a, b), 1, (0, 0, 255), 2)

#         cv2.imshow('Detected Circles', gray_eye)

#         cv2.waitKey(0)

circles = cv2.SimpleBlobDetector_Params()
circles.filterByArea = True
circles.minArea = 100

circles.filterByCircularity = True
circles.minCircularity = 0.1
circles.filterByConvexity = True
circles.minConvexity = 0.2
circles.filterByInertia = True
circles.minInertiaRatio = 0.01

detector = cv2.SimpleBlobDetector_create(circles)
keypoints = detector.detect(eye)

# Draw blobs on our image as red circles
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(eye, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
number_of_blobs = len(keypoints)
text = "Number of Circular Blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)
# Show blobs
cv2.imshow("Filtering Circular Blobs Only", blobs)

cv2.waitKey(0)


cv2.destroyAllWindows()