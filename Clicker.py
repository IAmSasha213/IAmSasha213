#Саша Лихотворик
from tkinter import *   
g=100000000
t=1
h=0
d=0
def jmyak():
    global g, t
    lbl1.configure(text = '{}$'.format(g))
    lbl2.configure(text = '{} за 1 клик'.format(t))  
    g=g+t
def jmyak2():
    global t, g, h
    if g==100 or g>100 and g < 10000:
        t=5
        g=g-100
        lbl1.configure(text = '{}$'.format(g))
        lbl2.configure(text = '{} за 1 клик$'.format(t))
        canvas.create_rectangle(100,100,400,250,fill="red",outline="black")
        canvas.create_rectangle(120,120,250,170,fill="blue",outline="black")
        canvas.create_text(220,180,text="ВОЛГА",
              font="Verdana 12",justify=CENTER,fill="black")
        canvas.create_oval([110,180],[210,290],fill="black")
        canvas.create_oval([285,180],[385,290],fill="black")
        text = '{}$'.format(g)
        btn2.configure(text = "КУПИТЬ НИССАН 10000$")
        print(h)
    if g==10000 or g>10000:
        canvas.delete("all")
        canvas.create_rectangle(-10,-10,1000,1000,fill="white",outline="black")
        t=100
        g=g-10000
        lbl1.configure(text = '{}$'.format(g))
        lbl2.configure(text = '{} за 1 клик$'.format(t))
        canvas.create_rectangle(100,180,400,250,fill="gray",outline="black")
        canvas.create_polygon([200,100],[100,180],[200,180],fill="gray", outline="gray")
        canvas.create_rectangle(200,100,400,180,fill="gray",outline="gray")
        canvas.create_polygon([205,110],[105,190],[180,170],fill="blue", outline="blue")
        canvas.create_text(220,180,text="НИССАН",
                font="Verdana 12",justify=CENTER,fill="black")
        canvas.create_oval([120,190],[210,290],fill="black")
        canvas.create_oval([295,190],[385,290],fill="black")
        text = '{}$'.format(g)
def jmyak3():
    global t, g
    if g==750 or g>750:
        t=t+10
        g=g-750
        lbl1.configure(text = '{}$'.format(g))
        lbl2.configure(text = '{} за 1 клик'.format(t))
        canvas.create_polygon([400,100],[300,200],[400,200],fill="blue", outline="red")
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
window = Tk()  
window.title("Добро пожаловать в приложение") 
window.geometry('600x600')
gui_game_screen=Label(window,text="CLICKER_VERY_WELL")
lbl = Label(window, text="money")  
lbl.pack()
lbl1 = Label(window, text=g)  
lbl1.pack()
btn = Button(window, text="клик", command=jmyak)  
btn.pack()
btn2 = Button(window, text="купить волгу 100$", command=jmyak2)  
btn2.pack()
btn3 = Button(window, text="улучшение(+10 за клик)750$", command=jmyak3)  
btn3.pack()
btn4 = Button(window, text="улучшение(+110 за клик)10000$", command=jmyak4)  
btn4.pack()
btn5 = Button(window, text="улучшение(*2 за клик)100000000000$", command=jmyak5)  
btn5.pack()
btn6 = Button(window, text="конец игры 100000000000000000000000000000000000000000000$", command=jmyak10)  
btn6.pack()
lbl2 = Label(window, text = '{}$'.format(t))  
lbl2.pack()
canvas = Canvas(window,width=500,height=350,bg="white",)
canvas.pack()
window.mainloop()  
