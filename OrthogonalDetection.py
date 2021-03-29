import numpy as np
import matplotlib.pylab as plt
import scipy.signal as sg
import cv2
import time

#プログラムの処理時間測定開始
start = time.process_time()

#読み込む動画の指定  originalRGB2.avi
EDITED_FILE_NAME = 'originalRGB.avi'
#読み込んだ動画のプロパティ
edit = cv2.VideoCapture(EDITED_FILE_NAME)
end_flag, edit_frame = edit.read()
fps = int(edit.get(cv2.CAP_PROP_FPS))
height = int(edit.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(edit.get(cv2.CAP_PROP_FRAME_WIDTH))
fcount = int(edit.get(cv2.CAP_PROP_FRAME_COUNT))

#各フレームの各ピクセルの画素値を格納する配列(高さ＊幅＊チャンネル数＊フレーム数)
pixel_t = np.zeros((height,width,3,fcount))# チャンネル数は色の範囲のこと
# RGBで3

i = 0
#配列に格納
while end_flag == True:
    pixel_t[:,:,:,i] = edit_frame
    i = i + 1
    # 次のフレーム読み込み
    end_flag, edit_frame = edit.read()

t = np.arange(0,fcount,1)
#直交検波で用いるsin,cos波を定義
fc = 40   #検波したい周波数
sin = np.sin(2*np.pi*(fc/fps)*t)
cos = np.cos(2*np.pi*(fc/fps)*t)

#各画素の時間方向の画素値とsin,cos波の内積を計算(ブロードキャスト使用)
sin_dot = (pixel_t*sin).sum(axis = 3)
cos_dot = (pixel_t*cos).sum(axis = 3)

#それぞれの内積の二乗を足して、要素数×2で割る
A = (np.sqrt(sin_dot**2 + cos_dot**2)).sum(axis = 2)
A = A/(fcount*2)

#生成した画像を保存
plt.imsave('a_res.jpg', A, cmap = 'gray')

elapsed = (time.process_time() - start)
print(elapsed)
cv2.destroyAllWindows()
plt.show()
edit.release()