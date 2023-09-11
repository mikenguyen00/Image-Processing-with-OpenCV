
from matplotlib import pyplot as plt
import numpy as np
import cv2
import time
start_time = time.time()

img = cv2.imread('/home/mikenguyen/Desktop/cpplogo.jpg') #Retrieve image from system
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #convert image from BGR to RGB

height, width = img.shape[:2]		#Pixelate image
w, h = (64, 64)
temp = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)
output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

plt.subplot(121),plt.imshow(img),plt.title('Original')		#plot the before and after images
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(output),plt.title('Pixelation')
plt.xticks([]), plt.yticks([])
print("--- %s seconds ---" % (time.time() - start_time)) #shows time of execution
plt.show()









