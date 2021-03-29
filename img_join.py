import cv2
import glob
import os
import shutil
import time

"""
parameta
"""
frame_size = -1  #FHD=0, 4K=1
frame_rate = 29.97  #FPS

"""
end
"""

""" size set"""
if frame_size == 0:
    #FHD Timelaps動画用
    width = 3840
    height = 1920
elif frame_size ==1:
    #4K Timelasp動画用
    width = 3840
    height = 1920
else:
    #小さめに作る
    width = 3840
    height = 1920

""" """


def timelaps(images):
    
    
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    video = cv2.VideoWriter('D:/0125sample/test3/10.mp4', fourcc, frame_rate, (width, height))
    
    
    print("動画変換中...")
    
    for i in range(len(images)):
        img = cv2.imread(images[i])
        img = cv2.resize(img,(width,height))
        video.write(img) 
        
    
    video.release()
    print("動画変換完了")
    

if __name__ == '__main__':
    
    start = time.time()
    
    images = sorted(glob.glob('D:/0125sample/test3/10/*.jpg'))
    print("画像の総枚数{0}".format(len(images)))
    timelaps(images)

    elapsed_time = time.time() - start
    print ("処理にかかった時間は:{0}".format(elapsed_time) + "[sec]")