import cv2

face_cascade=cv2.CascadeClassifier("/Users/assisieo/Documents/python/opencv/haarcascade_frontalface_default.xml")
path="/Users/assisieo/Documents/python/opencv/face.jpeg"
img=cv2.imread(path,1)


gray_scale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_scale, 1.1, 4)

for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("name",img)
cv2.waitKey(0)
cv2.destroyAllWindows()