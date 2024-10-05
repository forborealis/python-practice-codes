import pyautogui
import numpy as np
import cv2

resolution = (1920, 1080)

codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "Recording.avi"
fps = 20.0

videowriter_obj = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Recording", 480, 270)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    videowriter_obj.write(frame)
    cv2.imshow("Recording", frame)
    if cv2.waitKey(1)==ord('q'):
        break

videowriter_obj.release()

cv2.destroyAllWindows()