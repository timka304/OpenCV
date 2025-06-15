import cv2


tree = cv2.imread('images/tree.jpg')
rainbow = cv2.imread('images/rainbow.jpg')

rainbow = cv2.resize(rainbow, (400, 400))
tree = cv2.resize(tree, (400, 400))

gray_tree = cv2.cvtColor(tree, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Tree', gray_tree)

rotated_tree = cv2.rotate(tree, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated Tree', rotated_tree)

flipped_tree = cv2.getRotationMatrix2D((200, 200), 180, 1)
flipped_tree = cv2.warpAffine(tree, flipped_tree, (400, 400))
cv2.imshow('Flipped Tree', flipped_tree)

edges = cv2.Canny(tree, 400, 500)
cv2.imshow('Edges of Tree', edges)

tree_color_conversion = cv2.cvtColor(tree, cv2.COLOR_BGR2HSV)
cv2.imshow('Tree Color Conversion', tree_color_conversion)

tree_color_conversion2 = cv2.cvtColor(tree, cv2.COLOR_BGR2LAB)
cv2.imshow('Tree Color Conversion 2', tree_color_conversion2)

(row, col) = rainbow.shape[:2]
for i in range(row):
    for j in range(col):
        rainbow[i, j] = sum(rainbow[i, j]) // 3

cv2.imshow('Rainbow Grayscale', rainbow)

cv2.waitKey(0)
cv2.destroyAllWindows()