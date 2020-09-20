
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import  Image, ImageTk

import tkinter
import numpy
import cv2
import os
import datetime

gRoomWidth = 300
gRoomHeight = 300
gAvatourBlankType=1
gAvatourVisibleFlg=True
gAvatourWidth=100
gAvatourHeight=150
gAvatourPosX = 0
gAvatourPosY = 0
gAvatourPosZ = 0


gCurrentToDoTaskPoint = 100
gCurrentToDoTaskPointStrLabel=''
gGetTaskPointVols=[10,20,30,40]

#タブリスト
gSijoTab1 = ''
gTaskListTab = ''
gAddTaskTab = ''
gAddFanitureTab = ''
gAvatourItemShopTab = ''
gAddAvatourItemTab = ''
gDeleteFanitureTab = ''
gDeleteAvatourItemTab = ''
gShowCurrentToDoTaskPointTab = ''
gAvatourConfigurationTab = ''


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
#タイトル,難易度,達成回数,リセット日時,リセット間隔(D,W,M,Y)
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
gAddFanitureTabPosZEntry=''
gAddFanitureTabSizeXEntry=''
gAddFanitureTabSizeYEntry=''


#市場URL,商品ID,x位置,y位置,z位置,高さ,幅
gMyFaniture=[];
gMyAddFaniturePrev=[];
gMyDelFaniturePrev=[];
gCurrentRoomImg=''
gCurrentPreviewRoomImg=''
gPointLabelOnAddFanitureTab=''
gFnPosX = ''
gFnPosY = ''
gFnPosZ = ''
gFnSizeX = ''
gFnSizeY = ''


#市場URL,商品ID,名前
gMyHavingFaniture=[]
gSearchedHavingFaniture=[]
gHavingFanitureListBox=''
gAddFanitureTabFnImgLabel=''

gCurrentAvatourItemShopURL=''
gCurrentAvatourItemShopName=''
gAvatourItemShopNameLabel=''
gAvatourItemListOnAvatourItemShopTab=[]
gAvatourItemListBoxOnAvatourItemShopTab=''
gAvatourItemSuishoWidthLabel=''
gAvatourItemSuishoHeightLabel=''
gAvatourItemPriceLabel=''
gAvatourItemShopTabShohinLabel=''

gAvatourImg=''
gCurrentAvatourImg=''
gCurrentPreviewAvatourImg=''
gAddAvatourItemTabPosXEntry=''
gAddAvatourItemTabPosYEntry=''
gAddAvatourItemTabPosZEntry=''
gAddAvatourItemTabSizeXEntry=''
gAddAvatourItemTabSizeYEntry=''
gHavingAvatourItemListBox=''
#アバターショップURL,アイテムID,名前
gMyHavingAvatourItem=[]
#市場URL,アバターアイテムID,x位置,y位置,z位置,高さ,幅
gMyAvatourItem=[]
gMyAvatourPrev=[]
gAddAvatorItemTabItmImgLabel=''
gPointLabelOnAddAvatourItemTab=''


gAvatourItmPosX=''
gAvatourItmPosY=''
gAvatourItmPosZ=''
gAvatourItmSizeX=''
gAvatourItmSizeY=''

gFanitureDelButtons=[]
gFanitureDelPrevButtons=[]
gDeleteFanitureTabTree=''

gAvatourItemDelButtons=[]
gAvatourItemDelPrevButtons=[]
gDeleteAvatourItemTabTree=''

gVisibleFlgRadioValue=True
gAvatourBlankTypeRadioValue=1
gAvatourConfigurationTabPosXEntry=''
gAvatourConfigurationTabPosYEntry=''
gAvatourConfigurationTabPosZEntry=''
gAvatourConfigurationTabSizeXEntry=''
gAvatourConfigurationTabSizeYEntry=''

def calcFanitureSetPoint(height, width):
    print("height:"+str(height))
    print("width:"+str(width))
    return int(int(30) + (height * width) * 0.001)
    
    
def setNeetPtToSetFanitureCallBack():
    
    def setNeetPtToSetFaniture():
        global gPointLabelOnAddFanitureTab
        global gFnSizeX
        global gFnSizeY
        if not getFaniturePosAndSizeEntryVals():
            return
            
        NeedPt = calcFanitureSetPoint(gFnSizeY, gFnSizeX)
        str1 = "設置に必要なポイント:"+ str(NeedPt)
        gPointLabelOnAddFanitureTab.configure(text=str1)

        return
    
    return setNeetPtToSetFaniture

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
    global gToDoTaskPoint
   
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
    gSijoTabShohinLabel.place(x=200, y=150)
    
    
    im2 = cv2.imread(imgURL)
    sh, sw, c = im2.shape;
    
    str1 = "推奨高さ:"+ str(sh);
    gSijoTabSuishoHeightLabel.configure(text=str1);
    
    str1 = "推奨幅:"+ str(sw);
    gSijoTabSuishoWidthLabel.configure(text=str1);
    
    str1 = "購入に必要なポイント:" + str(gMarketShohinList[crSelectIdx][3])
    gSijoTabPriceLabel.configure(text=str1);
    
