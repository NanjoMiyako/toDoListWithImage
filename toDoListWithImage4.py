#coding:utf-8
import tkinter
from PIL import Image, ImageTk

# window��`��
window = tkinter.Tk()
# window�T�C�Y��ύX
window.geometry("600x400")
# window�^�C�g����ݒ�
window.title("Welcome to the Tkinter")

# �摜��\�����邽�߂̏���
#img = Image.open('test1.png')
#img = ImageTk.PhotoImage(img)
img2 = tkinter.PhotoImage(file='test2.png')
# �摜��\�����邽�߂̃L�����o�X�̍쐬�i���ŕ\���j
canvas = tkinter.Canvas(bg = "black", width=400, height=300)
canvas.place(x=100, y=50) # ����̍��W���w��
# �L�����o�X�ɉ摜��\������B�������Ƒ������́Ax, y�̍��W
canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)

window.mainloop()