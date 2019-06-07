import cv2
dataset = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray)
        eyes = eye_cascade.detectMultiScale(gray)
        smile = smile_cascade.detectMultiScale(gray)
        for x,y,w,h in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),4)
        for x,y,w,h in eyes:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),4)
        #for x,y,w,h in smile:
            #cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),4)
        cv2.imshow('result', img)
        if cv2.waitKey(1) == 27:
            break
    else:
        print("Camera not working")
cap.release()
cv2.destroyAllWindows()
