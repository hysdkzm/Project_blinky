import cv2
import numpy as np
from glob import glob


def check(data, delta=0):
    for i in range(len(data)):
        if (data[i][0] <= 0) & (data[i][2] > 0):
            delta += data[i][2]
            data[..., 0] = data[..., 0] - data[i][2]
            data[..., 2] = data[..., 2] - data[i][2]
            print(data)
            print(delta)
            delta = check(data, delta)
            break
    return delta

def delete(n, data, center, mask_gray, mask_pink, area = 100):
    delnum = 0
    for i in range(n):
        phi = (H/2. - center[i-delnum][1] - H*3//5) * np.pi / H
        print(np.sum(mask_gray[data[i-delnum][1]: data[i-delnum][3], data[i-delnum][0]:data[i-delnum][2]]))
        if (np.sum(mask_gray[data[i-delnum][1]: data[i-delnum][3], data[i-delnum][0]:data[i-delnum][2]]) < 255*50) or (data[i-delnum][4] < area * (1 / np.cos(phi))):

            mask_pink[data[i-delnum][1]: data[i-delnum][3], data[i-delnum][0]:data[i-delnum][2]] = 0
            data = np.delete(data, i-delnum, 0)
            center = np.delete(center, i-delnum, 0)
            delnum += 1
    n -= delnum
    return n, data, center

data = glob("gray1.jpg")
data.sort()
count = 0
for j, path in enumerate(data):
    count += 1
    print("")
    print(count)
    print("")

    # 画像読み込み
    img = cv2.imread(path)
    H, W, C = img.shape

    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_gray = np.array([0, 30, 120])
    upper_gray = np.array([180, 80, 250])
    lower_pink = np.array([135, 60, 60])
    upper_pink = np.array([165, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask_gray = cv2.inRange(hsv, lower_gray, upper_gray)
    mask_pink = cv2.inRange(hsv, lower_pink, upper_pink)

    cv2.imwrite("gray/HSV_origin"+str(count)+".jpg", mask_pink)
    cv2.imwrite("gray/HSV_origin_gray"+str(count)+".jpg", mask_gray)

    # mask前処理
    #mask = mask - open1
    #mask[mask < 255] = 0

    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(mask_pink, cv2.MORPH_OPEN, kernel, iterations=1)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=1)

    cv2.imwrite("gray/HSV_closing"+str(count)+".jpg", closing)


    # ラベリング処理
    label = cv2.connectedComponentsWithStats(closing)


    # オブジェクト情報を項目別に抽出
    n = label[0] - 1
    data = np.delete(label[2], 0, 0)
    center = np.delete(label[3], 0, 0)

    data[..., 2] = data[..., 0] + data[..., 2]
    data[..., 3] = data[..., 1] + data[..., 3]
    delta = check(data)
    print(data)
    if (delta != 0):
        tmp = closing.copy()
        closing[:, :W-delta] = tmp[:, delta:]
        closing[:, W-delta:] = tmp[:, :delta]

        # ラベリング処理
        label = cv2.connectedComponentsWithStats(closing)

        # オブジェクト情報を項目別に抽出
        n = label[0] - 1
        data = np.delete(label[2], 0, 0)
        center = np.delete(label[3], 0, 0)

        data[..., 2] = data[..., 0] + data[..., 2]
        data[..., 3] = data[..., 1] + data[..., 3]

    if (n > 3):
        print(n)
        print("")
        n, data, center = delete(n, data, center, mask_gray, mask_pink)
        print(n)
        print("")
    # ラベリング結果書き出し用に二値画像をカラー変換
    color_src01 = cv2.cvtColor(closing, cv2.COLOR_GRAY2BGR)
    color_src02 = cv2.cvtColor(closing, cv2.COLOR_GRAY2BGR)

    # Thetaを中心にしたx-y座標
    xy = np.zeros((len(center), 2), dtype=np.float)

    
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img, img, mask=closing)

    cv2.imwrite("gray/HSV"+str(count)+".jpg", res)

    cv2.imwrite("gray/color_src01_"+str(count)+".jpg", color_src01)
    cv2.imwrite("gray/color_src02_"+str(count)+".jpg", color_src02)