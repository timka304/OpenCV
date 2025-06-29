import cv2

sky = cv2.imread('images/sky.jpg')
# cv2.imshow('Sky', sky)

line1 = cv2.line(sky, (50, 50), (200, 200), (0, 255, 0), 5)
line2 = cv2.line(sky, (50, 50), (200, 50), (0, 255, 0), 5)

rectangle = cv2.rectangle(sky, (50, 50), (200, 200), (0, 0, 255), 5)
# cv2.imshow('Rectangle', rectangle)

start_point = (170, 170)
end_point = (300, 300)
color = (255, 0, 0)  
thickness = -1

rectangle_filled = cv2.rectangle(sky, start_point, end_point, color, thickness)
# cv2.imshow('Filled Rectangle', rectangle_filled)

circle = cv2.circle(sky, (300, 300), 50, (0, 255, 255), -1)
# cv2.imshow('Filled Circle', circle)

circle1 = cv2.circle(sky, (100, 100), 50, (255, 0, 255), 5)
# cv2.imshow('Circle', circle1)

line8 = cv2.putText(sky, 'Hello OpenCV', (300, 200), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255,), 10, cv2.LINE_8)
cv2.imshow('Line 8', line8)

normal = cv2.putText(sky, 'Hello OpenCV', (300, 200), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 0), 10)
cv2.imshow('Normal', normal)

line4 = cv2.putText(sky, 'Hello OpenCV', (300, 200), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 0), 10, cv2.LINE_4)
cv2.imshow('Line 4', line4)

lineAA = cv2.putText(sky, 'Hello OpenCV', (300, 200), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 0), 10, cv2.LINE_AA)
cv2.imshow('LineAA', lineAA)


cv2.waitKey(0)
cv2.destroyAllWindows()