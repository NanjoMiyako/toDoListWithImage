
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import  Image, ImageTk

import tkinter
import numpy
import cv2
import os
import datetime

gSijoTab1 = ''
gTaskListTab = ''
gAddTaskTab = ''
gAddFanitureTab = ''


gCurrentMarketURL=''
gCurrentMarketName=''
gMarketShohinList = [];

gSijoTabSijoNameLabel = ''
gSijoTabSelectBox=''
gSijoTabShohinLabel=''

gSijoTabSuishoWidthLabel=''
gSijoTabSuishoHeightLabel=''
gSijoTabPriceLabel=''

gTaskDataURL=''
gGetExpVols=[10,20,30,40]
gTaskList = [];
gTaskAddCountButtons = [];
gTaskDelButtons = [];
gTaskListTabTree=''

gNanidoRadioValue = ''
gRisetSpanRadioValue = ''
gAddTaskTabTitleEntry = ''

gRoomImg=''
gAddFanitureTabPosXEntry=''
gAddFanitureTabPosYEntry=''
gAddFanitureTabSizeXEntry=''
gAddFanitureTabSizeYEntry=''

gMyFaniture=[];
gCurrentRoomImg=''
gFnPosX = ''
gFnPosY = ''
gFnSizeX = ''
gFnSizeY = ''

def SijoTabSelectBoxselected(event):
    global gSijoTab1
    global gTaskListTab
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
    global gSijoTab1
    global gTaskListTab
    global gAddTaskTab
    global gAddFanitureTab
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
    main_view.geometry("1000x500")
    
    #メインウィンドウにnotebook作成
    nb = ttk.Notebook(main_view)
    
    gSijoTab1 = tkinter.Frame(nb)
    gTaskListTab = tkinter.Frame(nb)
    gAddTaskTab = tkinter.Frame(nb)
    gAddFanitureTab = tkinter.Frame(nb)
    
    nb.add(gSijoTab1, text="市場", padding=4)
    nb.add(gTaskListTab, text="タスク一覧", padding=4)
    nb.add(gAddTaskTab, text="タスク追加", padding=4)
    nb.add(gAddFanitureTab, text="家具配置", padding=4)
    
    #メインフレームでのnotebook配置を決定する。
    nb.pack(expand=1, fill="both")
 
    #各タブの内容を記載する。
    sijoTab_main()
    gTaskListTab_main()
    gAddTaskTab_main()
    gAddFanitureTab_main()
    
 
    #main_viewを表示する無限ループ
    main_view.mainloop()
 
    return 0
 