def main():
    global gSijoTab1
    global gTaskListTab
    global gAddTaskTab
    global gAddFanitureTab
    global gAvatourItemShopTab
    global gAddAvatourItemTab
    global gDeleteFanitureTab
    global gDeleteAvatourItemTab
    global gShowCurrentToDoTaskPointTab
    global gAvatourConfigurationTab
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
    gAvatourItemShopTab = tkinter.Frame(nb)
    gAddAvatourItemTab = tkinter.Frame(nb)
    gDeleteFanitureTab = tkinter.Frame(nb)
    gDeleteAvatourItemTab = tkinter.Frame(nb)
    gShowCurrentToDoTaskPointTab = tkinter.Frame(nb)
    gAvatourConfigurationTab = tkinter.Frame(nb)
    

    nb.add(gTaskListTab, text="タスク一覧", padding=5)
    nb.add(gAddTaskTab, text="タスク追加", padding=5)
    nb.add(gSijoTab1, text="市場", padding=5)
    nb.add(gAddFanitureTab, text="家具配置", padding=5)
    nb.add(gDeleteFanitureTab, text="家具削除", padding=5)
    nb.add(gAvatourItemShopTab, text="アバターアイテムショップ", padding=5)
    nb.add(gAddAvatourItemTab, text="アバターアイテム追加", padding=5)
    nb.add(gDeleteAvatourItemTab, text="アバターアイテム削除", padding=5)
    nb.add(gAvatourConfigurationTab, text="アバター表示設定", padding=5)
    nb.add(gShowCurrentToDoTaskPointTab, text="現在の保有ポイント", padding=5)
    
    #メインフレームでのnotebook配置を決定する。
    nb.pack(expand=1, fill="both")
 
    #各タブの内容を記載する。
    sijoTab_main()
    gTaskListTab_main()
    gAddTaskTab_main()
    gAddFanitureTab_main()
    gAvatourItemShopTab_main()
    gAddAvatourItemTab_main()
    gDeleteFanitureTab_main()
    gDeleteAvatourItemTab_main()
    gShowCurrentToDoTaskPointTab_main()
    gAvatourConfigurationTab_main()
 
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
    
    # Scrollbar
    scrollbar = ttk.Scrollbar(
        gSijoTab1,
        orient=VERTICAL,
        command=gSijoTabSelectBox.yview)
    gSijoTabSelectBox['yscrollcommand'] = scrollbar.set
    scrollbar.place(x=150, y=150, width=30, height=150)
    
    img = Image.open("blank.png");
    img = img.resize((100, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img)
    gSijoTabShohinLabel = tkinter.Label(gSijoTab1, image=img2)
    gSijoTabShohinLabel.image = img2
    gSijoTabShohinLabel.place(x=200, y=150)
    
    
    gSijoTabSuishoHeightLabel = tkinter.Label(gSijoTab1, text="推奨高さ:")
    gSijoTabSuishoHeightLabel.place(x=200, y=260)
    
    gSijoTabSuishoWidthLabel = tkinter.Label(gSijoTab1, text="推奨幅:")
    gSijoTabSuishoWidthLabel.place(x=200, y=290)
    
    gSijoTabPriceLabel = tkinter.Label(gSijoTab1, text="購入に必要なポイント:")
    gSijoTabPriceLabel.place(x=200, y=320)
    
    button2 = ttk.Button(
        gSijoTab1,
        text='購入',
        command=parchaseFanitureCallBack())
    button2.place(x=200,y=350)

    return 0
    
def addHavingFaniture(sijoURL, fnId):
    global gMyHavingFaniture
    
    jufukuFlg = False
    for hfn1 in gMyHavingFaniture:
        if sijoURL == hfn1[0] and fnId == hfn1[1]:
            messagebox.showinfo('メッセージ','既に購入済みの家具です')
            return False
    
    if jufukuFlg == False:
        name1 = getFanitureName(sijoURL, fnId)
        vars = [sijoURL, fnId, name1]
        gMyHavingFaniture.append(vars)

    return True
    
def parchaseFanitureCallBack():

    def parchaseFaniture():
        global gSijoTabSelectBox
        global gCurrentToDoTaskPoint
        global gMarketShohinList
        global gCurrentMarketURL
        
        if not gSijoTabSelectBox.curselection():
            return 
        crSelectIdx = gSijoTabSelectBox.curselection()[0];

        price = int(gMarketShohinList[crSelectIdx][3])
        if price > gCurrentToDoTaskPoint:
            messagebox.showinfo('メッセージ','購入に必要なポイントが足りません')
            return
        
        ret = addHavingFaniture(gCurrentMarketURL, gMarketShohinList[crSelectIdx][0])
        
        if ret == True:
            str2 = "商品:"
            str2 += gMarketShohinList[crSelectIdx][1]
            str2 += "を購入しました"
            messagebox.showinfo('メッセージ',str2)
            gCurrentToDoTaskPoint = gCurrentToDoTaskPoint - price

        DisplayCuttentToDoTaskPointTab()
        DisplayAddFanitureTab()
        
        saveHavingFanitureList()
        
        return
        
    return parchaseFaniture
    
def saveHavingFanitureList():
    global gMyHavingFaniture
    
    try:
        URL = os.getcwd()
        path1 = URL + "\\prop\MyHavingFaniture.txt"
        f = open(path1, encoding='UTF-8', mode='w')
    except OSError as e:
        messagebox.showinfo('エラー','ファイルのオープンに失敗しました')
        return
    else:
        #持っている家具一覧ファイルには（市場URL, 商品ID)のみ書き出し
        for t1 in gMyHavingFaniture:
            var1 = [t1[0], t1[1]]
            f.write(','.join(map(str,var1)))
            f.write('\n')
        
        f.close()

    return
    
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
            vars[0] = int(vars[0])
            vars[3] = int(vars[3])
            
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
        global gCurrentToDoTaskPoint
        global gGetTaskPointVols
        
        for t1 in gTaskList:
            if title == t1[0]:
                t1[2] = int(t1[2]) + 1
                gCurrentToDoTaskPoint = gCurrentToDoTaskPoint + gGetTaskPointVols[(int(t1[1])-1)]
        
        DisplayTaskListTab()
        DisplayCuttentToDoTaskPointTab()
        
    return addTaskCount
    
def deleteTaskCallBack(title):
    
    def deleteTask():
        global gTaskList
            
        result=[]
        for t1 in gTaskList:
            if title != t1[0]:
                result.append(t1) 
        
        
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
        gTaskList.append(task1)
        
        saveTaskList()
        
        DisplayTaskListTab()
        
    return registTask

def saveTaskList():
    try:
        URL = os.getcwd()
        path1 = URL + "\\prop\TaskData.txt"
        f = open(path1, encoding='UTF-8', mode='w')
    except OSError as e:
        messagebox.showinfo('エラー','ファイルのオープンに失敗しました')
        return
    else:
        for t1 in gTaskList:
            f.write(','.join(map(str,t1)))
            f.write('\n')
        
        f.close()

    return
def gHavingFanitureListBoxSelected(event):
    global gAddFanitureTab
    global gHavingFanitureListBox
    global gMyHavingFaniture
    global gAddFanitureTabFnImgLabel
    
    if not gHavingFanitureListBox.curselection():
        return 
    crSelectIdx = gHavingFanitureListBox.curselection()[0];

    imgURL = getFanitureImgURL(gMyHavingFaniture[crSelectIdx][0],gMyHavingFaniture[crSelectIdx][1])
    img = Image.open(imgURL);
    img = img.resize((100, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img)
    gAddFanitureTabFnImgLabel.configure(image=img2)
    gAddFanitureTabFnImgLabel.image = img2
    gAddFanitureTabFnImgLabel.place(x=300, y=50)
    
    
    im2 = cv2.imread(imgURL)
    sh, sw, c = im2.shape;


    return 0
    
def gAddFanitureTab_main():
    global gAddFanitureTab
    global gRoomImg
    global gAddFanitureTabPosXEntry
    global gAddFanitureTabPosYEntry
    global gAddFanitureTabPosZEntry
    global gAddFanitureTabSizeXEntry
    global gAddFanitureTabSizeYEntry
    global gHavingFanitureListBox
    global gMyHavingFaniture
    global gAddFanitureTabFnImgLabel
    global gPointLabelOnAddFanitureTab
    
    
    #文字を表示する。
    param_name = tkinter.Label(gAddFanitureTab, text="家具配置")
    param_name.place(x=10, y=30)

    #ListBox
    gHavingFanitureListBox = Listbox(gAddFanitureTab, height=10)
    gHavingFanitureListBox.place(x=10, y=60)
    gHavingFanitureListBox.bind('<<ListboxSelect>>',gHavingFanitureListBoxSelected);
    
    LoadHavingFaniture()
    
    gHavingFanitureListBox.delete(0, tkinter.END);
    for hFn in gMyHavingFaniture:
        gHavingFanitureListBox.insert(tkinter.END, hFn[2])
        
    
    # Scrollbar
    scrollbar = ttk.Scrollbar(
        gAddFanitureTab,
        orient=VERTICAL,
        command=gHavingFanitureListBox.yview)
    gHavingFanitureListBox['yscrollcommand'] = scrollbar.set
    scrollbar.place(x=150, y=60, width=30, height=150)
    
    posLabel = tkinter.Label(gAddFanitureTab, text="配置位置")
    posLabel.place(x=200, y=60)
    
    posLabel2 = tkinter.Label(gAddFanitureTab, text="x位置:")
    posLabel2.place(x=200, y=90)
    gAddFanitureTabPosXEntry = tkinter.Entry(gAddFanitureTab, width=4)
    gAddFanitureTabPosXEntry.place(x=240, y=90)
    gAddFanitureTabPosXEntry.insert(0, "0")
    
    posLabel3 = tkinter.Label(gAddFanitureTab, text="y位置:")
    posLabel3.place(x=200, y=120)
    gAddFanitureTabPosYEntry = tkinter.Entry(gAddFanitureTab, width=4)
    gAddFanitureTabPosYEntry.place(x=240, y=120)
    gAddFanitureTabPosYEntry.insert(0, "0")
    

    posLabel4 = tkinter.Label(gAddFanitureTab, text="z位置:")
    posLabel4.place(x=200, y=150)
    gAddFanitureTabPosZEntry = tkinter.Entry(gAddFanitureTab, width=4)
    gAddFanitureTabPosZEntry.place(x=240, y=150)
    gAddFanitureTabPosZEntry.insert(0, "0")
        
    sizeLabel = tkinter.Label(gAddFanitureTab, text="大きさ")
    sizeLabel.place(x=200, y=180)
    
    sizeLabel2 = tkinter.Label(gAddFanitureTab, text="高さ:")
    sizeLabel2.place(x=200, y=210)
    gAddFanitureTabSizeYEntry = tkinter.Entry(gAddFanitureTab, width=4)
    gAddFanitureTabSizeYEntry.place(x=240, y=210)
    gAddFanitureTabSizeYEntry.insert(0, "0")
        
    sizeLabel3 = tkinter.Label(gAddFanitureTab, text="幅:")
    sizeLabel3.place(x=200, y=240)
    gAddFanitureTabSizeXEntry = tkinter.Entry(gAddFanitureTab, width=4)
    gAddFanitureTabSizeXEntry.place(x=240, y=240)
    gAddFanitureTabSizeXEntry.insert(0, "0")
    
    img = Image.open("blank.png");
    img = img.resize((100, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img)
    gAddFanitureTabFnImgLabel = tkinter.Label(gAddFanitureTab, image=img2)
    gAddFanitureTabFnImgLabel.image = img2
    gAddFanitureTabFnImgLabel.place(x=300, y=50)
    
    gPointLabelOnAddFanitureTab = tkinter.Label(gAddFanitureTab, text="設置に必要なポイント:")
    gPointLabelOnAddFanitureTab.place(x=200, y=270)
    
    DisplayRoom()
    
    button1 = ttk.Button(
        gAddFanitureTab,
        text='配置プレビュー',
        command=DisplayPreViewCallBack())
    button1.place(x=10,y=240)
    
    button2 = ttk.Button(
        gAddFanitureTab,
        text='設置に必要なポイント計算',
        command=setNeetPtToSetFanitureCallBack())
    button2.place(x=10,y=270)
    
    button3 = ttk.Button(
        gAddFanitureTab,
        text='配置',
        command=fixFanitureCallBack())
    button3.place(x=10,y=300)


  
def fixFanitureCallBack():

    def fixFaniture():
        global gHavingFanitureListBox
        global gFnPosX
        global gFnPosY
        global gFnPosZ
        global gFnSizeX
        global gFnSizeY
        global gCurrentToDoTaskPoint
        
        if not getFaniturePosAndSizeEntryVals():
            return
            
        
        if not gHavingFanitureListBox.curselection():
            return 
        crSelectIdx = gHavingFanitureListBox.curselection()[0];
        
        needPt = calcFanitureSetPoint(gFnSizeY, gFnSizeX)
        if gCurrentToDoTaskPoint < needPt:
            messagebox.showinfo('メッセージ','配置に必要なポイントが足りません')
            return
        
        addMyFanitureList(gMyHavingFaniture[crSelectIdx][0],gMyHavingFaniture[crSelectIdx][1])
        gCurrentToDoTaskPoint = gCurrentToDoTaskPoint - needPt
        
        saveMyRoomFanitureList()
        
        DisplayCuttentToDoTaskPointTab()
        DisplayRoom()
        
        return

    return fixFaniture

def saveMyRoomFanitureList():
    try:
        URL = os.getcwd()
        path1 = URL + "\\prop\MyRoomFaniture.txt"
        f = open(path1, encoding='UTF-8', mode='w')
    except OSError as e:
        messagebox.showinfo('エラー','ファイルのオープンに失敗しました')
        return
    else:
        for t1 in gMyFaniture:
            f.write(','.join(map(str,t1)))
            f.write('\n')
        
        f.close()

    return

def addMyFanitureList(sijoURL, fnId):
    global gMyFaniture
    global gFnPosX
    global gFnPosY
    global gFnPosZ
    global gFnSizeX
    global gFnSizeY
    
    if not getFaniturePosAndSizeEntryVals():
        return
        
    var1 = [sijoURL, fnId, gFnPosX, gFnPosY, gFnPosZ, gFnSizeY, gFnSizeX]
    gMyFaniture.append(var1)
    
    return

def DisplayAddFanitureTab():
    global gHavingFanitureListBox
    global gMyHavingFaniture
    
    gHavingFanitureListBox.delete(0, tkinter.END);
    
    for fn1 in gMyHavingFaniture:
        gHavingFanitureListBox.insert(tkinter.END, fn1[2])
        
    return

def getFaniturePosAndSizeEntryVals():
    global gFnPosX
    global gFnPosY
    global gFnPosZ
    global gFnSizeX
    global gFnSizeY
    global gAddFanitureTab
    global gRoomImg
    global gAddFanitureTabPosXEntry
    global gAddFanitureTabPosYEntry
    global gAddFanitureTabPosZEntry
    global gAddFanitureTabSizeXEntry
    global gAddFanitureTabSizeYEntry
        
    gFnPosX = 0
    gFnPosY = 0
    gFnPosZ = 0
    gFnSizeX = 0
    gFnSizeY = 0
    
    NStr1 = gAddFanitureTabPosXEntry.get()
    if not NStr1.isdecimal():
        return False
    else :
        Num = int(NStr1)
        if Num < 0:
            return False
        else:
            gFnPosX = Num
            
    NStr2 = gAddFanitureTabPosYEntry.get()
    if not NStr2.isdecimal():
        return False
    else :
        Num = int(NStr2)
        if Num < 0:
            return False
        else:
            gFnPosY = Num
            
    NStr5 = gAddFanitureTabPosZEntry.get()
    if not NStr5.isdecimal():
        return False
    else :
        Num = int(NStr5)
        if Num < 0:
            return False
        else:
            gFnPosZ = Num            
            
    NStr3 = gAddFanitureTabSizeXEntry.get()
    if not NStr3.isdecimal():
        return False
    else :
        Num = int(NStr3)
        if Num <= 0:
            return False
        else:
            gFnSizeX = Num
            
    NStr4 = gAddFanitureTabSizeYEntry.get()
    if not NStr4.isdecimal():
        return False
    else :
        Num = int(NStr4)
        if Num <= 0:
            return False
        else:
            gFnSizeY = Num
        
    return True

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
        cv2.namedWindow("room", cv2.WINDOW_NORMAL)
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
    
    im1h, im1w, im1c = img1.shape;
    
    img3 = cv2.resize(img2, (size_x, size_y) )
    
    out_img = cv2.imread("blank.png")
    out_img = cv2.resize(out_img,(im1w, im1h))

    
    width = im1w
    height = im1h

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
        global gCurrentPreviewRoomImg
        global gRoomWidth
        global gRoomHeight
        global gFnPosX
        global gFnPosY
        global gFnSizeX
        global gFnSizeY
        global gAddFanitureTab
        global gHavingFanitureListBox
        global gMyHavingFaniture
        global gSearchedHavingFaniture
        global gMyFaniture
        global gMyAddFaniturePrev
        global gAvatourVisibleFlg
        global gAvatourWidth
        global gAvatourHeight
        global gAvatourPosX
        global gAvatourPosY
        global gAvatourPosZ
        
        avatourDrawedFlg=False
    
        gSearchedHavingFaniture = gMyHavingFaniture.copy()
        if not gHavingFanitureListBox.curselection():
            return 
        crSelectIdx = gHavingFanitureListBox.curselection()[0];

        if not getFaniturePosAndSizeEntryVals():
            return
        
        avatourImg = MakeAvatourImage()
            
        gMyAddFaniturePrev = gMyFaniture.copy()
        
        val1 = [gSearchedHavingFaniture[crSelectIdx][0], gSearchedHavingFaniture[crSelectIdx][1], gFnPosX, gFnPosY, gFnPosZ,gFnSizeY, gFnSizeX]
        gMyAddFaniturePrev.append(val1)

        gMyAddFaniturePrev = sorted(gMyAddFaniturePrev, reverse=False, key=lambda x:x[4])
        
        roomImg = cv2.imread("blank.png")    
        roomImg = cv2.resize(roomImg, (gRoomWidth, gRoomHeight) )
        
        for fn in gMyAddFaniturePrev:
            fnURL = getFanitureImgURL(fn[0], fn[1])
            fnImg = cv2.imread(fnURL)
            
        #アバターを描画
            if gAvatourVisibleFlg == True and fn[4] >= gAvatourPosZ:
                roomImg = AddImage(roomImg, avatourImg, gAvatourPosX, gAvatourPosY, gAvatourHeight, gAvatourWidth)
                avatourDrawedFlg=True
                
            roomImg = AddImage(roomImg, fnImg, fn[2], fn[3], fn[5], fn[6])
            
            #アバターが画面の一番手前にいるとき
        if avatourDrawedFlg == False:
            roomImg = AddImage(roomImg, avatourImg, gAvatourPosX, gAvatourPosY, gAvatourHeight, gAvatourWidth)
        
        gCurrentPreviewRoomImg = roomImg

        cv2.imshow("previewRoom", roomImg)
        
        return
    
    return DisplayPreView
    
def DisplayRoom():
    global gMyFaniture
    global gCurrentRoomImg
    global gRoomWidth
    global gRoomHeight
    global gAvatourVisibleFlg
    global gAvatourWidth
    global gAvatourHeight
    global gAvatourPosX
    global gAvatourPosY
    global gAvatourPosZ
    
    avatourDrawedFlg=False
    
    avatourImg = MakeAvatourImage()
    
    roomImg = cv2.imread("blank.png")    
    roomImg = cv2.resize(roomImg, (gRoomWidth, gRoomHeight) )
    
    LoadFaniture()

    for fn in gMyFaniture:
        fnURL = getFanitureImgURL(fn[0], fn[1])
        fnImg = cv2.imread(fnURL)
        
        
        #アバターを描画
        if gAvatourVisibleFlg == True and fn[4] >= gAvatourPosZ:
            roomImg = AddImage(roomImg, avatourImg, gAvatourPosX, gAvatourPosY, gAvatourHeight, gAvatourWidth)
            avatourDrawedFlg=True
    
        roomImg = AddImage(roomImg, fnImg, fn[2], fn[3], fn[5], fn[6])
    
    #アバターが画面の一番手前にいるとき
    if avatourDrawedFlg == False:
        roomImg = AddImage(roomImg, avatourImg, gAvatourPosX, gAvatourPosY, gAvatourHeight, gAvatourWidth)
    
    gCurrentRoomImg = roomImg

    cv2.imshow("room", roomImg)
    cv2.moveWindow('room', 100, 200)
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

#現在部屋に置かれている家具のリストをロードする    
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

#現在持っている家具のリストをロードする    
def LoadHavingFaniture():
    global gMyHavingFaniture
    
    URL = os.getcwd()
    path1 = URL + '\prop\MyHavingFaniture.txt'
    
    try:
        f = open(path1, encoding='UTF-8')
    except OSError as e:
        messagebox.showinfo('エラー','持っている家具リストファイルがありません')
        return
    else:
        lines = f.readlines()
        
        gMyHavingFaniture = [];
        for line in lines:
            line = line.rstrip('\n')
            vars = line.split(',');
            #市場URL,商品ID
            gMyHavingFaniture.append(vars) 
        
        f.close()
        
        for fn1 in gMyHavingFaniture:
            v1 = int(fn1[1])
            fn1[1] = v1
            name1 = getFanitureName(fn1[0], fn1[1])
            fn1.append(name1)
        
        #市場URL,商品ID,商品名
        gMyHavingFaniture = sorted(gMyHavingFaniture, reverse=False, key=lambda x:x[2])
        
    return
    
def getFanitureName(sijoURL, fnId):
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
                name = vars[1]
                break
        
        f.close()
        
    return name

def gAvatourItemShopTab_main():
    global gAvatourItemShopTab
    global gCurrentAvatourItemShopURL
    global gCurrentAvatourItemShopName
    global gAvatourItemShopNameLabel
    global gAvatourItemListOnAvatourItemShopTab
    global gAvatourItemListBoxOnAvatourItemShopTab
    global gAvatourItemSuishoWidthLabel
    global gAvatourItemSuishoHeightLabel
    global gAvatourItemPriceLabel
    global gAvatourItemShopTabShohinLabel
    
    #文字を表示する。
    title_name = tkinter.Label(gAvatourItemShopTab, text="アバターアイテムショップ")
    title_name.place(x=10, y=30)
    
    label1 = tkinter.Label(gAvatourItemShopTab, text="アバターアイテムショップURL")
    label1.place(x=10, y=60)
    
    # Text
    txt = Text(gAvatourItemShopTab, height=1, width=30)
    txt.insert(1.0, "")
    txt.place(x=200, y=60)
    
    # ボタン
    button1 = ttk.Button(
        gAvatourItemShopTab,
        text='アバターアイテムショップへジャンプ',
        command=lambda: jumpToAvatourItemShop(txt))
    button1.place(x=10,y=90)
    
    
    gAvatourItemShopNameLabel = tkinter.Label(gAvatourItemShopTab, text="ショップ名:")
    gAvatourItemShopNameLabel.place(x=10, y=120)
    
    #ListBox
    gAvatourItemListBoxOnAvatourItemShopTab = Listbox(gAvatourItemShopTab, height=10)
    gAvatourItemListBoxOnAvatourItemShopTab.place(x=10, y=150)
    gAvatourItemListBoxOnAvatourItemShopTab.bind('<<ListboxSelect>>',gAvatourItemListBoxOnAvatourItemShopTabSelected);
    
    # Scrollbar
    scrollbar = ttk.Scrollbar(
        gAvatourItemShopTab,
        orient=VERTICAL,
        command=gAvatourItemListBoxOnAvatourItemShopTab.yview)
    gAvatourItemListBoxOnAvatourItemShopTab['yscrollcommand'] = scrollbar.set
    scrollbar.place(x=150, y=150, width=30, height=150)
    
    img = Image.open("blank.png");
    img = img.resize((100, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img)
    gAvatourItemShopTabShohinLabel = tkinter.Label(gAvatourItemShopTab, image=img2)
    gAvatourItemShopTabShohinLabel.image = img2
    gAvatourItemShopTabShohinLabel.place(x=200, y=150)
    
    
    gAvatourItemSuishoHeightLabel = tkinter.Label(gAvatourItemShopTab, text="推奨高さ:")
    gAvatourItemSuishoHeightLabel.place(x=200, y=260)
    
    gAvatourItemSuishoWidthLabel = tkinter.Label(gAvatourItemShopTab, text="推奨幅:")
    gAvatourItemSuishoWidthLabel.place(x=200, y=290)
    
    gAvatourItemPriceLabel = tkinter.Label(gAvatourItemShopTab, text="購入に必要なポイント:")
    gAvatourItemPriceLabel.place(x=200, y=320)
    
    button2 = ttk.Button(
        gAvatourItemShopTab,
        text='購入',
        command=parchaseAvatourItemCallBack())
    button2.place(x=200,y=350)
    
    return 0

def addHavingAvatourItem(avatourItemShopURL, itmId):
    global gMyHavingAvatourItem
    
    jufukuFlg = False
    for hfn1 in gMyHavingAvatourItem:
        if avatourItemShopURL == hfn1[0] and itmId == hfn1[1]:
            messagebox.showinfo('メッセージ','既に購入済みのアイテムです')
            return False
    
    if jufukuFlg == False:
        name1 = getAvatourItemName(avatourItemShopURL, itmId)
        vars = [avatourItemShopURL, itmId, name1]
        gMyHavingAvatourItem.append(vars)

    return True
    
def parchaseAvatourItemCallBack():

    def parchaseAvatourItem():
        global gAvatourItemListBoxOnAvatourItemShopTab
        global gCurrentToDoTaskPoint
        global gAvatourItemListOnAvatourItemShopTab
        global gCurrentAvatourItemShopURL
        
        if not gAvatourItemListBoxOnAvatourItemShopTab.curselection():
            return 
        crSelectIdx = gAvatourItemListBoxOnAvatourItemShopTab.curselection()[0];

        price = int(gAvatourItemListOnAvatourItemShopTab[crSelectIdx][3])
        if price > gCurrentToDoTaskPoint:
            messagebox.showinfo('メッセージ','購入に必要なポイントが足りません')
            return
        
        ret = addHavingAvatourItem(gCurrentAvatourItemShopURL, gAvatourItemListOnAvatourItemShopTab[crSelectIdx][0])
        
        if ret == True:
            str2 = "アイテム:"
            str2 += gAvatourItemListOnAvatourItemShopTab[crSelectIdx][1]
            str2 += "を購入しました"
            messagebox.showinfo('メッセージ',str2)
            gCurrentToDoTaskPoint = gCurrentToDoTaskPoint - price

        DisplayCuttentToDoTaskPointTab()
        DisplayAddAvatourItemTab()
        
        saveHavingAvatourItemList()
        
        return
        
    return parchaseAvatourItem

    
def DisplayAddAvatourItemTab():
    global gHavingAvatourItemListBox
    global gMyHavingAvatourItem
    
    gHavingAvatourItemListBox.delete(0, tkinter.END);
    
    for fn1 in gMyHavingAvatourItem:
        gHavingAvatourItemListBox.insert(tkinter.END, fn1[2])
        
    return
    
def saveHavingAvatourItemList():
    global gMyHavingAvatourItem
    
    try:
        URL = os.getcwd()
        path1 = URL + "\\prop\MyHavingAvatourItem.txt"
        f = open(path1, encoding='UTF-8', mode='w')
    except OSError as e:
        messagebox.showinfo('エラー','ファイルのオープンに失敗しました')
        return
    else:
        #持っている家具一覧ファイルには（市場URL, 商品ID)のみ書き出し
        for t1 in gMyHavingAvatourItem:
            var1 = [t1[0], t1[1]]
            f.write(','.join(map(str,var1)))
            f.write('\n')
        
        f.close()

    return
    


def gAvatourItemListBoxOnAvatourItemShopTabSelected(event):
    global gAvatourItemShopTab
    global gCurrentAvatourItemShopURL
    global gCurrentAvatourItemShopName
    global gAvatourItemShopNameLabel
    global gAvatourItemListOnAvatourItemShopTab
    global gAvatourItemListBoxOnAvatourItemShopTab
    global gAvatourItemSuishoWidthLabel
    global gAvatourItemSuishoHeightLabel
    global gAvatourItemPriceLabel
    global gAvatourItemShopTabShohinLabel
   

    if not gAvatourItemListBoxOnAvatourItemShopTab.curselection():
        return 
    crSelectIdx = gAvatourItemListBoxOnAvatourItemShopTab.curselection()[0];


    var1 = gAvatourItemListBoxOnAvatourItemShopTab.get(crSelectIdx)
    imgURL = gCurrentAvatourItemShopURL + '\\' + gAvatourItemListOnAvatourItemShopTab[crSelectIdx][2]
    img = Image.open(imgURL);
    img = img.resize((100, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img)
    gAvatourItemShopTabShohinLabel.configure(image=img2)
    gAvatourItemShopTabShohinLabel.image = img2
    gAvatourItemShopTabShohinLabel.place(x=200, y=150)
    
    
    im2 = cv2.imread(imgURL)
    sh, sw, c = im2.shape;
    
    str1 = "推奨高さ:"+ str(sh);
    gAvatourItemSuishoHeightLabel.configure(text=str1);
    
    str1 = "推奨幅:"+ str(sw);
    gAvatourItemSuishoWidthLabel.configure(text=str1);
    
    str1 = "購入に必要なポイント:" + str(gAvatourItemListOnAvatourItemShopTab[crSelectIdx][3])
    gAvatourItemPriceLabel.configure(text=str1);


def jumpToAvatourItemShop(textBox1):
    result=textBox1.get("1.0", "end")
    result = result.rstrip('\n')
    
    loadAvatourItemShopData(result)
    
    DisplayAvatourItemShopData();

def loadAvatourItemShopData(URL):
    global gAvatourItemShopTab
    global gCurrentAvatourItemShopURL
    global gCurrentAvatourItemShopName
    global gAvatourItemListOnAvatourItemShopTab
    global gAvatourItemListBoxOnAvatourItemShopTab
    global gAvatourItemShopNameLabel

    path1 = URL + '\AvatourItemShopInfo.txt'
    
    try:
        f = open(path1, encoding='UTF-8')
    except OSError as e:
        messagebox.showinfo('エラー','URLが違っています')
        return
    else:
        gCurrentAvatourItemShopURL = URL;
        lines = f.readlines()
        gCurrentAvatourItemShopName=lines[0].split(',')[1];
        lines.pop(0);
        
        str1 = "アバターアイテムショップ名:"+gCurrentAvatourItemShopName;
        gAvatourItemShopNameLabel.configure(text=str1);
        
        gAvatourItemListOnAvatourItemShopTab = [];
        for line in lines:
            line = line.rstrip('\n')
            vars = line.split(',');
            vars[0] = int(vars[0])
            gAvatourItemListOnAvatourItemShopTab.append(vars) 
        
        f.close()
        
    return
   
def DisplayAvatourItemShopData():
    global gAvatourItemShopTab
    global gCurrentAvatourItemShopURL
    global gCurrentAvatourItemShopName
    global gAvatourItemListOnAvatourItemShopTab
    global gAvatourItemListBoxOnAvatourItemShopTab
    
    gAvatourItemListBoxOnAvatourItemShopTab.delete(0, tkinter.END);
    
    for s1 in gAvatourItemListOnAvatourItemShopTab:
        gAvatourItemListBoxOnAvatourItemShopTab.insert(tkinter.END, s1[1])
        
    return

def gAvatourItemListBoxOnAddAvatourItmSelected(event):
    global gAddAvatourItemTab
    global gHavingAvatourItemListBox
    global gMyHavingAvatourItem
    global gAddAvatorItemTabItmImgLabel
    
    if not gHavingAvatourItemListBox.curselection():
        return 
    crSelectIdx = gHavingAvatourItemListBox.curselection()[0];

    imgURL = getAvatourItemImgURL(gMyHavingAvatourItem[crSelectIdx][0], gMyHavingAvatourItem[crSelectIdx][1])
    img = Image.open(imgURL);
    img = img.resize((100, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img)
    gAddAvatorItemTabItmImgLabel.configure(image=img2)
    gAddAvatorItemTabItmImgLabel.image = img2
    gAddAvatorItemTabItmImgLabel.place(x=300, y=50)
    
    im2 = cv2.imread(imgURL)
    sh, sw, c = im2.shape;

    return 0     
def gAddAvatourItemTab_main():
    global gAddAvatourItemTab
    global gAvatourImg
    global gAddAvatourItemTabPosXEntry
    global gAddAvatourItemTabPosYEntry
    global gAddAvatourItemTabPosZEntry
    global gAddAvatourItemTabSizeXEntry
    global gAddAvatourItemTabSizeYEntry
    global gHavingAvatourItemListBox
    global gMyHavingAvatourItem
    global gAddAvatorItemTabItmImgLabel
    global gPointLabelOnAddAvatourItemTab
    global gHavingAvatourItemListBox
    
    
    #文字を表示する。
    param_name = tkinter.Label(gAddAvatourItemTab, text="アバターアイテム追加")
    param_name.place(x=10, y=30)

    #ListBox
    gHavingAvatourItemListBox = Listbox(gAddAvatourItemTab, height=10)
    gHavingAvatourItemListBox.place(x=10, y=60)
    gHavingAvatourItemListBox.bind('<<ListboxSelect>>',gAvatourItemListBoxOnAddAvatourItmSelected);
    
    LoadHavingAvatourItem()
    
    gHavingAvatourItemListBox.delete(0, tkinter.END);
    for hFn in gMyHavingAvatourItem:
        gHavingAvatourItemListBox.insert(tkinter.END, hFn[2])
        
    # Scrollbar
    scrollbar = ttk.Scrollbar(
        gAddAvatourItemTab,
        orient=VERTICAL,
        command=gHavingAvatourItemListBox.yview)
    gHavingAvatourItemListBox['yscrollcommand'] = scrollbar.set
    scrollbar.place(x=150, y=60, width=30, height=150)
    
    posLabel = tkinter.Label(gAddAvatourItemTab, text="配置位置")
    posLabel.place(x=200, y=60)
    
    posLabel2 = tkinter.Label(gAddAvatourItemTab, text="x位置:")
    posLabel2.place(x=200, y=90)
    gAddAvatourItemTabPosXEntry = tkinter.Entry(gAddAvatourItemTab, width=4)
    gAddAvatourItemTabPosXEntry.place(x=240, y=90)
    gAddAvatourItemTabPosXEntry.insert(0, "0")
    
    posLabel3 = tkinter.Label(gAddAvatourItemTab, text="y位置:")
    posLabel3.place(x=200, y=120)
    gAddAvatourItemTabPosYEntry = tkinter.Entry(gAddAvatourItemTab, width=4)
    gAddAvatourItemTabPosYEntry.place(x=240, y=120)
    gAddAvatourItemTabPosYEntry.insert(0, "0")
    

    posLabel4 = tkinter.Label(gAddAvatourItemTab, text="z位置:")
    posLabel4.place(x=200, y=150)
    gAddAvatourItemTabPosZEntry = tkinter.Entry(gAddAvatourItemTab, width=4)
    gAddAvatourItemTabPosZEntry.place(x=240, y=150)
    gAddAvatourItemTabPosZEntry.insert(0, "0")
        
    sizeLabel = tkinter.Label(gAddAvatourItemTab, text="大きさ")
    sizeLabel.place(x=200, y=180)
    
    sizeLabel2 = tkinter.Label(gAddAvatourItemTab, text="高さ:")
    sizeLabel2.place(x=200, y=210)
    gAddAvatourItemTabSizeYEntry = tkinter.Entry(gAddAvatourItemTab, width=4)
    gAddAvatourItemTabSizeYEntry.place(x=240, y=210)
    gAddAvatourItemTabSizeYEntry.insert(0, "0")
        
    sizeLabel3 = tkinter.Label(gAddAvatourItemTab, text="幅:")
    sizeLabel3.place(x=200, y=240)
    gAddAvatourItemTabSizeXEntry = tkinter.Entry(gAddAvatourItemTab, width=4)
    gAddAvatourItemTabSizeXEntry.place(x=240, y=240)
    gAddAvatourItemTabSizeXEntry.insert(0, "0")
    
    img = Image.open("blank.png");
    img = img.resize((100, 100), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img)
    gAddAvatorItemTabItmImgLabel = tkinter.Label(gAddAvatourItemTab, image=img2)
    gAddAvatorItemTabItmImgLabel.image = img2
    gAddAvatorItemTabItmImgLabel.place(x=300, y=50)
    
        
    DisplayAvatour()
    
    button1 = ttk.Button(
        gAddAvatourItemTab,
        text='装備プレビュー',
        command=DisplayAvatourItemPreViewCallBack())
    button1.place(x=10,y=240)
    
    button2 = ttk.Button(
        gAddAvatourItemTab,
        text='40pt使ってアイテム装備',
        command=setItemCallBack())
    button2.place(x=10,y=270)
    
    return 0
    
def DisplayAvatourItemPreViewCallBack():
    
    def DisplayAvatourItemPreView():
    
        global gCurrentPreviewAvatourImg
        global gAvatourItmPosX
        global gAvatourItmPosY
        global gAvatourItmPosZ
        global gAvatourItmSizeX
        global gAvatourItmSizeY
        global gAddAvatourItemTab
        global gHavingAvatourItemListBox
        global gMyHavingAvatourItem
        global gAddAvatorItemTabItmImgLabel
        global gMyAvatourItem
        global gMyAvatourPrev
        global gAvatourBlankType
    
        if not gHavingAvatourItemListBox.curselection():
            return 
        crSelectIdx = gHavingAvatourItemListBox.curselection()[0];

        if not getAvatourItemPosAndSizeEntryVals():
            return
            
        gMyAvatourPrev = gMyAvatourItem.copy()

        
        val1 = [gMyHavingAvatourItem[crSelectIdx][0], gMyHavingAvatourItem[crSelectIdx][1], gAvatourItmPosX, gAvatourItmPosY, gAvatourItmPosZ, gAvatourItmSizeY, gAvatourItmSizeX]
        gMyAvatourPrev.append(val1)

        gMyAvatourPrev = sorted(gMyAvatourPrev, reverse=False, key=lambda x:x[4])
        
        if gAvatourBlankType == 1:
            avatourImg = cv2.imread("AvatourBlank1.png")
        else:
            avatourImg = cv2.imread("AvatourBlank2.png")
                      
        avatourImg = cv2.resize(avatourImg, (gAvatourWidth, gAvatourHeight) )
        
        for fn in gMyAvatourPrev:
            fnURL = getAvatourItemImgURL(fn[0], fn[1])
            fnImg = cv2.imread(fnURL)
            avatourImg = AddImage(avatourImg, fnImg, fn[2], fn[3], fn[5], fn[6])
        
        gCurrentPreviewRoomImg = avatourImg

        cv2.imshow("previewAvatour", avatourImg)
        
        return
    
    return DisplayAvatourItemPreView

def getAvatourItemPosAndSizeEntryVals():
    global gAvatourItmPosX
    global gAvatourItmPosY
    global gAvatourItmPosZ
    global gAvatourItmSizeX
    global gAvatourItmSizeY
    global gAddFanitureTab
    global gAvatourImg
    global gAddAvatourItemTabPosXEntry
    global gAddAvatourItemTabPosYEntry
    global gAddAvatourItemTabPosZEntry
    global gAddAvatourItemTabSizeXEntry
    global gAddAvatourItemTabSizeYEntry
        
    gAvatourItmPosX = 0
    gAvatourItmPosY = 0
    gAvatourItmPosZ = 0
    gAvatourItmSizeX = 0
    gAvatourItmSizeY = 0
    
    NStr1 = gAddAvatourItemTabPosXEntry.get()
    if not NStr1.isdecimal():
        return False
    else :
        Num = int(NStr1)
        if Num < 0:
            return False
        else:
            gAvatourItmPosX = Num
            
    NStr2 = gAddAvatourItemTabPosYEntry.get()
    if not NStr2.isdecimal():
        return False
    else :
        Num = int(NStr2)
        if Num < 0:
            return False
        else:
            gAvatourItmPosY = Num
            
    NStr5 = gAddAvatourItemTabPosZEntry.get()
    if not NStr5.isdecimal():
        return False
    else :
        Num = int(NStr5)
        if Num < 0:
            return False
        else:
            gAvatourItmPosZ = Num            
            
    NStr3 = gAddAvatourItemTabSizeXEntry.get()
    if not NStr3.isdecimal():
        return False
    else :
        Num = int(NStr3)
        if Num <= 0:
            return False
        else:
            gAvatourItmSizeX = Num
            
    NStr4 = gAddAvatourItemTabSizeYEntry.get()
    if not NStr4.isdecimal():
        return False
    else :
        Num = int(NStr4)
        if Num <= 0:
            return False
        else:
            gAvatourItmSizeY = Num
        
    return True
    
def DisplayAvatour():
    global gAvatourBlankType
    global gMyAvatourItem
    global gCurrentAvatourImg
    global gAvatourWidth
    global gAvatourHeight
    
    if gAvatourBlankType == 1:
        avatourImg = cv2.imread("AvatourBlank1.png")
    else:
        avatourImg = cv2.imread("AvatourBlank2.png")
      
    avatourImg = cv2.resize(avatourImg, (gAvatourWidth, gAvatourHeight) )
    LoadAvatour()

    for fn in gMyAvatourItem:
        fnURL = getAvatourItemImgURL(fn[0], fn[1])
        fnImg = cv2.imread(fnURL)
        avatourImg = AddImage(avatourImg, fnImg, fn[2], fn[3], fn[5], fn[6])
    
    gCurrentAvatourImg = avatourImg

    cv2.namedWindow("avatour", cv2.WINDOW_NORMAL)
    cv2.imshow("avatour", avatourImg)
    cv2.moveWindow('avatour', 200, 200)
    
    return

def getAvatourItemImgURL(avatourItemShopURL, itmId):
    path1 = avatourItemShopURL + '\AvatourItemShopInfo.txt'
    
    path2 = ""
    try:
        f = open(path1, encoding='UTF-8')
    except OSError as e:
        return
    else:
        lines = f.readlines()
        #最初の一行目読み飛ばし
        lines.pop(0);
        
        for line in lines:
            line = line.rstrip('\n')
            vars = line.split(',');
            id = int(vars[0])
            if id == itmId:
                path2 = avatourItemShopURL + "\\" + vars[2]
                break
        
        f.close()
        
    return path2
    
def LoadHavingAvatourItem():
    global gMyHavingAvatourItem
    
    URL = os.getcwd()
    path1 = URL + '\prop\MyHavingAvatourItem.txt'
    
    try:
        f = open(path1, encoding='UTF-8')
    except OSError as e:
        messagebox.showinfo('エラー','所持中アバターアイテムリストファイルがありません')
        return
    else:
        lines = f.readlines()
        
        gMyHavingAvatourItem = [];
        for line in lines:
            line = line.rstrip('\n')
            vars = line.split(',');
            vars[1] = int(vars[1])
            #市場URL,商品ID
            gMyHavingAvatourItem.append(vars) 
        
        f.close()
        
        for fn1 in gMyHavingAvatourItem:
            name1 = getAvatourItemName(fn1[0], fn1[1])
            fn1.append(name1)
        
        #市場URL,商品ID,商品名
        gMyHavingAvatourItem = sorted(gMyHavingAvatourItem, reverse=False, key=lambda x:x[2])
        
    return
    
def getAvatourItemName(avatourShopURL, itmId):
    path1 = avatourShopURL + '\AvatourItemShopInfo.txt'
    
    path2 = ""
    try:
        f = open(path1, encoding='UTF-8')
    except OSError as e:
        return
    else:
        lines = f.readlines()
        #最初の一行目読み飛ばし
        lines.pop(0);
        
        for line in lines:
            line = line.rstrip('\n')
            vars = line.split(',');
            id = int(vars[0])
            if id == itmId:
                name = vars[1]
                break
        
        f.close()
   
    return name


#現在装備しているアバターアイテムのリストをロードする    
def LoadAvatour():
    global gMyAvatourItem
    
    URL = os.getcwd()
    path1 = URL + '\prop\MyAvatour.txt'
    
    try:
        f = open(path1, encoding='UTF-8')
    except OSError as e:
        messagebox.showinfo('エラー','装備中アバターアイテムデータがありません')
        return
    else:
        lines = f.readlines()
        
        gMyAvatourItem = [];
        for line in lines:
            line = line.rstrip('\n')
            vars = line.split(',');
            #市場URL,商品ID,x位置,y位置,z位置,高さ,幅
            gMyAvatourItem.append(vars) 
        
        f.close()
        
        for fn1 in gMyAvatourItem:
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
        
        gMyAvatourItem = sorted(gMyAvatourItem, reverse=False, key=lambda x:x[4])
        
        
    return

def setItemCallBack():

    def setItem():
        global gMyHavingAvatourItem
        global gAddAvatourItemTabPosXEntry
        global gAddAvatourItemTabPosYEntry
        global gAddAvatourItemTabPosZEntry
        global gAddAvatourItemTabSizeXEntry
        global gAddAvatourItemTabSizeYEntry
        global gHavingAvatourItemListBox
        global gCurrentToDoTaskPoint
        global gMyAvatourItem
        
        if not getAvatourItemPosAndSizeEntryVals():
            return
            
        
        if not gHavingAvatourItemListBox.curselection():
            return 
        crSelectIdx = gHavingAvatourItemListBox.curselection()[0];
        
        needPt = 40
        if gCurrentToDoTaskPoint < needPt:
            messagebox.showinfo('メッセージ','配置に必要なポイントが足りません')
            return
        
        addMyAvatourItemList(gMyHavingAvatourItem[crSelectIdx][0],gMyHavingAvatourItem[crSelectIdx][1])
        gCurrentToDoTaskPoint = gCurrentToDoTaskPoint - needPt
        
        saveMyAvatourItemList()
        
        DisplayCuttentToDoTaskPointTab()
        DisplayAvatour()
        
        return

    return setItem

def saveMyAvatourItemList():
    global gMyAvatourItem
    
    try:
        URL = os.getcwd()
        path1 = URL + "\\prop\MyAvatour.txt"
        f = open(path1, encoding='UTF-8', mode='w')
    except OSError as e:
        messagebox.showinfo('エラー','ファイルのオープンに失敗しました')
        return
    else:
        for t1 in gMyAvatourItem:
            f.write(','.join(map(str,t1)))
            f.write('\n')
        
        f.close()

    return

def addMyAvatourItemList(avatourShopURL, itmId):
    global gMyAvatourItem
    global gAvatourItmPosX
    global gAvatourItmPosY
    global gAvatourItmPosZ
    global gAvatourItmSizeX
    global gAvatourItmSizeY
    
    if not getAvatourItemPosAndSizeEntryVals():
        return
        
    var1 = [avatourShopURL, itmId, gAvatourItmPosX, gAvatourItmPosY, gAvatourItmPosZ, gAvatourItmSizeY, gAvatourItmSizeX]
    gMyAvatourItem.append(var1)
    
    return
    
def gDeleteFanitureTab_main():
    global gDeleteFanitureTab
    global gDeleteFanitureTabTree
    
    LoadFaniture()
    
    #文字を表示する。
    param_name = tkinter.Label(gDeleteFanitureTab, text="家具削除")
    param_name.place(x=10, y=30)
    
    label1 = tkinter.Label(gDeleteFanitureTab, text="配置中家具一覧")
    label1.place(x=10, y=60)
    
    gDeleteFanitureTabTree = ttk.Treeview(gDeleteFanitureTab);

    gDeleteFanitureTabTree["columns"] = (1, 2, 3, 4)
    gDeleteFanitureTabTree["show"] = "headings"

    gDeleteFanitureTabTree.column(1,width=150)
    gDeleteFanitureTabTree.column(2,width=100)
    gDeleteFanitureTabTree.column(3,width=100)
    gDeleteFanitureTabTree.column(4,width=200)
    
    gDeleteFanitureTabTree.heading(1,text="家具名")
    gDeleteFanitureTabTree.heading(2,text="位置(x, y, z)")
    gDeleteFanitureTabTree.heading(3,text="サイズ(h,w)")
    gDeleteFanitureTabTree.heading(4,text="操作")
    
    gDeleteFanitureTabTree.place(x=10, y=90)
    
    DisplayFanitureListTab();
    
    return 0        
    
def DisplayFanitureListTab():
    global gDeleteFanitureTab
    global gDeleteFanitureTabTree
    global gFanitureDelButtons
    global gFanitureDelPrevButtons
    global gMyFaniture
    
    for i in gDeleteFanitureTabTree.get_children():
        gDeleteFanitureTabTree.delete(i)
    
    for b1 in gFanitureDelPrevButtons:
        b1.place_forget()

    for b2 in gFanitureDelButtons:
        b2.place_forget()
        


    style = ttk.Style(gDeleteFanitureTab)
    style.configure("Treeview", rowheight=30)
    
    lineIdx=0
    for t1 in gMyFaniture:

        name = getFanitureName(t1[0], t1[1])
        
        positionStr = '( '
        positionStr += str(t1[2])
        positionStr += ', '
        positionStr += str(t1[3])
        positionStr += ', '
        positionStr += str(t1[4])
        positionStr += ' )'
        
        sizeStr = '( '
        sizeStr += str(t1[5])
        sizeStr += ', '
        sizeStr += str(t1[6])
        sizeStr += ' )'
        
        gDeleteFanitureTabTree.insert("","end",values=(name,positionStr,sizeStr, ""))    
        
        # ボタン
        button1 = ttk.Button(
            gDeleteFanitureTab,
            text='削除後のプレビュー',
            command=showDelFaniturePreviewCallBack(lineIdx))
        button1.place(x=370,y=120+30*lineIdx)
        gFanitureDelPrevButtons.append(button1)
        
        button2 = ttk.Button(
            gDeleteFanitureTab,
            text='この家具を削除',
            command=delFanitureCallBack(lineIdx))
        button2.place(x=470,y=120+30*lineIdx)
        gFanitureDelButtons.append(button2)
        
        lineIdx = lineIdx + 1
          
    return  0
    
def delFanitureCallBack(delLineIdx):
    
    def delFaniture():
        global gMyFaniture
            
        lineIdx = 0
        result=[]
        for t1 in gMyFaniture:
            if lineIdx != delLineIdx:
                result.append(t1) 
        
            lineIdx = lineIdx + 1
        
        gMyFaniture = result
        
        saveFanitureList()
        
        DisplayFanitureListTab()
        DisplayRoom()
        
    return delFaniture

def saveFanitureList():
    global gMyFaniture
        
    try:
        URL = os.getcwd()
        path1 = URL + "\\prop\MyRoomFaniture.txt"
        f = open(path1, encoding='UTF-8', mode='w')
    except OSError as e:
        messagebox.showinfo('エラー','ファイルのオープンに失敗しました')
        return
    else:
        for t1 in gMyFaniture:
            f.write(','.join(map(str,t1)))
            f.write('\n')
            
        f.close()



def showDelFaniturePreviewCallBack(delLineIdx):

    def showDelFaniturePreview():
        global gCurrentPreviewRoomImg
        global gRoomWidth
        global gRoomHeight
        global gMyFaniture
        global gMyDelFaniturePrev
    
    
        gMyDelFaniturePrev = gMyFaniture.copy()
        gMyDelFaniturePrev.pop(delLineIdx)
        
        roomImg = cv2.imread("blank.png")    
        roomImg = cv2.resize(roomImg, (gRoomWidth, gRoomHeight) )
        
        for fn in gMyDelFaniturePrev:
            fnURL = getFanitureImgURL(fn[0], fn[1])
            fnImg = cv2.imread(fnURL)
            roomImg = AddImage(roomImg, fnImg, fn[2], fn[3], fn[5], fn[6])
        
        gCurrentPreviewRoomImg = roomImg

        cv2.imshow("previewRoom", roomImg)
        
        return
    
    return showDelFaniturePreview


def gDeleteAvatourItemTab_main():
    global gDeleteAvatourItemTab
    global gDeleteAvatourItemTabTree
    
    LoadAvatour()
    
    #文字を表示する。
    param_name = tkinter.Label(gDeleteAvatourItemTab, text="アバターアイテム削除")
    param_name.place(x=10, y=30)
    
    label1 = tkinter.Label(gDeleteAvatourItemTab, text="装備中アバターアイテム一覧")
    label1.place(x=10, y=60)
    
    gDeleteAvatourItemTabTree = ttk.Treeview(gDeleteAvatourItemTab);

    gDeleteAvatourItemTabTree["columns"] = (1, 2, 3, 4)
    gDeleteAvatourItemTabTree["show"] = "headings"

    gDeleteAvatourItemTabTree.column(1,width=150)
    gDeleteAvatourItemTabTree.column(2,width=100)
    gDeleteAvatourItemTabTree.column(3,width=100)
    gDeleteAvatourItemTabTree.column(4,width=250)
    
    gDeleteAvatourItemTabTree.heading(1,text="アイテム名")
    gDeleteAvatourItemTabTree.heading(2,text="位置(x, y, z)")
    gDeleteAvatourItemTabTree.heading(3,text="サイズ(h,w)")
    gDeleteAvatourItemTabTree.heading(4,text="操作")
    
    gDeleteAvatourItemTabTree.place(x=10, y=90)
    
    DisplayAvatourItemListTab();
    
    return 0
    
def DisplayAvatourItemListTab():
    global gDeleteAvatourItemTab
    global gDeleteAvatourItemTabTree
    global gAvatourItemDelButtons
    global gAvatourItemDelPrevButtons
    global gMyAvatourItem
    global gMyAvatourPrev
    
    for i in gDeleteAvatourItemTabTree.get_children():
        gDeleteAvatourItemTabTree.delete(i)
    
    for b1 in gAvatourItemDelPrevButtons:
        b1.place_forget()

    for b2 in gAvatourItemDelButtons:
        b2.place_forget()
        

    style = ttk.Style(gDeleteAvatourItemTab)
    style.configure("Treeview", rowheight=30)
    
    lineIdx=0
    for t1 in gMyAvatourItem:

        name = getAvatourItemName(t1[0], t1[1])
        
        positionStr = '( '
        positionStr += str(t1[2])
        positionStr += ', '
        positionStr += str(t1[3])
        positionStr += ', '
        positionStr += str(t1[4])
        positionStr += ' )'
        
        sizeStr = '( '
        sizeStr += str(t1[5])
        sizeStr += ', '
        sizeStr += str(t1[6])
        sizeStr += ' )'
        
        gDeleteAvatourItemTabTree.insert("","end",values=(name,positionStr,sizeStr, ""))    
        
        # ボタン
        button1 = ttk.Button(
            gDeleteAvatourItemTabTree,
            text='削除後のプレビュー',
            command=showDelAvatourItemPreviewCallBack(lineIdx))
        button1.place(x=370,y=30+30*lineIdx)
        gAvatourItemDelPrevButtons.append(button1)
        
        button2 = ttk.Button(
            gDeleteAvatourItemTabTree,
            text='このアイテムを削除',
            command=delAvatourItemCallBack(lineIdx))
        button2.place(x=470,y=30+30*lineIdx)
        gAvatourItemDelButtons.append(button2)
        
        lineIdx = lineIdx + 1
          
    return  0
    
def delAvatourItemCallBack(delLineIdx):
    
    def delAvatourItem():
        global gMyAvatourItem
            
        lineIdx = 0
        result=[]
        for t1 in gMyAvatourItem:
            if lineIdx != delLineIdx:
                result.append(t1) 
        
            lineIdx = lineIdx + 1
        
        gMyAvatourItem = result
        
        saveAvatourItemList()
        
        DisplayAvatourItemListTab()
        DisplayAvatour()
        
    return delAvatourItem

def saveAvatourItemList():
    global gMyAvatourItem
        
    try:
        URL = os.getcwd()
        path1 = URL + "\\prop\MyAvatour.txt"
        f = open(path1, encoding='UTF-8', mode='w')
    except OSError as e:
        messagebox.showinfo('エラー','ファイルのオープンに失敗しました')
        return
    else:
        for t1 in gMyAvatourItem:
            f.write(','.join(map(str,t1)))
            f.write('\n')
            
        f.close()

def showDelAvatourItemPreviewCallBack(delLineIdx):

    def showDelAvatourItemPreview():
        global gCurrentPreviewAvatourImg
        global gAvatourBlankType
        global gAvatourWidth
        global gAvatourHeight
        global gMyAvatourItem
        global gMyAvatourPrev
        
        global gAvatourBlankType
        global gMyAvatourItem
        global gMyAvatourPrev
        global gCurrentAvatourImg
        

        
        LoadAvatour()

        gMyAvatourPrev = gMyAvatourItem.copy()
        gMyAvatourPrev.pop(delLineIdx)
        
        if gAvatourBlankType == 1:
            avatourImg = cv2.imread("AvatourBlank1.png")
        else:
            avatourImg = cv2.imread("AvatourBlank2.png")
          
        avatourImg = cv2.resize(avatourImg, (gAvatourWidth, gAvatourHeight) )
        
        for fn in gMyAvatourPrev:
            fnURL = getAvatourItemImgURL(fn[0], fn[1])
            itmImg = cv2.imread(fnURL)
            avatourImg = AddImage(avatourImg, itmImg, fn[2], fn[3], fn[5], fn[6])
        
        gCurrentPreviewAvatourImg = avatourImg

        cv2.imshow("previewAvatour", avatourImg)
        
        return
    
    return showDelAvatourItemPreview
    
def gShowCurrentToDoTaskPointTab_main():
    global gShowCurrentToDoTaskPointTab
    global gCurrentToDoTaskPoint
    global gCurrentToDoTaskPointStrLabel
    
    #文字を表示する。
    str1 = "現在のポイント数:"
    str1 += str(gCurrentToDoTaskPoint)
    gCurrentToDoTaskPointStrLabel = tkinter.Label(gShowCurrentToDoTaskPointTab, text=str1)
    gCurrentToDoTaskPointStrLabel.place(x=10, y=30)
    

def MakeAvatourImage():
    global gAvatourBlankType
    global gMyAvatourItem
    global gCurrentAvatourImg
    global gAvatourWidth
    global gAvatourHeight
    
    if gAvatourBlankType == 1:
        avatourImg = cv2.imread("AvatourBlank1.png")
    else:
        avatourImg = cv2.imread("AvatourBlank2.png")
      
    avatourImg = cv2.resize(avatourImg, (gAvatourWidth, gAvatourHeight) )
    LoadAvatour()

    for fn in gMyAvatourItem:
        fnURL = getAvatourItemImgURL(fn[0], fn[1])
        fnImg = cv2.imread(fnURL)
        avatourImg = AddImage(avatourImg, fnImg, fn[2], fn[3], fn[5], fn[6])
    
    gCurrentAvatourImg = avatourImg
    
    return gCurrentAvatourImg
    
def DisplayCuttentToDoTaskPointTab():
    global gCurrentToDoTaskPointStrLabel
    global gCurrentToDoTaskPoint
    
    #文字を表示する。
    str1 = "現在のポイント数:"
    str1 += str(gCurrentToDoTaskPoint)
    gCurrentToDoTaskPointStrLabel.configure(text=str1);
    
    return

def gAvatourConfigurationTab_main():
    global gAvatourConfigurationTab    
    global gAvatourConfigurationTabPosXEntry
    global gAvatourConfigurationTabPosYEntry
    global gAvatourConfigurationTabPosZEntry
    global gAvatourConfigurationTabSizeXEntry
    global gAvatourConfigurationTabSizeYEntry
    global gVisibleFlgRadioValue
    global gAvatourBlankTypeRadioValue
    
    #文字を表示する。
    param_name = tkinter.Label(gAvatourConfigurationTab, text="アバター表示設定")
    param_name.place(x=10, y=30)

    visibleFlgLabel = tkinter.Label(gAvatourConfigurationTab, text="アバターの表示")
    visibleFlgLabel.place(x=10, y=60)
    
    gVisibleFlgRadioValue = tkinter.IntVar(master=gAddTaskTab, value=True)
    rdioVisible = tkinter.Radiobutton(gAvatourConfigurationTab, variable = gVisibleFlgRadioValue, text="表示する", value=True)
    rdioHidden = tkinter.Radiobutton(gAvatourConfigurationTab, variable = gVisibleFlgRadioValue, text="表示しない", value=False)
    
    rdioVisible.place(x=10, y=90)
    rdioHidden.place(x=10, y=120)   
    
    label2 = tkinter.Label(gAvatourConfigurationTab, text="アバターの下地")
    label2.place(x=10, y=150)
    
    gAvatourBlankTypeRadioValue = tkinter.IntVar(master=gAddTaskTab, value=1)
    rdioWireFlameBlank = tkinter.Radiobutton(gAvatourConfigurationTab, variable = gAvatourBlankTypeRadioValue, text="あり", value=1)
    rdioAllBlank = tkinter.Radiobutton(gAvatourConfigurationTab, variable = gAvatourBlankTypeRadioValue, text="なし", value=2)
    
    rdioWireFlameBlank.place(x=10, y=180)
    rdioAllBlank.place(x=10, y=210)
    
    label3 = tkinter.Label(gAvatourConfigurationTab, text="アバターの表示位置")
    label3.place(x=100, y=30)
    
    posLabel1 = tkinter.Label(gAvatourConfigurationTab, text="x位置:")
    posLabel1.place(x=100, y=60)
    gAvatourConfigurationTabPosXEntry = tkinter.Entry(gAvatourConfigurationTab, width=4)
    gAvatourConfigurationTabPosXEntry.place(x=150, y=60)
    gAvatourConfigurationTabPosXEntry.insert(0, "0")
    
    posLabel3 = tkinter.Label(gAvatourConfigurationTab, text="y位置:")
    posLabel3.place(x=100, y=90)
    gAvatourConfigurationTabPosYEntry = tkinter.Entry(gAvatourConfigurationTab, width=4)
    gAvatourConfigurationTabPosYEntry.place(x=150, y=90)
    gAvatourConfigurationTabPosYEntry.insert(0, "0")
    

    posLabel4 = tkinter.Label(gAvatourConfigurationTab, text="z位置:")
    posLabel4.place(x=100, y=120)
    gAvatourConfigurationTabPosZEntry = tkinter.Entry(gAvatourConfigurationTab, width=4)
    gAvatourConfigurationTabPosZEntry.place(x=150, y=120)
    gAvatourConfigurationTabPosZEntry.insert(0, "0")
    
    label3 = tkinter.Label(gAvatourConfigurationTab, text="アバターのサイズ")
    label3.place(x=100, y=150)
    
    sizeLabel2 = tkinter.Label(gAvatourConfigurationTab, text="高さ:")
    sizeLabel2.place(x=100, y=180)
    gAvatourConfigurationTabSizeYEntry = tkinter.Entry(gAvatourConfigurationTab, width=4)
    gAvatourConfigurationTabSizeYEntry.place(x=150, y=180)
    gAvatourConfigurationTabSizeYEntry.insert(0, "0")
        
    sizeLabel3 = tkinter.Label(gAvatourConfigurationTab, text="幅:")
    sizeLabel3.place(x=100, y=210)
    gAvatourConfigurationTabSizeXEntry = tkinter.Entry(gAvatourConfigurationTab, width=4)
    gAvatourConfigurationTabSizeXEntry.place(x=150, y=210)
    gAvatourConfigurationTabSizeXEntry.insert(0, "0")
        
    button1 = ttk.Button(
        gAvatourConfigurationTab,
        text='決定',
        command=changeConfigurationCallBack())
    button1.place(x=10,y=250)

def changeConfigurationCallBack():

    def changeConfiguration():
        global gVisibleFlgRadioValue
        global gAvatourBlankTypeRadioValue
        global gAvatourBlankType
        global gAvatourVisibleFlg
        
        if not getPosAndSizeEntryValsOnAvatourConfigurationTab():
            return
        
        gAvatourVisibleFlg = gVisibleFlgRadioValue.get()
        gAvatourBlankType = gAvatourBlankTypeRadioValue.get()
        
        DisplayRoom()
        
        return 0
        
    return changeConfiguration

def getPosAndSizeEntryValsOnAvatourConfigurationTab():    
    global gAvatourWidth
    global gAvatourHeight
    global gAvatourPosX
    global gAvatourPosY
    global gAvatourPosZ
    global gAvatourConfigurationTabPosXEntry
    global gAvatourConfigurationTabPosYEntry
    global gAvatourConfigurationTabPosZEntry
    global gAvatourConfigurationTabSizeXEntry
    global gAvatourConfigurationTabSizeYEntry 
        
    gFnPosX = 0
    gFnPosY = 0
    gFnPosZ = 0
    gFnSizeX = 0
    gFnSizeY = 0
    
    NStr1 = gAvatourConfigurationTabPosXEntry.get()
    if not NStr1.isdecimal():
        return False
    else :
        Num = int(NStr1)
        if Num < 0:
            return False
        else:
            gAvatourPosX = Num
            
    NStr2 = gAvatourConfigurationTabPosYEntry.get()
    if not NStr2.isdecimal():
        return False
    else :
        Num = int(NStr2)
        if Num < 0:
            return False
        else:
            gAvatourPosY = Num
            
    NStr5 = gAvatourConfigurationTabPosZEntry.get()
    if not NStr5.isdecimal():
        return False
    else :
        Num = int(NStr5)
        if Num < 0:
            return False
        else:
            gAvatourPosZ = Num            
            
    NStr3 = gAvatourConfigurationTabSizeXEntry.get()
    if not NStr3.isdecimal():
        return False
    else :
        Num = int(NStr3)
        if Num <= 0:
            return False
        else:
            gAvatourWidth = Num
            
    NStr4 = gAvatourConfigurationTabSizeYEntry.get()
    if not NStr4.isdecimal():
        return False
    else :
        Num = int(NStr4)
        if Num <= 0:
            return False
        else:
            gAvatourHeight = Num
        
    return True

if __name__ == "__main__":
    main()
    
    

