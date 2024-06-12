import cv2
import numpy as np

video = cv2.VideoCapture("no_fire.mov")

while True:
    ret, frame = video.read()
    widht = int(video.get(3))
    height = int(video.get(4))
     
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower = np.array([0, 0, 0])
    upper = np.array([0, 0, 255])
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    print(int(cv2.countNonZero(mask)))
    
    cv2.imshow("Video", res)
    
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()