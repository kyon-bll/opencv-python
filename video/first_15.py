import numpy as np
import cv2

cap = cv2.VideoCapture('killlakill.mp4')
fps = cap.get(5)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
w = int(cap.get(3))
h = int(cap.get(4))
out = cv2.VideoWriter('killlakill-15.mp4',fourcc, fps, (w, h))

n_frame = 0

while(n_frame / fps <= 15):
    n_frame += 1

    ret, frame = cap.read()

    out.write(frame)

    # Display the resulting frame

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
