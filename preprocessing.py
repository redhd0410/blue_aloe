import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2


# defining global variable path
image_path = os.getcwd()

def loadImages(path):
    image_files = sorted([os.path.join(path, 'posters_data', file)
         for file in os.listdir(path + "/posters_data") if file.endswith('.jpg')])
    return image_files



# Display one image
def display_one(a, title1="Original"):
    plt.imshow(a), plt.title(title1)
    plt.xticks([]), plt.yticks([])
    plt.show()  # Display two images


def display(a, b, title1="Original", title2="Edited"):
    plt.subplot(121), plt.imshow(a), plt.title(title1)
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(b), plt.title(title2)
    plt.xticks([]), plt.yticks([])
    plt.show()


def processing(data):
    # loading image
    # Getting 3 images to work with
    img = [cv2.imread(i, cv2.IMREAD_UNCHANGED) for i in data[:3]]
    print('Original size', img[0].shape)
    # --------------------------------
    # setting dim of the resize
    height = 250
    width = 185
    dim = (width, height)
    res_img = []
    for i in range(len(img)):
        res = cv2.resize(img[i], dim, interpolation=cv2.INTER_LINEAR)
        res_img.append(res)

    # Checking the size
    print("RESIZED", res_img[1].shape)
    # Visualizing one of the images in the array
    original = res_img[1]
    display_one(original)

    # ----------------------------------
    # Remove noise
    # Gaussian
    no_noise = []
    for i in range(len(res_img)):
        blur = cv2.GaussianBlur(res_img[i], (5, 5), 0)
        no_noise.append(blur)

    image = no_noise[1]
    display(original, image, 'Original', 'Blured')
    # ---------------------------------


## body
data = loadImages(image_path)
processing(data)



