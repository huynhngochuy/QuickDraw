import numpy as np
import cv2 
images = np.load(r"C:\Users\huynh\Downloads\Machine Learning Quick draw\vent\project\full_numpy_bitmap_cow.npy")
image = images[12]
image = np.reshape(image, (28,28))
cv2. imwrite("cow.jpg", image)
