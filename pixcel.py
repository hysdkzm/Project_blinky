#-*- coding:utf-8 -*-
import cv2
import csv
import os
import numpy as np
from PIL import Image
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pylab as plt
import scipy.signal as sg
import time
import pandas as pd
fig, (ax00,ax01,ax02,ax03,ax04,ax05,ax06,ax07) = plt.subplots(nrows=1, ncols=8, sharey=True)
plt.suptitle('ax00          ||    ax01          ||    ax02          ||   ax03          ||    ax04          ||   ax05          ||   ax06          ||   ax07          ||')
#fig.ax01.suptitle('Multi HBars2')
x1=980
y1=525
x2=1004
y2=525
x3=980
y3=542
r1,g1,b1,r2,g2,b2,r3,g3,b3=[],[],[],[],[],[],[],[],[]
r4,g4,b4,r5,g5,b5,r6,g6,b6=[],[],[],[],[],[],[],[],[]
r7,g7,b7,r8,g8,b8=[],[],[],[],[],[]
time=[]
filepath = "D:/0125sample/mix3.mp4"
count=0
count1=1
# # 動画の読み込み
cap = cv2.VideoCapture(filepath)
fps = int(cap.get(cv2.CAP_PROP_FPS))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fcount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("fps:",fps)
print("size:",width,height)
print("frame:",fcount)
# print("time:",duration)
# # 動画終了まで繰り返し

boxFromX1 = 225#対象範囲開始位置 X座標
boxFromY1 = 985 #対象範囲開始位置 Y座標
boxToX1 = 270 #対象範囲終了位置 X座標
boxToY1 = 1020 #対象範囲終了位置 Y座標
boxFromX2 = 730 #対象範囲開始位置 X座標
boxFromY2 = 985 #対象範囲開始位置 Y座標
boxToX2 = 785 #対象範囲終了位置 X座標
boxToY2 = 1020 #対象範囲終了位置 Y座標
boxFromX3 = 1262 #対象範囲開始位置 X座標
boxFromY3 = 985 #対象範囲開始位置 Y座標
boxToX3 = 1305 #対象範囲終了位置 X座標
boxToY3 = 1020 #対象範囲終了位置 Y座標
boxFromX4 = 1670 #対象範囲開始位置 X座標
boxFromY4 = 985 #対象範囲開始位置 Y座標
boxToX4 = 1708 #対象範囲終了位置 X座標
boxToY4 = 1020 #対象範囲終了位置 Y座標
boxFromX5 = 2145  #対象範囲開始位置 X座標(2080,980),(2140,1020)
boxFromY5 = 985 #対象範囲開始位置 Y座標
boxToX5 = 2185 #対象範囲終了位置 X座標
boxToY5 = 1020 #対象範囲終了位置 Y座標
boxFromX6 = 2620  #対象範囲開始位置 X座標(2080,980),(2140,1020)
boxFromY6 = 985 #対象範囲開始位置 Y座標
boxToX6 = 2665 #対象範囲終了位置 X座標
boxToY6 = 1020 #対象範囲終了位置 Y座標
boxFromX7 = 3110  #対象範囲開始位置 X座標(2080,980),(2140,1020)
boxFromY7 = 985 #対象範囲開始位置 Y座標
boxToX7 = 3155 #対象範囲終了位置 X座標
boxToY7 = 1025 #対象範囲終了位置 Y座標
boxFromX8 = 3590  #対象範囲開始位置 X座標(2080,980),(2140,1020)
boxFromY8 = 985 #対象範囲開始位置 Y座標
boxToX8 = 3635 #対象範囲終了位置 X座標
boxToY8 = 1025 #対象範囲終了位置 Y座標


    # img = cv2.rectangle(img,(160,985),(220,1025),(0,0,255),3)
    # img = cv2.rectangle(img,(635,985),(695,1025),(0,0,255),3)
    # img = cv2.rectangle(img,(1110,980),(1170,1020),(0,0,255),3)
    # img = cv2.rectangle(img,(1590,980),(1650,1020),(0,0,255),3)
    # img = cv2.rectangle(img,(2080,980),(2140,1020),(0,0,255),3)
    # img = cv2.rectangle(img,(2540,980),(2600,1020),(0,0,255),3)
    # img = cv2.rectangle(img,(3075,985),(3135,1025),(0,0,255),3)
    # img = cv2.rectangle(img,(3520,985),(3580,1025),(0,0,255),3)
# y:y+h, x:x+w　の順で設定





