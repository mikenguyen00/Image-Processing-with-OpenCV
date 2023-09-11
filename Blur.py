
from matplotlib import pyplot as plt
import numpy as np
import cv2
import time
start_time = time.time()

img = cv2.imread('/home/mikenguyen/Desktop/cpplogo.jpg') #Retrieve image from system
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #convert image from BGR to RGB

blur = cv2.blur(img,(13,13),0)  #Blur image 

plt.subplot(121),plt.imshow(img),plt.title('Original')	#plot the before and after images
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
print("--- %s seconds ---" % (time.time() - start_time))	#shows time of execution
plt.show()








