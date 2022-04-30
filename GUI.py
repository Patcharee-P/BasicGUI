# GUI.py

from tkinter import *
from tkinter import ttk, messagebox

friend = {'1997':'พัชรี พลอินทร์','1996':'ไกรยศ วรรณา','2207':'แมวน้อย อิอิ'}

GUI = Tk()
GUI.title('โปรแกรมของฉัน')
GUI.geometry('500x300')

L = Label(GUI, text='กรุณากรอกรหัสชื่อ').pack(pady=30)

v_text = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_text,font=('Angsana New',20))
E1.pack(pady=20)

def Click():
	text = v_text.get() #ดึงข้อความที่ user พิมพ์ออกมา
	print('Text: ',text)
	if text in friend:
		result = friend[text]
		messagebox.showinfo('result','รหัส: {} คือชื่อ: {}'.format(text,result))
		print(friend[text])
	else:
		print('ไม่มีข้อมูลของคนนี้')
		messagebox.showwarning('Result: Error','ไม่มีข้อมูลในระบบ กรุณากรอกใหม่ หรือเพิ่มข้อมูลใหม่')


B1 = ttk.Button(GUI, text='Click me!',command=Click)
B1.pack(ipadx=50,ipady=30,pady=30)


GUI.mainloop()