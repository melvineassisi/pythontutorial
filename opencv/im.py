import cv2

path="/Users/assisieo/Documents/python/opencv/download.jpeg"
img=cv2.imread(path,0)# colored
#print(img)

#img=cv2.imread("/Users/assisieo/Documents/python/opencv/download.jpeg",0)# Gray Scale
#print(img)

#print(img.shape) #size

cv2.imshow("name",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