while(cap.isOpened()):
#     # フレームを取得
    ret, frame = cap.read()
    duration = count1/fps
    seconds = duration%60
    time.append(seconds)
    # if seconds==5.0:
    print("time:",seconds,"s")
    # 対象画像読み込み
    #img = cv2.imread(frame,cv2.IMREAD_COLOR)
    #print(frame)
# 対象範囲を切り出し
    imgBox1 = frame[boxFromY1: boxToY1, boxFromX1: boxToX1]
    imgBox2 = frame[boxFromY2: boxToY2, boxFromX2: boxToX2]
    imgBox3 = frame[boxFromY3: boxToY3, boxFromX3: boxToX3]
    imgBox4 = frame[boxFromY4: boxToY4, boxFromX4: boxToX4]
    imgBox5 = frame[boxFromY5: boxToY5, boxFromX5: boxToX5]
    imgBox6 = frame[boxFromY6: boxToY6, boxFromX6: boxToX6]
    imgBox7 = frame[boxFromY7: boxToY7, boxFromX7: boxToX7]
    imgBox8 = frame[boxFromY8: boxToY8, boxFromX8: boxToX8]
    
# RGB平均値を出力
# flattenで一次元化しmeanで平均を取得 
    b1.append(imgBox1.T[0].flatten().mean())
    g1.append(imgBox1.T[1].flatten().mean())
    r1.append(imgBox1.T[2].flatten().mean())
    b=b1[count]
    g=g1[count]
    r=r1[count]
    frame = cv2.rectangle(frame,(boxFromX1,boxFromY1),(boxToX1,boxToY1),(0,0,255),1)
# RGB平均値を出力
# flattenで一次元化しmeanで平均を取得 
    b2.append(imgBox2.T[0].flatten().mean())
    g2.append(imgBox2.T[1].flatten().mean())
    r2.append(imgBox2.T[2].flatten().mean())
    # b=b1[count]
    # g=g1[count]
    # r=r1[count]
    frame = cv2.rectangle(frame,(boxFromX2,boxFromY2),(boxToX2,boxToY2),(0,0,255),1)
# RGB平均値を出力
# flattenで一次元化しmeanで平均を取得 
    b3.append(imgBox3.T[0].flatten().mean())
    g3.append(imgBox3.T[1].flatten().mean())
    r3.append(imgBox3.T[2].flatten().mean())
    # b=b1[count]
    # g=g1[count]
    # r=r1[count]
    frame = cv2.rectangle(frame,(boxFromX3,boxFromY3),(boxToX3,boxToY3),(0,0,255),1)
# RGB平均値を出力
# flattenで一次元化しmeanで平均を取得 
    b4.append(imgBox4.T[0].flatten().mean())
    g4.append(imgBox4.T[1].flatten().mean())
    r4.append(imgBox4.T[2].flatten().mean())
    # b=b1[count]
    # g=g1[count]
    # r=r1[count]
    frame = cv2.rectangle(frame,(boxFromX4,boxFromY4),(boxToX4,boxToY4),(0,0,255),1)
    # RGB平均値を出力
# flattenで一次元化しmeanで平均を取得 
    b5.append(imgBox5.T[0].flatten().mean())
    g5.append(imgBox5.T[1].flatten().mean())
    r5.append(imgBox5.T[2].flatten().mean())
    # b=b1[count]
    # g=g1[count]
    # r=r1[count]
    frame = cv2.rectangle(frame,(boxFromX5,boxFromY5),(boxToX5,boxToY5),(0,0,255),1)
    # RGB平均値を出力
# flattenで一次元化しmeanで平均を取得 
    b6.append(imgBox6.T[0].flatten().mean())
    g6.append(imgBox6.T[1].flatten().mean())
    r6.append(imgBox6.T[2].flatten().mean())
    # b=b1[count]
    # g=g1[count]
    # r=r1[count]
    frame = cv2.rectangle(frame,(boxFromX6,boxFromY6),(boxToX6,boxToY6),(0,0,255),1)
    # RGB平均値を出力
# flattenで一次元化しmeanで平均を取得 
    b7.append(imgBox7.T[0].flatten().mean())
    g7.append(imgBox7.T[1].flatten().mean())
    r7.append(imgBox7.T[2].flatten().mean())
    # b=b1[count]
    # g=g1[count]
    # r=r1[count]
    frame = cv2.rectangle(frame,(boxFromX7,boxFromY7),(boxToX7,boxToY7),(0,0,255),1)
    # RGB平均値を出力
