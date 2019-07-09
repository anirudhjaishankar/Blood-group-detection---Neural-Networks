import cv2
import matplotlib.pyplot as plt
import numpy as np
import imutils as im


img = cv2.imread('1.png');

# hist = cv2.calcHist([img],[0],None,[256],[0,256])

# plt.plot(hist)
# plt.show()
img1 = img.copy()
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

img1 = cv2.bilateralFilter(img1,9,75,75)
cv2.imshow('bf',img1)

kernel = np.ones((5,5),np.uint8)
gradient = cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('morph', img1)

img1 =cv2.erode(img1, kernel, iterations = 2)
cv2.imshow('erosion',img1)

img1 = cv2.medianBlur(img1,5)
cv2.imshow('MedianBlur',img1)



img2 = img.copy()

img1 = cv2.adaptiveThreshold(img1.copy(),255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,115,2)
cv2.imshow('thresh',img1)
#

#
#
# img1 = cv2.Canny(img1,150,220)
# cv2.imshow('canny', img1)

contours, heirarchy = cv2.findContours(img1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

outline = np.zeros((img1.shape), dtype = 'uint8')

cv2.drawContours(outline, contours, -1, (255,255,255), 1)

print(len(contours))
if len(contours) == 4:
    images = []
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        images.append(img[y:y+h, x:x+w])

        # cv2.rectangle(outline,(x,y),(x+w,y+h),(255,255,255),2)

        cv2.imshow('blood1',images[0]);
        # cv2.imshow('blood2',images[1]);
        # cv2.imshow('blood3',images[2]);
        # cv2.imshow('blood4',images[3]);
    # print(images)

cv2.imshow('img',outline);

cv2.waitKey(0)
cv2.destroyAllWindows()
