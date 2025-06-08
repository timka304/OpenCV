import cv2
import numpy as np


img1 = cv2.imread('images/cat.jpg')
img2 = cv2.imread('images/dog.jpg')

#BORDERING
img = cv2.resize(img2, (400, 400))
bordered = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT, value=1)
cv2.imshow('Bordered Image', bordered)

#BILATERAL BLURRING

# img = cv2.resize(img1, (400, 400))
# bilateral = cv2.bilateralFilter(img, 9, 75, 75)
# cv2.imshow('Bilateral Blur', bilateral)


#MEDIAN BLURRING - Preserves edges while reducing noise

# img = cv2.resize(img2, (400, 400))
# median = cv2.medianBlur(img,5)
# cv2.imshow('Median Blur', median)


#GAUSSIAN BLURRING

# img1 = cv2.resize(img1, (400, 400))
# gaussian = cv2.GaussianBlur(img1, (5, 5), 10)
# cv2.imshow('Gaussian Blur', gaussian)


#ERROSION

# kernel = np.ones((5, 5), np.uint8)
# img = cv2.erode(img2, kernel)
# cv2.imshow('Erosion', img)


#RESIZING IMAGES

# img1 = cv2.resize(img1, (400, 400))
# cv2.imshow('Cat', img1)


#SUBTRACTION

# img3 = cv2.subtract(img1, img2)
# cv2.imwrite('combination.jpg', img3)


# cv2.imshow('Combination', img3)


#WEIGHTED ADDITION

#weightedsum = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
# cv2.imshow('Weighted Sum', weightedsum)


#ADDITION

# img3 = cv2.add(img1, img2)
# cv2.imwrite('combination.jpg', img3)


# cv2.imshow('Combination', img3)


cv2.waitKey(0)
cv2.destroyAllWindows()