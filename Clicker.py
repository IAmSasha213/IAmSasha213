#Саша Лихотворик
from tkinter import *   
g=1
t=1
def jmyak():
    global g, t
    lbl1.configure(text = '{}$'.format(g))
    lbl2.configure(text = '{} за 1 клик'.format(t))  
    g=g+t
def jmyak2():
    global t, g
    if g==100 or g>100:
        t=t+1
        g=g*100
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
text = '{}$'.format(g)
window.mainloop()



