
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
    
    nb.add(gSijoTab1, text="市場", padding=3)
    nb.add(gTaskListTab, text="タスク一覧", padding=3)
    nb.add(gAddTaskTab, text="タスク追加", padding=3)
    
    #メインフレームでのnotebook配置を決定する。
    nb.pack(expand=1, fill="both")
 
    #各タブの内容を記載する。
    sijoTab_main()
    gTaskListTab_main()
    gAddTaskTab_main()
 
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
if __name__ == "__main__":
    main()
    
    

