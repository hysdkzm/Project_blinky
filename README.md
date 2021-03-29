# Project_blinky
## 林田担当
### 全天球カメラからRGB値の時系列データを取得(ブリンキーの位置は決め打ち)
### 開発環境
・windows10 home & WSL2<br>
・python<br>
・全天球カメラ RICOH THETA V<br>
**・RICOH アプリケーション（全天球球面画像　⇒　全天球平面画像）**<br>
⇒　平面動画としてmp4形式で保存できる<br>
[パソコン用基本アプリ](https://theta360.com/ja/about/application/pc.html)
※撮影時はスマホ用アプリからbluetoothで遠隔撮影

### ファイルについて

主に使ったのはpixel_img.py,pixel.py,kiridashi.py

動画撮影　**（THETA V）**<br>
⇒　平面動画に変換　**（PCアプリ）** <br>
⇒　フレームで切り出し　**（kiridashi.py）** <br>
⇒　ブリンキーの位置を決め打ち　**(pixel_img.pyで位置を取得)** <br>
⇒　動画からRGB値取得　**(pixel.pyで時系列データをcsvとして保存)** <br>

