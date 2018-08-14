import cv2

cap = cv2.VideoCapture('killlakill-15.mp4')
fps = cap.get(5)
w = int(cap.get(3))
h = int(cap.get(4))
frame_count = int(cap.get(7))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('draw.mp4', fourcc, fps, (w, h))

for f in range(frame_count):
    ret, frame = cap.read()

    frame = cv2.rectangle(frame, (int(w/5), int(4*h/5)), (int(4*w/5), h), 0, -1)

    font = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(frame, 'Kill La Kill', (int(w/5), 0), font, 3, (255, 255, 255), 2, cv2.LINE_AA)

    out.write(frame)

    cv2.imshow('frame', frame)

cap.release()
out.release()
cv2.destroyAllWindows()