# flattenで一次元化しmeanで平均を取得 
    b8.append(imgBox8.T[0].flatten().mean())
    g8.append(imgBox8.T[1].flatten().mean())
    r8.append(imgBox8.T[2].flatten().mean())
    # b=b1[count]
    # g=g1[count]
    # r=r1[count]
    frame = cv2.rectangle(frame,(boxFromX8,boxFromY8),(boxToX8,boxToY8),(0,0,255),1)
    
# RGB平均値を取得
    # print("R: %.2f" % (r))
    # print("G: %.2f" % (g))
    # print("B: %.2f" % (b))
#plotした関数を表示する。
    ax00.plot(range(count), r1[:count], color="r", marker='.')
    ax00.plot(range(count), g1[:count], color="g", marker='.')
    ax00.plot(range(count), b1[:count], color="b", marker='.')
    ax01.plot(range(count), r2[:count], color="r", marker='.')
    ax01.plot(range(count), g2[:count], color="g", marker='.')
    ax01.plot(range(count), b2[:count], color="b", marker='.')
    ax02.plot(range(count), r3[:count], color="r", marker='.')
    ax02.plot(range(count), g3[:count], color="g", marker='.')
    ax02.plot(range(count), b3[:count], color="b", marker='.')
    ax03.plot(range(count), r4[:count], color="r", marker='.')
    ax03.plot(range(count), g4[:count], color="g", marker='.')
    ax03.plot(range(count), b4[:count], color="b", marker='.')
    ax04.plot(range(count), r5[:count], color="r", marker='.')
    ax04.plot(range(count), g5[:count], color="g", marker='.')
    ax04.plot(range(count), b5[:count], color="b", marker='.')
    ax05.plot(range(count), r6[:count], color="r", marker='.')
    ax05.plot(range(count), g6[:count], color="g", marker='.')
    ax05.plot(range(count), b6[:count], color="b", marker='.')
    ax06.plot(range(count), r7[:count], color="r", marker='.')
    ax06.plot(range(count), g7[:count], color="g", marker='.')
    ax06.plot(range(count), b7[:count], color="b", marker='.')
    ax07.plot(range(count), r8[:count], color="r", marker='.')
    ax07.plot(range(count), g8[:count], color="g", marker='.')
    ax07.plot(range(count), b8[:count], color="b", marker='.')

    #print(count)
    # if r>200:
    #     print("Rが200以上：",count+1)
    if count1==(fcount):
        #cv2.imwrite("rect_text.jpg", frame)
        ax00.plot(range(count), r1[:count], color="r", marker='.')
        ax00.plot(range(count), g1[:count], color="g", marker='.')
        ax00.plot(range(count), b1[:count], color="b", marker='.')
        ax01.plot(range(count), r2[:count], color="r", marker='.')
        ax01.plot(range(count), g2[:count], color="g", marker='.')
        ax01.plot(range(count), b2[:count], color="b", marker='.')
        ax02.plot(range(count), r3[:count], color="r", marker='.')
        ax02.plot(range(count), g3[:count], color="g", marker='.')
        ax02.plot(range(count), b3[:count], color="b", marker='.')
        ax03.plot(range(count), r4[:count], color="r", marker='.')
        ax03.plot(range(count), g4[:count], color="g", marker='.')
        ax03.plot(range(count), b4[:count], color="b", marker='.')
        ax04.plot(range(count), r5[:count], color="r", marker='.')
        ax04.plot(range(count), g5[:count], color="g", marker='.')
        ax04.plot(range(count), b5[:count], color="b", marker='.')
        ax05.plot(range(count), r6[:count], color="r", marker='.')
        ax05.plot(range(count), g6[:count], color="g", marker='.')
        ax05.plot(range(count), b6[:count], color="b", marker='.')
        ax06.plot(range(count), r7[:count], color="r", marker='.')
        ax06.plot(range(count), g7[:count], color="g", marker='.')
        ax06.plot(range(count), b7[:count], color="b", marker='.')
        ax07.plot(range(count), r8[:count], color="r", marker='.')
        ax07.plot(range(count), g8[:count], color="g", marker='.')
        ax07.plot(range(count), b8[:count], color="b", marker='.')
        # plt.show()
        # print(b5[128])
        # print(g5[128])
        df_time=pd.Series(time,index=[i for i in range(len(time))]).T
        df_r1=pd.Series(r1,index=[i for i in range(len(r1))]).T
        df_b1=pd.Series(b1,index=[i for i in range(len(b1))]).T
        df_g1=pd.Series(g1,index=[i for i in range(len(g1))]).T
        df_r2=pd.Series(r2,index=[i for i in range(len(r2))]).T
        df_b2=pd.Series(b2,index=[i for i in range(len(b2))]).T
        df_g2=pd.Series(g2,index=[i for i in range(len(g2))]).T
        df_r3=pd.Series(r3,index=[i for i in range(len(r3))]).T
        df_b3=pd.Series(b3,index=[i for i in range(len(b3))]).T
        df_g3=pd.Series(g3,index=[i for i in range(len(g3))]).T
        df_r4=pd.Series(r4,index=[i for i in range(len(r4))]).T
        df_b4=pd.Series(b4,index=[i for i in range(len(b4))]).T
        df_g4=pd.Series(g4,index=[i for i in range(len(g4))]).T
        df_r5=pd.Series(r5,index=[i for i in range(len(r5))]).T
        df_b5=pd.Series(b5,index=[i for i in range(len(b5))]).T
        df_g5=pd.Series(g5,index=[i for i in range(len(g5))]).T
        df_r6=pd.Series(r6,index=[i for i in range(len(r6))]).T
        df_b6=pd.Series(b6,index=[i for i in range(len(b6))]).T
        df_g6=pd.Series(g6,index=[i for i in range(len(g6))]).T
        df_r7=pd.Series(r7,index=[i for i in range(len(r7))]).T
        df_b7=pd.Series(b7,index=[i for i in range(len(b7))]).T
        df_g7=pd.Series(g7,index=[i for i in range(len(g7))]).T
        df_r8=pd.Series(r8,index=[i for i in range(len(r8))]).T
        df_b8=pd.Series(b8,index=[i for i in range(len(b8))]).T
        df_g8=pd.Series(g8,index=[i for i in range(len(g8))]).T
        print(df_time.shape)
        print(df_r1.shape)
        print(df_b1.shape)
        print(df_g1.shape)
        print(df_r2.shape)
        print(df_b2.shape)
        print(df_g2.shape)
        print(df_r3.shape)
        print(df_b3.shape)
        print(df_g3.shape)
        print(df_r4.shape)
        print(df_b4.shape)
        print(df_g4.shape)
        print(df_r5.shape)
        print(df_b5.shape)
        print(df_g5.shape)
        print(df_r6.shape)
        print(df_b6.shape)
        print(df_g6.shape)
        print(df_r7.shape)
        print(df_b7.shape)
        print(df_g7.shape)
        print(df_r8.shape)
        print(df_b8.shape)
        print(df_g8.shape)
        df1=pd.concat((df_time.rename("time"),df_r1.rename("r"),df_b1.rename("b"),df_g1.rename("g")),axis=1)
        df2=pd.concat((df_time.rename("time"),df_r2.rename("r"),df_b2.rename("b"),df_g2.rename("g")),axis=1)
        df3=pd.concat((df_time.rename("time"),df_r3.rename("r"),df_b3.rename("b"),df_g3.rename("g")),axis=1)
        df4=pd.concat((df_time.rename("time"),df_r4.rename("r"),df_b4.rename("b"),df_g4.rename("g")),axis=1)
        df5=pd.concat((df_time.rename("time"),df_r5.rename("r"),df_b5.rename("b"),df_g5.rename("g")),axis=1)
        df6=pd.concat((df_time.rename("time"),df_r6.rename("r"),df_b6.rename("b"),df_g6.rename("g")),axis=1)
        df7=pd.concat((df_time.rename("time"),df_r7.rename("r"),df_b7.rename("b"),df_g7.rename("g")),axis=1)
        df8=pd.concat((df_time.rename("time"),df_r8.rename("r"),df_b8.rename("b"),df_g8.rename("g")),axis=1)
        df1.to_csv("D:/0125sample/mix3_result/res1.csv")
        df2.to_csv("D:/0125sample/mix3_result/res2.csv")
        df3.to_csv("D:/0125sample/mix3_result/res3.csv")
        df4.to_csv("D:/0125sample/mix3_result/res4.csv")
        df5.to_csv("D:/0125sample/mix3_result/res5.csv")
        df6.to_csv("D:/0125sample/mix3_result/res6.csv")
        df7.to_csv("D:/0125sample/mix3_result/res7.csv")
        df8.to_csv("D:/0125sample/mix3_result/res8.csv")
        plt.show()
        cv2.imwrite("rect_text.jpg", frame)
        # with open('D:/blinky_image/0113/test2.csv','a',newline='') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(["TIME",[float(i) for i in time[:count1]]])#([1,'スパム','500円'])
        #     print(type([float(i) for i in time[:count1]]))
        # #     print(len(time))
        # #     writer.writerow(["R1",r1[:count1]])
        # #     print(len(r1))
        # #     writer.writerow(["B1",b1[:count1]])
        # #     print(len(b1))
        # #     writer.writerow(["G1",g1[:count1]])
        # #     print(len(g1))
        # #     writer.writerow(["R2",r2[:count1]])
        # #     print(len(r2))
        # #     writer.writerow(["B2",b2[:count1]])
        # #     print(len(b2))
        # #     writer.writerow(["G2",g2[:count1]])
        # #     print(len(g2))
        # #     writer.writerow(["R3",r3[:count1]])
        # #     print(len(r3))
        # #     writer.writerow(["B3",b3[:count1]])
        # #     print(len(b3))
        # #     writer.writerow(["G3",g3[:count1]])
        # #     print(len(g3))
        # #     writer.writerow(["R4",r4[:count1]])
        # #     print(len(r4))
        # #     writer.writerow(["B4",b4[:count1]])
        # #     print(len(b4))
        # #     writer.writerow(["G4",g4[:count1]])
        # #     print(len(g4))
        #     writer.writerow(["R5",[float(i) for i in r5[:count1]]])
        #     print(len(r5))
        #     writer.writerow(["B5",[float(i) for i in b5[:count1]]])
        #     print(len(b5))
        #     writer.writerow(["G5",[float(i) for i in g5[:count1]]])
        #     print(len(g5))
        #     writer.writerow(["R6",r6[:count1]])
        #     print(len(r6))
        #     writer.writerow(["B6",b6[:count1]])
        #     print(len(b6))
        #     writer.writerow(["G6",g6[:count1]])
        #     print(len(g6))
        #     writer.writerow(["R7",r7[:count1]])
        #     print(len(r7))
        #     writer.writerow(["B7",b7[:count1]])
        #     print(len(b7))
        #     writer.writerow(["G7",g7[:count1]])
        #     print(len(g7))
        #     writer.writerow(["R8",r8[:count1]])
        #     print(len(r8))
        #     writer.writerow(["B8",b8[:count1]])
        #     print(len(b8))
        #     writer.writerow(["G8",g8[:count1]])
        #     print(len(g8))
        # print("time",time[:count],"RGB1",r1[:count],g1[:count],b1[:count])
        # print("time",time[:count],"RGB2",r2[:count],g2[:count],b2[:count])
    count=count+1
    count1=count1+1
