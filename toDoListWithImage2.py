from tkinter import *
from tkinter import ttk

import numpy
import cv2

def show_selection():
    for i in lb.curselection():
        print(lb.get(i))
        
def newWindow():
    img = MixImage("test1.png", "test2.png");
    cv2.imshow("testWindow",img)

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
    
    

if __name__ == '__main__':
    root = Tk()
    root.title('Scrollbar 1')

    # Frame
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # Listbox
    currencies = (
        'JPY', 'USD', 'EUR', 
        'CNY', 'MXN', 'CAD')
    v1 = StringVar(value=currencies)
    lb = Listbox(frame1, listvariable=v1, height=10)
    lb.grid(row=0, column=0)

    # Scrollbar
    scrollbar = ttk.Scrollbar(
        frame1,
        orient=VERTICAL,
        command=lb.yview)
    lb['yscrollcommand'] = scrollbar.set
    scrollbar.grid(row=0, column=1, sticky=(N, S))

    # Button
    button1 = ttk.Button(
        frame1, text='OK',
        command=lambda: show_selection())
    button1.grid(row=1, column=0, columnspan=2)
    
    
    button2 = ttk.Button(
        frame1, text='new Window',
        command=lambda: newWindow())
    button2.grid(row=2, column=0, columnspan=2)

    root.mainloop()