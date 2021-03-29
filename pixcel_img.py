from PIL import Image
from PIL import Image, ImageDraw
import cv2
img_path="./out/img__020.jpg"
x=2550
y=1000
# “linspace(開始値，終了値，分割数)”で，線形数列を作成。
# “linspace(開始値，終了値，分割数)”で，線形数列を作成。
# 数列をsinの引数に入れると，sin(x)の数列が生成される。
# plot(x, y, linewidth=1)で，線色を設定。
# im = Image.open(img_path).convert('RGB')
# #r, g, b = im.getpixel((x, y))
# #a = (r, g, b)
# draw = ImageDraw.Draw(im)
# draw.rectangle((x, y, x+5, y+5), fill=(0, 192, 192), outline=(255, 255, 255))
# im.save('./pillow_imagedraw.jpg', quality=95)
#print(a)
# 対象画像読み込み
img = cv2.imread("D:/0125sample/mix3/img__040.jpg",cv2.IMREAD_COLOR)
#print(img)
# 対象範囲を切り出し

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
# y:y+h, x:x+w　の順で設定
imgBox = img[boxFromY1: boxToY1, boxFromX1: boxToX1]
imgBox = img[boxFromY2: boxToY2, boxFromX2: boxToX2]
imgBox = img[boxFromY3: boxToY3, boxFromX3: boxToX3]
imgBox = img[boxFromY4: boxToY4, boxFromX4: boxToX4]
imgBox = img[boxFromY5: boxToY5, boxFromX5: boxToX5]
imgBox = img[boxFromY6: boxToY6, boxFromX6: boxToX6]
imgBox = img[boxFromY7: boxToY7, boxFromX7: boxToX7]
imgBox = img[boxFromY8: boxToY8, boxFromX8: boxToX8]
# RGB平均値を出力
# flattenで一次元化しmeanで平均を取得 
# b = imgBox.T[0].flatten().mean()
# g = imgBox.T[1].flatten().mean()
# r = imgBox.T[2].flatten().mean()
#imgBox5 = img[boxFromY5: boxToY5, boxFromX5: boxToX5]
img = cv2.rectangle(img,(boxFromX1,boxFromY1),(boxToX1,boxToY1),(0,0,255),2)
img = cv2.rectangle(img,(boxFromX2,boxFromY2),(boxToX2,boxToY2),(0,0,255),2)
img = cv2.rectangle(img,(boxFromX3,boxFromY3),(boxToX3,boxToY3),(0,0,255),2)
img = cv2.rectangle(img,(boxFromX4,boxFromY4),(boxToX4,boxToY4),(0,0,255),2)
img = cv2.rectangle(img,(boxFromX5,boxFromY5),(boxToX5,boxToY5),(0,0,255),2)
img = cv2.rectangle(img,(boxFromX6,boxFromY6),(boxToX6,boxToY6),(0,0,255),2)
img = cv2.rectangle(img,(boxFromX7,boxFromY7),(boxToX7,boxToY7),(0,0,255),2)
img = cv2.rectangle(img,(boxFromX8,boxFromY8),(boxToX8,boxToY8),(0,0,255),2)


# img = cv2.rectangle(img,(160,985),(220,1025),(0,0,255),3)
# img = cv2.rectangle(img,(635,985),(695,1025),(0,0,255),3)
# img = cv2.rectangle(img,(1110,980),(1170,1020),(0,0,255),3)
# img = cv2.rectangle(img,(1590,980),(1650,1020),(0,0,255),3)
# img = cv2.rectangle(img,(2080,980),(2140,1020),(0,0,255),3)
# img = cv2.rectangle(img,(2540,980),(2600,1020),(0,0,255),3)
# img = cv2.rectangle(img,(3075,985),(3135,1025),(0,0,255),3)
# img = cv2.rectangle(img,(3520,985),(3580,1025),(0,0,255),3)
cv2.imwrite("rect_text.jpg", img)
# RGB平均値を取得
# print("R: %.2f" % (r))
# print("G: %.2f" % (g))
# print("B: %.2f" % (b))
