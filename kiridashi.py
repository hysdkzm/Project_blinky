import cv2
import os
from PIL import Image
#img = Image.open('C:/Users/kazum/OneDrive/画像/test/*.jpg')
# 何らかの画像処理
#new_img.save('C:/Users/kazum/OneDrive/画像/test/new_img.jpg')
# 上記と同様の保存処理
# new_img.save('path/to/your/new_img', 'PNG')





def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            return

save_all_frames('./red1.MP4', './red1/', 'img_')

#save_all_frames('data/temp/sample_video.mp4', 'data/temp/result_png', 'sample_video_img', 'png')