import cv2
import numpy as np
from glob import glob

def check(data, delta=0):
    for i in range(len(data)):
        if (data[i][0] <= 0) & (data[i][2] > 0):
            delta += data[i][2]
            data[..., 0] = data[..., 0] - data[i][2]
            data[..., 2] = data[..., 2] - data[i][2]
            delta = check(data, delta)
            break
    return delta

def delete(n, data, center, mask_gray, mask_pink, area = 30):
    delnum = 0
    for i in range(n):
        phi = (H/2. - center[i-delnum][1] - H*3//5) * np.pi / H
        #print(np.sum(mask_gray[data[i-delnum][1]: data[i-delnum][3], data[i-delnum][0]:data[i-delnum][2]+10]))
        if (np.sum(mask_gray[data[i-delnum][1]-5: data[i-delnum][3]+5, data[i-delnum][0]:data[i-delnum][2]+10]) < 255*30*(1 / np.cos(phi))) or (data[i-delnum][4] < area * (1 / np.cos(phi))):

            #mask_pink[data[i-delnum][1]: data[i-delnum][3], data[i-delnum][0]:data[i-delnum][2]] = 0
            data = np.delete(data, i-delnum, 0)
            center = np.delete(center, i-delnum, 0)
            delnum += 1

    n -= delnum
    
    return n, data, center

# VideoCapture オブジェクトを取得します
capture = cv2.VideoCapture(0)

while(True):

    # 1フレームずつ取得する。
    ret, frame = capture.read()
    if not ret:
        break  # 映像取得に失敗


    print(capture.get(cv2.CAP_PROP_FPS))


    img_ = frame
    H, W, C = img_.shape
    print(img_.shape)

    # 机のみを見るように画像を横に分割

    img = img_

    # Convert BGR to HSV
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_black = np.array(20)
    upper_black = np.array(70)
    lower_gray = np.array([0, 30, 120])
    upper_gray = np.array([180, 90, 230])
    lower_pink = np.array([130, 70, 70])
    upper_pink = np.array([170, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask_black = cv2.inRange(gray, lower_black, upper_black)
    mask_gray = cv2.inRange(hsv, lower_gray, upper_gray)
    mask_pink = cv2.inRange(hsv, lower_pink, upper_pink)

    kernel = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(
        mask_pink, cv2.MORPH_CLOSE, kernel, iterations=2)
    opening = cv2.morphologyEx(
        closing, cv2.MORPH_OPEN, kernel, iterations=2)

    # ラベリング処理
    label = cv2.connectedComponentsWithStats(opening)

    # オブジェクト情報を項目別に抽出
    n = label[0] - 1
    data = np.delete(label[2], 0, 0)
    center = np.delete(label[3], 0, 0)

    data[..., 2] = data[..., 0] + data[..., 2]
    data[..., 3] = data[..., 1] + data[..., 3]

    delta = check(data)
    if (delta != 0):
        tmp = opening.copy()
        opening[:, :W-delta] = tmp[:, delta:]
        opening[:, W-delta:] = tmp[:, :delta]

        # ラベリング処理
        label = cv2.connectedComponentsWithStats(opening)

        # オブジェクト情報を項目別に抽出
        n = label[0] - 1
        data = np.delete(label[2], 0, 0)
        center = np.delete(label[3], 0, 0)

        data[..., 2] = data[..., 0] + data[..., 2]
        data[..., 3] = data[..., 1] + data[..., 3]

    n, data, center = delete(n, data, center, mask_gray, opening)

    # ラベリング結果書き出し用に二値画像をカラー変換
    color_src_p = cv2.cvtColor(opening, cv2.COLOR_GRAY2BGR)
    color_src_g = cv2.cvtColor(mask_gray, cv2.COLOR_GRAY2BGR)
    color_src_b = cv2.cvtColor(mask_black, cv2.COLOR_GRAY2BGR)



    cv2.imshow('frame', color_src_g)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()