import cv2
import numpy as np

img = cv2.imread('sign1.JPG')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

l_b = np.array([100, 50, 50])
u_b = np.array([130, 255, 255])

mask = cv2.inRange(hsv, l_b, u_b)

res = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("image", img)

cv2.imshow("res", res)
cv2.waitKey(0)
cv2.destroyAllWindows()