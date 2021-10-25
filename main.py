import cv2 as cv

path = 0 # 'people.mp4'
video = cv.VideoCapture(path)

subtractor = cv.createBackgroundSubtractorMOG2(100, 50)

while True:
    ret, frame = video.read()

    if(ret):
        mask = subtractor.apply(frame)
        cv.imshow('Movements', mask)

        if cv.waitKey(5) == ord('X'):
            break
    else:
        video = cv.VideoCapture(path)

cv.destroyAllWindows()
video.release()