# #     # フレームを表示
    #cv2.imshow("Frame", frame)
#      # qキーが押されたら途中終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        plt.show()
        cv2.imwrite("rect_text.jpg", frame)
        #print("\ntime",time[:count],"\n\nRGB1",r1[:count],g1[:count],b1[:count],"\n\nRGB2",r2[:count],g2[:count],b2[:count])
        #print("\ntime",time[:count],"\nRGB2",r2[:count],g2[:count],b2[:count])
#         print(r1)
        break
cap.release()
cv2.destroyAllWindows()



# from PIL import Image
# from PIL import Image, ImageDraw
# img_path="./01484.jpg"
# x=240
# y=160
#“linspace(開始値，終了値，分割数)”で，線形数列を作成。
#“linspace(開始値，終了値，分割数)”で，線形数列を作成。
#数列をsinの引数に入れると，sin(x)の数列が生成される。
#plot(x, y, linewidth=1)で，線色を設定。

# im = Image.open(img_path).convert('RGB')
# r, g, b = im.getpixel((x, y))
# a = (r, g, b)
# draw = ImageDraw.Draw(im)
# draw.rectangle((x, y, x+5, y+5), fill=(0, 192, 192), outline=(255, 255, 255))
# im.save('./pillow_imagedraw.jpg', quality=95)
# print(a)

# # 対象画像読み込み
# img = cv2.imread(img_path,cv2.IMREAD_COLOR)
# print(img)
# # 対象範囲を切り出し
# boxFromX = x #対象範囲開始位置 X座標
# boxFromY = y #対象範囲開始位置 Y座標
# boxToX = x+5 #対象範囲終了位置 X座標
# boxToY = y+5 #対象範囲終了位置 Y座標
# # y:y+h, x:x+w　の順で設定
# imgBox = img[boxFromY: boxToY, boxFromX: boxToX]

# # RGB平均値を出力
# # flattenで一次元化しmeanで平均を取得 
# b = imgBox.T[0].flatten().mean()
# g = imgBox.T[1].flatten().mean()
# r = imgBox.T[2].flatten().mean()

# img = cv2.rectangle(img,(boxFromX,boxFromY),(boxToX,boxToY),(0,0,255),1)
# cv2.imwrite("rect_text.jpg", img)
# # RGB平均値を取得
# print("R: %.2f" % (r))
# print("G: %.2f" % (g))
# print("B: %.2f" % (b))

