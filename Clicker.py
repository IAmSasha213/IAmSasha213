#Саша Лихотворик
from tkinter import *   
g=1
t=1
d=0
def jmyak():
    global g, t
    lbl1.configure(text = '{}$'.format(g))
    lbl2.configure(text = '{} за 1 клик'.format(t))  
    g=g+t
def jmyak2():
    global t, g
    if g==100 or g>100:
        t=t+1
        g=g-100
        lbl1.configure(text = '{}$'.format(g))
        lbl2.configure(text = '{} за 1 клик$'.format(t))  
def jmyak3():
    global t, g
    if g==750 or g>750:
        t=t+10
        g=g-750
        lbl1.configure(text = '{}$'.format(g))
        lbl2.configure(text = '{} за 1 клик'.format(t))  
def jmyak4():
    global t, g
    if g==10000 or g>10000:
        t=t+110
        g=g-10000
        lbl1.configure(text = '{}$'.format(g))
        lbl2.configure(text = '{} за 1 клик'.format(t))  
def jmyak10():
    global t, g
    if g==100000000000000000000000000000000000000000000 or g>100000000000000000000000000000000000000000000:
        g=g-100000000000000000000000000000000000000000000
        print("Спасибо за то что играли в мою игру:)")
        exit()
def jmyak5():
    global t, g
    if g==100000000000 or g>100000000000:
        t=t*2
        g=g-100000000000
        lbl1.configure(text = '{}$'.format(g))
        lbl2.configure(text = '{} за 1 клик'.format(t)) 
def jmyak16():
    global d
    if d == 1:
        btn2 = Button(window, text="улучшение(+1 за клик)100$", command=jmyak2)  
        btn2.pack()
        btn3 = Button(window, text="улучшение(+10 за клик)750$", command=jmyak3)  
        btn3.pack()
        btn4 = Button(window, text="улучшение(+110 за клик)10000$", command=jmyak4)  
        btn4.pack()
        btn5 = Button(window, text="улучшение(*2 за клик)100000000000$", command=jmyak5)  
        btn5.pack()
        btn6 = Button(window, text="конец игры 100000000000000000000000000000000000000000000$", command=jmyak10)  
        btn6.pack()
        btn1.configure(text="открыть")
        btn1.pack
        d=0
    elif d == 0:
        btn2.pack_forget
        btn3.pack_forget
        btn4.pack_forget
        btn5.pack_forget
        btn6.pack_forget
        btn1.configure(text="закрыть")
        btn1.pack
        d=1
window = Tk()  
window.title("Добро пожаловать в приложение") 
window.geometry('400x250')
gui_game_screen=Label(window,text="CLICKER_VERY_WELL")
lbl = Label(window, text="money")  
lbl.pack()
lbl1 = Label(window, text=g)  
lbl1.pack()
btn = Button(window, text="клик", command=jmyak)  
btn.pack()
btn1 = Button(window, text="закрыть", command=jmyak16)  
btn1.pack()
btn = Button(window, text="улучшение(+1 за клик)100$", command=jmyak2)  
btn.pack()
btn = Button(window, text="улучшение(+10 за клик)750$", command=jmyak3)  
btn.pack()
btn = Button(window, text="улучшение(+110 за клик)10000$", command=jmyak4)  
btn.pack()
btn = Button(window, text="улучшение(*2 за клик)100000000000$", command=jmyak5)  
btn.pack()
btn = Button(window, text="конец игры 100000000000000000000000000000000000000000000$", command=jmyak10)  
btn.pack()
lbl2 = Label(window, text = '{}$'.format(t))  
lbl2.pack()
canvas = Canvas(window,width=600,height=600,bg="white",)
canvas.pack()
canvas.create_line(0,0,600,600,width=5,fill="yellow")
canvas.create_line(0,600,600,0,width=5,fill="yellow")
canvas.create_rectangle(50,250,300,400,fill="red",outline="black")
canvas.create_oval([70,400],[10,10],fill="pink")
canvas.create_polygon([400,400],[300,400],[350,300],fill="gray", outline="yellow")
canvas.create_text(250,280,text="Текст в canvas",
          font="Verdana 12",justify=CENTER,fill="red")
text = '{}$'.format(g)
window.mainloop()
