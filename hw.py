import cv2

haarcascade = "left eye.xml"
video = "left eye.mp4"

eye_video = cv2.VideoCapture(video)

eyecascade = cv2.CascadeClassifier(haarcascade)

while True:
    status,frame = eye_video.read()
    grey_eye = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    eyes = eyecascade.detectMultiScale(grey_eye)

    for(x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y), (x+w,y+h), (255,0,0), 3)


    cv2.imshow("eye detection", frame)
    if cv2.waitKey(10) == 27:
        break