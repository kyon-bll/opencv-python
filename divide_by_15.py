import cv2

cap = cv2.VideoCapture('killlakill-32.mp4')
fps = cap.get(5)
w = int(cap.get(3))
h = int(cap.get(4))
frame_count = int(cap.get(7))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

n_movie = 0

def frame2sec(frame, fps=fps):
    return frame / fps
sec = frame2sec(frame_count)

for n_frame in range(frame_count):    
    
    ret, frame = cap.read()

    if n_movie * 15 <= frame2sec(n_frame, fps):
        movie_name = 'killlakill_{}-{}.mp4'.format(n_movie*15, n_movie*15 + 15)
        if n_movie*15 + 15 >= sec:
            movie_name = 'killlakill_{}-{}.mp4'.format(n_movie*15, int(sec))
        out = cv2.VideoWriter(movie_name, fourcc, fps, (w, h))
        n_movie += 1

    out.write(frame)

    # Display the resulting frame

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
