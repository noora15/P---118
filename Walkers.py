# import the opencv library
import cv2

# Define a video capture object
vid = cv2.VideoCapture('walking.avi')
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
while(True):
    # roi - region of interest
    # Capture the video frame by frame
    ret, frame = vid.read()
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodies = body_cascade.detectMultiScale(gray,1.1,5)
    for (x,y,w,h) in bodies:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    # Display the resulting frame
    cv2.imshow("Web cam", frame)
      
    # Quit Window by Spacebar Key
    if cv2.waitKey(25) == 32:
        break
  
# After the loop release the cap object
vid.release()

# Destroy all the windows
