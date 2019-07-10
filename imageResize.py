import cv2
import imutils as im

for i in range(1,30):
    img = cv2.imread('./notagglu/'+str(i)+'.png')
    img = cv2.resize(img,(80,80))
    print(img.shape)
    cv2.imwrite('not-agglutinated/'+str(i)+'.png',img)
