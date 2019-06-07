def main():
    import cv2

    cap = cv2.VideoCapture(0) #0 gives default camera
    while True:
        ret, img = cap.read()
        cv2.imshow('result', img)
        #print(cv2.waitKey(1))
        if cv2.waitKey(1) == 27: # 27 is ASCII code for Esc
            break
    cap.release()
    cv2.destroyAllWindows()
                       
                       
