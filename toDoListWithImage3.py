
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import  Image, ImageTk

import tkinter
import numpy
import cv2


gTab1 = ''
gTab2 = ''
gTab3 = ''


gCurrentMarketURL=''
gCurrentMarketName=''
gMarketShohinList = [];

gSijoTabSijoNameLabel = ''
gSijoTabSelectBox=''
gSijoTabShohinLabel=''

gSijoTabSuishoWidthLabel=''
gSijoTabSuishoHeightLabel=''
gSijoTabPriceLabel=''


def SijoTabSelectBoxselected(event):
    global gTab1
    global gTab2
    global gTab3
    global gCurrentMarketURL
    global gCurrentMarketName
    global gMarketShohinList
    global gSijoTabSelectBox
    global gSijoTabSijoNameLabel
    global gSijoTabSuishoWidthLabel
    global gSijoTabSuishoHeightLabel
    global gSijoTabPriceLabel
   
    if not gSijoTabSelectBox.curselection():
        return 
    crSelectIdx = gSijoTabSelectBox.curselection()[0];

    
    var1 = gSijoTabSelectBox.get(crSelectIdx)
    imgURL = gCurrentMarketURL + '\\' + gMarketShohinList[crSelectIdx][2]
    img = Image.open(imgURL);
    img = img.resize((100, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img)
    gSijoTabShohinLabel.configure(image=img2)
    gSijoTabShohinLabel.image = img2
    gSijoTabShohinLabel.place(x=150, y=150)
    
    
    im2 = cv2.imread(imgURL)
    sh, sw, c = im2.shape;
    
    str1 = "推奨高さ:"+ str(sh);
    gSijoTabSuishoHeightLabel.configure(text=str1);
    
    str1 = "推奨幅:"+ str(sw);
    gSijoTabSuishoWidthLabel.configure(text=str1);
    
    str1 = "購入に必要なポイント:" + str(gMarketShohinList[crSelectIdx][3])
    gSijoTabPriceLabel.configure(text=str1);

    
    print(var1)

def main():
    global gTab1
    global gTab2
    global gTab3
    global gCurrentMarketURL
    global gCurrentMarketName
    global gMarketShohinList
    global gSijoTabSelectBox
    global gSijoTabShohinLabel


    #メインウィンドウ作成
    main_view = tkinter.Tk()
    
    #メインウィンドウタイトル設定
    main_view.title("Test title")
    
    #メインウィンドウの大きさ設定
    main_view.geometry("500x500")
    
    #メインウィンドウにnotebook作成
    nb = ttk.Notebook(main_view)
    
    gTab1 = tkinter.Frame(nb)
    gTab2 = tkinter.Frame(nb)
    gTab3 = tkinter.Frame(nb)
    
    nb.add(gTab1, text="市場", padding=3)
    nb.add(gTab2, text="tab2", padding=3)
    nb.add(gTab3, text="tab3", padding=3)
    
    #メインフレームでのnotebook配置を決定する。
    nb.pack(expand=1, fill="both")
 
    #各タブの内容を記載する。
    sijoTab_main(gTab1)
    tab2_main(gTab2)
    tab3_main(gTab3)
 
    #main_viewを表示する無限ループ
    main_view.mainloop()
 
    return 0
 
def sijoTab_main(tab1):
    global gTab1
    global gTab2
    global gTab3
    global gCurrentMarketURL
    global gCurrentMarketName
    global gMarketShohinList
    global gSijoTabSelectBox
    global gSijoTabShohinLabel
    global gSijoTabSijoNameLabel
    global gSijoTabSuishoWidthLabel
    global gSijoTabSuishoHeightLabel
    global gSijoTabPriceLabel
    
    #文字を表示する。
    title_name = tkinter.Label(gTab1, text="市場")
    title_name.place(x=10, y=30)
    
    label1 = tkinter.Label(gTab1, text="市場URL")
    label1.place(x=10, y=60)
    
    # Text
    txt = Text(gTab1, height=1, width=30)
    txt.insert(1.0, "")
    txt.place(x=100, y=60)
    
    # ボタン
    button1 = ttk.Button(
        gTab1,
        text='市場へジャンプ',
        command=lambda: jumpToSijo(txt))
    button1.place(x=10,y=90)
    
    
    gSijoTabSijoNameLabel = tkinter.Label(gTab1, text="市場名:")
    gSijoTabSijoNameLabel.place(x=10, y=120)
    
    #ListBox
    gSijoTabSelectBox = Listbox(gTab1, height=10)
    gSijoTabSelectBox.place(x=10, y=150)
    gSijoTabSelectBox.bind('<<ListboxSelect>>',SijoTabSelectBoxselected);
    
    img = Image.open("test1.png");
    img = img.resize((100, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img)
    gSijoTabShohinLabel = tkinter.Label(gTab1, image=img2)
    gSijoTabShohinLabel.image = img2
    gSijoTabShohinLabel.place(x=150, y=150)
    
    
    gSijoTabSuishoHeightLabel = tkinter.Label(gTab1, text="推奨高さ:")
    gSijoTabSuishoHeightLabel.place(x=150, y=260)
    
    gSijoTabSuishoWidthLabel = tkinter.Label(gTab1, text="推奨幅:")
    gSijoTabSuishoWidthLabel.place(x=150, y=290)
    
    gSijoTabPriceLabel = tkinter.Label(gTab1, text="購入に必要なポイント:")
    gSijoTabPriceLabel.place(x=150, y=320)
    
    return 0
    
def jumpToSijo(textBox1):
    global gTab1
    global gTab2
    global gTab3
    global gCurrentMarketURL
    global gCurrentMarketName
    global gMarketShohinList
    global gSijoTabSelectBox

    result=textBox1.get("1.0", "end")
    result = result.rstrip('\n')
    
    loadSijoData(result)
    
    
    DisplaySijoData();
    
def loadSijoData(URL):
    global gTab1
    global gTab2
    global gTab3
    global gCurrentMarketURL
    global gCurrentMarketName
    global gMarketShohinList
    global gSijoTabSelectBox
    global gSijoTabSijoNameLabel

    path1 = URL + '\MarketInfo.txt'
    
    try:
        f = open(path1, encoding='UTF-8')
    except OSError as e:
        messagebox.showinfo('エラー','URLが違っています')
        return
    else:
        gCurrentMarketURL = URL;
        lines = f.readlines()
        gCurrentMarketName=lines[0].split(',')[1];
        lines.pop(0);
        
        str1 = "市場名:"+gCurrentMarketName;
        gSijoTabSijoNameLabel.configure(text=str1);
        
        gMarketShohinList = [];
        for line in lines:
            line = line.rstrip('\n')
            vars = line.split(',');
            gMarketShohinList.append(vars) 
        
        f.close()
        
    return
    
def DisplaySijoData():
    global gTab1
    global gTab2
    global gTab3
    global gCurrentMarketURL
    global gCurrentMarketName
    global gMarketShohinList
    global gSijoTabSelectBox
    
    gSijoTabSelectBox.delete(0, tkinter.END);
    
    for s1 in gMarketShohinList:
        gSijoTabSelectBox.insert(tkinter.END, s1[1])
        
    return
        
def tab2_main(tab2):
    #文字を表示する。
    param_name = tkinter.Label(tab2, text="タブ2の内容")
    param_name.place(x=10, y=20)
    return 0
 
def tab3_main(tab3):
    #文字を表示する。
    param_name = tkinter.Label(tab3, text="タブ3の内容")
    param_name.place(x=10, y=30)
    return 0
 
if __name__ == "__main__":
    main()
    
    