def sijoTab_main():
    global gSijoTab1
    global gTaskListTab
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
    title_name = tkinter.Label(gSijoTab1, text="市場")
    title_name.place(x=10, y=30)
    
    label1 = tkinter.Label(gSijoTab1, text="市場URL")
    label1.place(x=10, y=60)
    
    # Text
    txt = Text(gSijoTab1, height=1, width=30)
    txt.insert(1.0, "")
    txt.place(x=100, y=60)
    
    # ボタン
    button1 = ttk.Button(
        gSijoTab1,
        text='市場へジャンプ',
        command=lambda: jumpToSijo(txt))
    button1.place(x=10,y=90)
    
    
    gSijoTabSijoNameLabel = tkinter.Label(gSijoTab1, text="市場名:")
    gSijoTabSijoNameLabel.place(x=10, y=120)
    
    #ListBox
    gSijoTabSelectBox = Listbox(gSijoTab1, height=10)
    gSijoTabSelectBox.place(x=10, y=150)
    gSijoTabSelectBox.bind('<<ListboxSelect>>',SijoTabSelectBoxselected);
    
    img = Image.open("test1.png");
    img = img.resize((100, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img)
    gSijoTabShohinLabel = tkinter.Label(gSijoTab1, image=img2)
    gSijoTabShohinLabel.image = img2
    gSijoTabShohinLabel.place(x=150, y=150)
    
    
    gSijoTabSuishoHeightLabel = tkinter.Label(gSijoTab1, text="推奨高さ:")
    gSijoTabSuishoHeightLabel.place(x=150, y=260)
    
    gSijoTabSuishoWidthLabel = tkinter.Label(gSijoTab1, text="推奨幅:")
    gSijoTabSuishoWidthLabel.place(x=150, y=290)
    
    gSijoTabPriceLabel = tkinter.Label(gSijoTab1, text="購入に必要なポイント:")
    gSijoTabPriceLabel.place(x=150, y=320)
    
    return 0
    
def jumpToSijo(textBox1):
    global gSijoTab1
    global gTaskListTab
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
    global gSijoTab1
    global gTaskListTab
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
    global gSijoTab1
    global gTaskListTab
    global gTab3
    global gCurrentMarketURL
    global gCurrentMarketName
    global gMarketShohinList
    global gSijoTabSelectBox
    
    gSijoTabSelectBox.delete(0, tkinter.END);
    
    for s1 in gMarketShohinList:
        gSijoTabSelectBox.insert(tkinter.END, s1[1])
        
    return
        
def gTaskListTab_main():
    global gTaskListTab
    global gTaskListTabTree
    global gTaskAddCountButtons
    global gTaskDelButtons
    
    #文字を表示する
    param_name = tkinter.Label(gTaskListTab, text="タスク一覧")
    param_name.place(x=10, y=30)
    
    gTaskListTabTree = ttk.Treeview(gTaskListTab);

    gTaskListTabTree["columns"] = (1, 2, 3, 4, 5, 6)
    gTaskListTabTree["show"] = "headings"

    gTaskListTabTree.column(1,width=150)
    gTaskListTabTree.column(2,width=90)
    gTaskListTabTree.column(3,width=90)
    gTaskListTabTree.column(4,width=70)
    gTaskListTabTree.column(5,width=90)
    gTaskListTabTree.column(6,width=150)
    
    gTaskListTabTree.heading(1,text="タイトル")
    gTaskListTabTree.heading(2,text="難易度")
    gTaskListTabTree.heading(3,text="達成回数")
    gTaskListTabTree.heading(4,text="+")
    gTaskListTabTree.heading(5,text="リセット間隔")
    gTaskListTabTree.heading(6,text="タスク操作")
    
    gTaskListTabTree.place(x=10, y=60)
    
    path1 = os.getcwd()
    loadTaskData(path1);
    DisplayTaskListTab();
    
    return 0

def loadTaskData(URL):
    global gTaskList
    
    path1 = URL + '\prop\TaskData.txt'
    
    try:
        f = open(path1, encoding='UTF-8')
    except OSError as e:
        messagebox.showinfo('エラー','タスクデータがありません')
        return
    else:
        gTaskDataURL = path1;
        lines = f.readlines()
        
        gTaskList = [];
        for line in lines:
            line = line.rstrip('\n')
            vars = line.split(',');
            #タイトル,難易度,達成回数,リセット日時,リセット間隔(D,W,M,Y)
            gTaskList.append(vars) 
        
        f.close()
        
    return

def DisplayTaskListTab():
    global gTaskListTab
    global gTaskListTabTree
    global gTaskList
    global gTaskAddCountButtons
    global gTaskDelButtons
    
    for i in gTaskListTabTree.get_children():
        gTaskListTabTree.delete(i)
    
    for b1 in gTaskAddCountButtons:
        b1.place_forget()
    
    for b2 in gTaskDelButtons:
        b2.place_forget()
        
    style = ttk.Style(gTaskListTab)
    style.configure("Treeview", rowheight=30)
    
    lineIdx=0
    for t1 in gTaskList:

        nanido = int(t1[1])
        if nanido == 1:
           nanidoStr = '小'
        elif nanido == 2:
           nanidoStr = '中'
        elif nanido == 3:
           nanidoStr = '大'
        else:
           nanidoStr = '特大'
           
        gTaskListTabTree.insert("","end",values=(t1[0],nanidoStr,"", t1[2], t1[4], ""))    
            # ボタン
        button1 = ttk.Button(
            gTaskListTab,
            text='達成',
            command=addTaskCountCallBack(t1[0]))
        button1.place(x=250,y=90+30*lineIdx)
        gTaskAddCountButtons.append(button1)
        
        button2 = ttk.Button(
            gTaskListTab,
            text='このタスクを削除',
            command=deleteTaskCallBack(t1[0]))
        button2.place(x=550,y=90+30*lineIdx)
        gTaskDelButtons.append(button2)
        
        lineIdx = lineIdx + 1
        
    return

def addTaskCountCallBack(title):        
    
    def addTaskCount():
        global gTaskList
    
        for t1 in gTaskList:
            if title == t1[0]:
                t1[2] = int(t1[2]) + 1
        
        DisplayTaskListTab()
        
    return addTaskCount
    
def deleteTaskCallBack(title):
    
    def deleteTask():
        global gTaskList
            
        result=[]
        for t1 in gTaskList:
            if title != t1[0]:
                result.append(t1) 
        
        
        print("aaa");
        gTaskList = result
        DisplayTaskListTab()
        
    return deleteTask
     
def gAddTaskTab_main():
    global gAddTaskTab
    global gNanidoRadioValue
    global gRisetSpanRadioValue
    global gAddTaskTabTitleEntry
    
    #文字を表示する。
    param_name = tkinter.Label(gAddTaskTab, text="タスク追加")
    param_name.place(x=10, y=30)
    
    
    titleLabel = tkinter.Label(gAddTaskTab, text="タスク名:")
    titleLabel.place(x=10, y=60)
    
    
    gAddTaskTabTitleEntry = tkinter.Entry(gAddTaskTab, width=50)
    gAddTaskTabTitleEntry.place(x=80, y=60)
    
    nanidoLabel = tkinter.Label(gAddTaskTab, text="難易度")
    nanidoLabel.place(x=10, y=90)
    
    gNanidoRadioValue = tkinter.IntVar(master=gAddTaskTab, value=1)
    rdioSyo = tkinter.Radiobutton(gAddTaskTab, variable = gNanidoRadioValue, text="小", value=1)
    rdioTyu = tkinter.Radiobutton(gAddTaskTab, variable = gNanidoRadioValue, text="中", value=2)
    rdioDai = tkinter.Radiobutton(gAddTaskTab, variable = gNanidoRadioValue, text="大", value=3)
    rdioTokuDai = tkinter.Radiobutton(gAddTaskTab, variable = gNanidoRadioValue, text="特大", value=4)
    
    rdioSyo.place(x=10, y=120)
    rdioTyu.place(x=10, y=150)
    rdioDai.place(x=10, y=180)
    rdioTokuDai.place(x=10,y=210)
    
    risetSpanLabel = tkinter.Label(gAddTaskTab, text="リセット間隔")
    risetSpanLabel.place(x=10, y=240)
    
    gRisetSpanRadioValue = tkinter.StringVar(master=gAddTaskTab, value="D")
    rdioD = tkinter.Radiobutton(gAddTaskTab, variable = gRisetSpanRadioValue, text="毎日", value="D")
    rdioW = tkinter.Radiobutton(gAddTaskTab, variable = gRisetSpanRadioValue, text="毎週", value="W")
    rdioM = tkinter.Radiobutton(gAddTaskTab, variable = gRisetSpanRadioValue, text="毎月", value="M")
    rdioY = tkinter.Radiobutton(gAddTaskTab, variable = gRisetSpanRadioValue, text="毎年", value="Y")
    
    rdioD.place(x=10, y=270)
    rdioW.place(x=10, y=300)
    rdioM.place(x=10, y=330)
    rdioY.place(x=10,y=360)
        
    button1 = ttk.Button(
        gAddTaskTab,
        text='タスクを登録',
        command=registTaskCallBack())
    button1.place(x=10,y=390)
    
    return 0

def registTaskCallBack():        
    
    def registTask():
        global gNanidoRadioValue
        global gRisetSpanRadioValue
        global gAddTaskTabTitleEntry
        global gTaskList
        
        taskTitle = gAddTaskTabTitleEntry.get()
        nanidoVal= gNanidoRadioValue.get()
        risetSpanVal = gRisetSpanRadioValue.get()
        
        
        currentTimeStr = datetime.date.today().strftime('%Y%m%d')
        
        task1 = [taskTitle, nanidoVal, 0, currentTimeStr, risetSpanVal]
        print(task1)
        gTaskList.append(task1)
        
        saveTaskList()
        
    return registTask

def saveTaskList():
    try:
        URL = os.getcwd()
        path1 = URL + "\\prop\\TaskData.txt"
        f = open(path1, encoding='UTF-8', mode='w')
    except OSError as e:
        messagebox.showinfo('エラー','ファイルのオープンに失敗しました')
        return
    else:
        for t1 in gTaskList:
            f.write(','.join(map(str,t1)))
            f.write('\n')
        
        f.close()
        DisplayTaskListTab()

    return
    
def gAddFanitureTab_main():
    global gAddFanitureTab
    global gRoomImg
    global gAddFanitureTabPosXEntry
    global gAddFanitureTabPosYEntry
    global gAddFanitureTabSizeXEntry
    global gAddFanitureTabSizeYEntry
    
    
    #文字を表示する。
    param_name = tkinter.Label(gAddFanitureTab, text="家具配置")
    param_name.place(x=10, y=30)
    
    posLabel = tkinter.Label(gAddFanitureTab, text="配置位置")
    posLabel.place(x=10, y=60)
    
    posLabel2 = tkinter.Label(gAddFanitureTab, text="x位置:")
    posLabel2.place(x=10, y=90)
    gAddFanitureTabPosXEntry = tkinter.Entry(gAddFanitureTab, width=4)
    gAddFanitureTabPosXEntry.place(x=60, y=90)
    gAddFanitureTabPosXEntry.insert(0, "0")
    
    posLabel3 = tkinter.Label(gAddFanitureTab, text="y位置:")
    posLabel3.place(x=10, y=120)
    gAddFanitureTabPosYEntry = tkinter.Entry(gAddFanitureTab, width=4)
    gAddFanitureTabPosYEntry.place(x=60, y=120)
    gAddFanitureTabPosYEntry.insert(0, "0")
        
    sizeLabel = tkinter.Label(gAddFanitureTab, text="大きさ")
    sizeLabel.place(x=10, y=150)
    
    sizeLabel2 = tkinter.Label(gAddFanitureTab, text="高さ:")
    sizeLabel2.place(x=10, y=180)
    gAddFanitureTabSizeXEntry = tkinter.Entry(gAddFanitureTab, width=4)
    gAddFanitureTabSizeXEntry.place(x=60, y=180)
    gAddFanitureTabSizeXEntry.insert(0, "0")
        
    sizeLabel3 = tkinter.Label(gAddFanitureTab, text="幅:")
    sizeLabel3.place(x=10, y=210)
    gAddFanitureTabSizeYEntry = tkinter.Entry(gAddFanitureTab, width=4)
    gAddFanitureTabSizeYEntry.place(x=60, y=210)
    gAddFanitureTabSizeYEntry.insert(0, "0")
        
    DisplayRoom(300,300)
    
    button1 = ttk.Button(
        gAddFanitureTab,
        text='プレビュー',
        command=DisplayPreViewCallBack())
    button1.place(x=10,y=240)

def getFaniturePosAndSizeEntryVals():
    global gFnPosX
    global gFnPosY
    global gFnSizeX
    global gFnSizeY
    global gAddFanitureTab
    global gRoomImg
    global gAddFanitureTabPosXEntry
    global gAddFanitureTabPosYEntry
    global gAddFanitureTabSizeXEntry
    global gAddFanitureTabSizeYEntry
        
    gFnPosX = 0
    gFnPosY = 0
    gFnSizeX = 0
    gFnSizeY = 0
    
    NStr1 = gAddFanitureTabPosXEntry.get()
    if not NStr1.isdecimal():
        return
    else :
        Num = int(NStr1)
        if Num < 0:
            return
        else:
            gFnPosX = Num
            
    NStr2 = gAddFanitureTabPosYEntry.get()
    if not NStr2.isdecimal():
        return
    else :
        Num = int(NStr2)
        if Num < 0:
            return
        else:
            gFnPosY = Num
            
    NStr3 = gAddFanitureTabSizeXEntry.get()
    if not NStr3.isdecimal():
        return
    else :
        Num = int(NStr3)
        if Num <= 0:
            return
        else:
            gFnSizeY = Num
            
    NStr4 = gAddFanitureTabSizeYEntry.get()
    if not NStr4.isdecimal():
        return
    else :
        Num = int(NStr4)
        if Num <= 0:
            return
        else:
            gFnSizeX = Num
        
    return

def setFanitureCallBack():        
    
    def setFaniture():
        global gAddFanitureTab
        global gRoomImg
        global gAddFanitureTabPosXEntry
        global gAddFanitureTabPosYEntry
        global gAddFanitureTabSizeXEntry
        global gAddFanitureTabSizeYEntry
        
        NStr1 = gAddFanitureTabPosXEntry.get()
        if not NStr1.isdecimal():
            return
        else :
            Num = int(NStr1)
            if Num < 0:
                return
            else:
                PosX = Num
                
        NStr2 = gAddFanitureTabPosYEntry.get()
        if not NStr2.isdecimal():
            return
        else :
            Num = int(NStr2)
            if Num < 0:
                return
            else:
                PosY = Num
                
        NStr3 = gAddFanitureTabSizeXEntry.get()
        if not NStr3.isdecimal():
            return
        else :
            Num = int(NStr3)
            if Num <= 0:
                return
            else:
                SizeY = Num
                
        NStr4 = gAddFanitureTabSizeYEntry.get()
        if not NStr4.isdecimal():
            return
        else :
            Num = int(NStr4)
            if Num <= 0:
                return
            else:
                SizeX = Num

        test1 = cv2.imread("test1.png")
        out1 = AddImage(gRoomImg, test1, PosX, PosY, SizeY, SizeX)
        cv2.imshow("room",out1)
        
        return 1

        
    return setFaniture


def isInRect(x, y, sx, sy, width, height):

    if x<sx:
        return False
    elif x>(sx+width-1):
        return False
        
    if y < sy:
        return False
    elif y >(sy+height-1):
        return False
        
    return True

def AddImage(img1, img2, sx, sy, size_y, size_x):

    if size_y <= 0:
        return img1
    elif size_x <= 0:
        return img1
    
    im1w, im1h, im1c = img1.shape;
    
    img3 = cv2.resize(img2, (size_x, size_y) )
    
    out_img = cv2.imread("blank.png")
    out_img = cv2.resize(out_img,(im1w, im1h))

    width, height, channel = out_img.shape;
    for y in range(height):
        for x in range(width):
            out_img[y, x] = img1[y, x]
            if isInRect(x, y, sx, sy, size_x, size_y) == True:
                pixelValue = img3[y-sy, x-sx]
                if (pixelValue[0] != 255 
                    or pixelValue[1] != 255
                    or pixelValue[2] != 255):
                    out_img[y, x] = pixelValue
                
    return out_img
    
def MixImage(imgURL1, imgURL2):
    img1 = cv2.imread(imgURL1)
    img2 = cv2.imread(imgURL2)
    
    out_img = cv2.imread("blank.png")
    
    width, height, channel = out_img.shape;
    
    for y in range(height):
        for x in range(width):
            pixelValue1 = img1[y, x]
            pixelValue2 = img2[y, x]
            
            if (pixelValue1[0] != 255 
                or pixelValue1[1] != 255
                or pixelValue1[2] != 255):
                out_img[y, x, 0] = pixelValue1[0];
                out_img[y, x, 1] = pixelValue1[1];
                out_img[y, x, 2] = pixelValue1[2];
                
            if (pixelValue2[0] != 255 
                or pixelValue2[1] != 255
                or pixelValue2[2] != 255):
                out_img[y, x, 0] = pixelValue2[0];
                out_img[y, x, 1] = pixelValue2[1];
                out_img[y, x, 2] = pixelValue2[2];
                
    return out_img

def DisplayPreViewCallBack():

    def DisplayPreView():
        global gFnPosX
        global gFnPosY
        global gFnSizeX
        global gFnSizeY
        
        preViewImg = gCurrentRoomImg.copy()
        getFaniturePosAndSizeEntryVals()
        
        fn2Img = cv2.imread("test1.png")
        preViewImg = AddImage(preViewImg, fn2Img, gFnPosX, gFnPosY, gFnSizeX, gFnSizeY)
        cv2.imshow("RoomPreview", preViewImg)
    
    return DisplayPreView
    
def DisplayRoom(roomWidth, roomHeight):
    global gMyFaniture
    global gCurrentRoomImg
    
    roomImg = cv2.imread("blank.png")    
    roomImg = cv2.resize(roomImg, (roomWidth, roomHeight) )
    
    LoadFaniture()

    for fn in gMyFaniture:
        fnURL = getFanitureImgURL(fn[0], fn[1])
        fnImg = cv2.imread(fnURL)
        roomImg = AddImage(roomImg, fnImg, fn[2], fn[3], fn[5], fn[6])
    
    gCurrentRoomImg = roomImg

    cv2.imshow("room", roomImg)
    return
    
def getFanitureImgURL(sijoURL, fnId):
    path1 = sijoURL + '\MarketInfo.txt'
    
    path2 = ""
    try:
        f = open(path1, encoding='UTF-8')
    except OSError as e:
        return
    else:
        lines = f.readlines()
        #最初の一行目読み飛ばし
        lines.pop(0);
        
        
        gMarketShohinList = [];
        for line in lines:
            line = line.rstrip('\n')
            vars = line.split(',');
            id = int(vars[0])
            if id == fnId:
                path2 = sijoURL + "\\" + vars[2]
                break
        
        f.close()
        
    return path2
    
def LoadFaniture():
    global gMyFaniture
    
    URL = os.getcwd()
    path1 = URL + '\prop\MyRoomFaniture.txt'
    
    try:
        f = open(path1, encoding='UTF-8')
    except OSError as e:
        messagebox.showinfo('エラー','部屋の家具データがありません')
        return
    else:
        lines = f.readlines()
        
        gMyFaniture = [];
        for line in lines:
            line = line.rstrip('\n')
            vars = line.split(',');
            #市場URL,商品ID,x位置,y位置,z位置,高さ,幅
            gMyFaniture.append(vars) 
        
        f.close()
        
        for fn1 in gMyFaniture:
            v1 = int(fn1[1])
            v2 = int(fn1[2])
            v3 = int(fn1[3])
            v4 = int(fn1[4])
            v5 = int(fn1[5])
            v6 = int(fn1[6])
            fn1[1] = v1
            fn1[2] = v2
            fn1[3] = v3
            fn1[4] = v4
            fn1[5] = v5
            fn1[6] = v6
        
        gMyFaniture = sorted(gMyFaniture, reverse=False, key=lambda x:x[4])
        
        
    return
    
if __name__ == "__main__":
    main()
    
    

