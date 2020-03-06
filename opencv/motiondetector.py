import cv2,time

video=cv2.VideoCapture(0)
first_frame=None

while True:

    check,frame=video.read()
    print(frame)
    cv2.imshow('Capture',frame)
    gray_scale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_scale=cv2.GaussianBlur(gray_scale,(21,21),0)
    if first_frame is None:
        first_frame=gray_scale
        continue
    delta_frame=cv2.absdiff(first_frame,gray_scale)
    thresh_delta=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_delta=cv2.dilate(delta_frame,None,iterations=0)
    (_,cnts,_)=cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if(cv2.contourArea(contour)<1000):
            continue
        (x,y,w,h)=cv2.boundingRect(frame,(x,y),(x+w,y+h),(0,255,0),3)
    
    cv2.imshow('frame',frame)
    cv2.imshow('Capturing',gray_scale)
    cv2.imshow('delta',delta_frame)
    cv2.imshow('thresh',thresh_delta)


    
    key=cv2.waitKey(1)
    if key==ord('q'):
        break



video.release()
cv2.destroyAllWindows()
