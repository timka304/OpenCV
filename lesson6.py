import cv2
import os
from PIL import Image

os.chdir("C:\\Users\\304ti\\Desktop\\JETLEARN\\OpenCV\\images")
path = "C:\\Users\\304ti\\Desktop\\JETLEARN\\OpenCV\\images"
mean_height = 0
mean_width = 0
number_of_images = len(os.listdir("."))

for file in os.listdir("."):
    img = Image.open(os.path.join(path, file))
    width, height = img.size
    mean_width = mean_width + width
    mean_height = mean_height + height

mean_width = mean_width // number_of_images
mean_height = mean_height // number_of_images
print("Mean Width: ", mean_width)
print("Mean Height: ", mean_height)

# Resize images to the mean dimensions
for file in os.listdir("."):
    if file.endswith(('.png') or file.endswith('.jpg')):
        img = Image.open(os.path.join(path, file))
        width, height = img.size
        print(width, height)

        resized_image = img.resize((mean_width, mean_height), Image.LANCZOS)
        resized_image.save(file, "PNG", quality=95)
        print(img.filename.split("\\")[-1], "is resized")

def video_generator():
    video_name = "video.mp4"
    os.chdir("C:\\Users\\304ti\\Desktop\\JETLEARN\\OpenCV\\images")
    images = []
    for img_file in os.listdir("."):
        if img_file.endswith(('.png', '.jpg')):
            images.append(img_file)
    
    print(images)

    frame = cv2.imread(os.path.join(".", images[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, 1, (width, height))
    for image in images:
        video.write(cv2.imread(os.path.join(".", image)))
    cv2.destroyAllWindows()
    video.release()



video_generator()