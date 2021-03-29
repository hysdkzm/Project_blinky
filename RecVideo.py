import numpy as np
import cv2
import time
from datetime import datetime

cap = cv2.VideoCapture(0)#使用するカメラの設定。PCのカメラは0、産業用カメラは1

#fps = int(cap.get(cv2.CAP_PROP_FPS))
fps = 20.0             # カメラのFPSを設定(使用するカメラで変える)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))              #カメラの横幅を取得
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))             #カメラの縦幅を取得
print(fps)
print(w)
print(h)
fourcc = cv2.VideoWriter_fourcc(*'DIVX') #ここで動画のファイル形式を決める？
out = cv2.VideoWriter('originalRGB.avi',fourcc, fps, (w,h)) #保存名を設定
g_out = cv2.VideoWriter('originalGray01.avi',fourcc, fps, (w,h),False)

start_time = time.time()
i = 0
while(True):
    ret, frame = cap.read()
    g_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    g_out.write(g_frame)
    cv2.imshow('frame',frame)
    i = i + 1
    #1000フレーム撮影したら終了
    if i >= 1000:
        elapsed_time = time.time() - start_time
        print(elapsed_time)
        break
    #qを押したら終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
g_out.release()
cv2.destroyAllWindows()