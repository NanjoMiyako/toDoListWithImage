#coding:utf-8
import tkinter
from PIL import Image, ImageTk

# windowを描画
window = tkinter.Tk()
# windowサイズを変更
window.geometry("600x400")
# windowタイトルを設定
window.title("Welcome to the Tkinter")

# 画像を表示するための準備
#img = Image.open('test1.png')
#img = ImageTk.PhotoImage(img)
img2 = tkinter.PhotoImage(file='test2.png')
# 画像を表示するためのキャンバスの作成（黒で表示）
canvas = tkinter.Canvas(bg = "black", width=400, height=300)
canvas.place(x=100, y=50) # 左上の座標を指定
# キャンバスに画像を表示する。第一引数と第二引数は、x, yの座標
canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)

window.mainloop()