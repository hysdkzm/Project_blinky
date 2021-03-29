import cv2
import numpy as np
from glob import glob

# 分断されたオブジェクトの編集
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


movie = glob("C:/Users/kazum/python/tmp/red1.MP4")
movie.sort()
count = 0

for i, path in enumerate(movie):
    count += 1
    print(count)
    # VideoCapture を作成する。
    cap = cv2.VideoCapture(path)
    W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    C = 3
    fps = cap.get(cv2.CAP_PROP_FPS)

    path_w = "pointmovie" + str(count) + ".txt"

    # VideoWriter を作成する。
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    writer_p = cv2.VideoWriter("result_pink_"+str(count)+".MP4", fourcc, fps, (W, H*2//5))
    writer_g = cv2.VideoWriter("result_gray_"+str(count)+".MP4", fourcc, fps, (W, H*2//5))
    writer_b = cv2.VideoWriter("result_black_"+str(count)+".MP4", fourcc, fps, (W, H*2//5))

    num = 0

    while True:
        num += 1
        # 1フレームずつ取得する。
        ret, frame = cap.read()
        if not ret:
            break  # 映像取得に失敗

        img_ = frame


        # 机のみを見るように画像を横に分割

        img = img_[H*3//5:, :]

        # Convert BGR to HSV
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # define range of blue color in HSV
        lower_black = np.array(20)
        upper_black = np.array(70)
        lower_gray = np.array([0, 30, 120])
        upper_gray = np.array([180, 90, 230])
        lower_pink = np.array([360, 70, 100])
        upper_pink = np.array([360, 100, 100])

        # Threshold the HSV image to get only blue colors
        mask_black = cv2.inRange(gray, lower_black, upper_black)
        mask_gray = cv2.inRange(hsv, lower_gray, upper_gray)
        mask_pink = cv2.inRange(hsv, lower_pink, upper_pink)


        kernel = np.ones((3, 3), np.uint8)
        closing = cv2.morphologyEx(mask_pink, cv2.MORPH_CLOSE, kernel, iterations=2)
        opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel, iterations=2)


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

        # Thetaを中心にしたx-y座標
        xy = np.zeros((len(center), 2), dtype=np.float)

        # オブジェクト情報を利用してラベリング結果を画面に表示
        for i in range(n):

            # 各オブジェクトの外接矩形を赤枠で表示
            x0 = data[i][0]
            y0 = data[i][1]
            x1 = data[i][2]
            y1 = data[i][3]
            cv2.rectangle(color_src_p, (x0, y0), (x1, y1), (0, 0, 255), 3)
            cv2.rectangle(color_src_g, (x0, y0), (x1, y1), (0, 0, 255), 3)
            cv2.rectangle(color_src_b, (x0, y0), (x1, y1), (0, 0, 255), 3)

            # xy座標に変換(cm)
            theta = 2. * np.pi * (center[i][0] + delta) / W
            phi = (H/2. - center[i][1] - H*3//5) * np.pi / H
            r = 35.8 / np.abs(np.tan(phi))
            xy[i][0] = -r * np.sin(theta)
            xy[i][1] = -r * np.cos(theta)

            # 各オブジェクトのラベル番号と面積に黄文字で表示
            #cv2.putText(color_src01, "X: " + str(xy[i][0]), (x1 - 20, y1 + 15), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))
            #cv2.putText(color_src01, "Y: " + str(xy[i][1]), (x1 - 20, y1 + 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))

        print(data)

        if (num == 1):
            with open(path_w, mode='w') as f:
                f.writelines("\n" + str(num) + "\n")
                f.writelines(str(xy))
                f.writelines("\n\n")
        else:
            with open(path_w, mode='a') as f:
                f.writelines("\n" + str(num) + "\n")
                f.writelines(str(xy))
                f.writelines("\n\n")

        writer_p.write(color_src_p)
        writer_g.write(color_src_g)
        writer_b.write(color_src_b)

    writer_p.release()
    writer_g.release()
    writer_b.release()
    cap.release()
