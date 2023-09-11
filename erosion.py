from matplotlib import pyplot as plt
import numpy as np
import cv2
import time
import time
start_time = time.time()


img = cv2.imread('/home/mikenguyen/Desktop/cpplogo.jpg') #Retrieve image from system
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #convert image from BGR to RGB

kernel = np.ones((5,5),np.uint8)	#erosion image
erosion = cv2.erode(img,kernel,iterations = 1)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')		#plot the before and after images
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(erosion,)
plt.title('Erosion'), plt.xticks([]), plt.yticks([])
print("--- %s seconds ---" % (time.time() - start_time)) #shows time of execution
plt.show()


