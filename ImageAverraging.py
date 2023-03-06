import cv2
import  numpy as np

img1 = cv2.imread('p1.jpg')
img2 = cv2.imread('p2.jpg')

#resize
img1 = cv2.resize (img1, (640, 480))
img2 = cv2.resize (img2, (640, 480))

#convert ke float   
img1 = np.float32(img1)
img2 = np.float32(img2)

sum_img = cv2.add(img1, img2)
avg_img = np.uint8(sum_img/2)

cv2.imshow('Averaged Image', avg_img)
cv2.waitKey(0)
cv2.destroyAllWindows()