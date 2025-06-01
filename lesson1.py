import cv2
import os

# img = cv2.imread('images/pikachu.png', cv2.IMREAD_GRAYSCALE)
# # img = cv2.imread('images/pikachu.png', 1)
# cv2.imshow('Pikachu', img)

# cv2.waitKey(0)

# #Save the image
# cv2.imwrite('images/pokemon.png', img)


img = cv2.imread('images/golovkin.jpg', cv2.IMREAD_COLOR)
B, G, R = cv2.split(img)
cv2.imshow('Golovkin', img)
cv2.imshow('Blue Channel', B)
cv2.imshow('Green Channel', G)
cv2.imshow('Red Channel', R)

cv2.waitKey(0)

new_dir = 'C:/Users/304ti/Desktop/JETLEARN/OpenCV/images/temp'
os.chdir(new_dir)
img2 = cv2.imread('images/golovkin.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('golovkin_gray', img2)



cv2.destroyAllWindows()