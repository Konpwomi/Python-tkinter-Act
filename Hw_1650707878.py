from tkinter import *

def mainwindow() :
    root =Tk()
    root.title("GUI 3 : Class Activity of Week 4 Created by Patiphan Arphorn")
    root.geometry("750x600")
    root.rowconfigure(0,weight=4)
    root.rowconfigure(1,weight=10)
    root.rowconfigure(2,weight=6)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
    return(root)

def layout(root) :
    top = Frame(root,bg="#6096B4")
    top.grid(row=0,columnspan=2,sticky="news")
    top.rowconfigure(0,weight=1)
    top.columnconfigure(0,weight=1)

    left = Frame(root,bg="#93BFCF")
    left.grid(row=1,column=0,sticky="news")
    left.rowconfigure(0,weight=1)
    left.rowconfigure(1,weight=1)
    left.rowconfigure(2,weight=1)
    left.rowconfigure(3,weight=1)
    left.rowconfigure(4,weight=1)
    left.rowconfigure(5,weight=1)
    left.columnconfigure(0,weight=1)
    left.columnconfigure(1,weight=1)

    right = Frame(root,bg="#BDCDD6")
    right.grid(row=1,column=1,sticky="news")
    right.columnconfigure(0,weight=1)
    right.rowconfigure(0,weight=1)
    right.rowconfigure(1,weight=1)
    right.rowconfigure(2,weight=15)

    down = Frame(root,bg="#6096B4")
    down.grid(row=2,columnspan=2,sticky="news")
    down.rowconfigure(0,weight=1)
    down.columnconfigure(0,weight=2)
    down.columnconfigure(1,weight=2)
    down.columnconfigure(2,weight=2)
    down.columnconfigure(3,weight=1)

    return(top,left,right,down)

def topwidget(top) :
    title = Label(top,text="My cake shop by Patiphan",font=("Times New Roman",(25)),fg="#0A2647",bg="#6096B4")
    title.grid(row=0,column=0)

def leftwidget(left) :
    order1 = Label(left,image=img1,bg="#93BFCF")
    order1.grid(rowspan=2,column=0)
    order2 = Label(left,image=img2,bg="#93BFCF")
    order2.grid(rowspan=2,column=0)
    order3 = Label(left,image=img3,bg="#93BFCF")    
    order3.grid(rowspan=2,column=0)
    detail1 = Label(left,text="Chocolate Cake \n Price 160 baths",bg="#93BFCF")
    detail1.grid(row=0,column=1)
    detail2 = Label(left,text="Strawberry Cake \n Price 170 baths",bg="#93BFCF")
    detail2.grid(row=2,column=1)
    detail3 = Label(left,text="Donut Party \n Price 45 baths",bg="#93BFCF")
    detail3.grid(row=4,column=1)
    piece1 = Spinbox(left,from_=0,to=10,width=30,justify='center',textvariable=spy1,command=userclick)
    piece1.grid(row=1,column=1)
    piece2 = Spinbox(left,from_=0,to=10,width=30,justify='center',textvariable=spy2,command=userclick)
    piece2.grid(row=3,column=1)
    piece3 = Spinbox(left,from_=0,to=10,width=30,justify='center',textvariable=spy3,command=userclick)
    piece3.grid(row=5,column=1)

def rightwidget(right) :
    text = Label(right,text="Thank you for your shopping \n Total price is",font=("Times New Roman",(17)),fg="#02273f",bg="#BDCDD6")
    text.grid(row=1,column=0,pady=15)
    showtotal = Label(right,font=("Opens san",(17)),fg="#02273f",bg="#BDCDD6")
    showtotal.grid(row=2,column=0)
    return(showtotal)

def downwidget(down) :
    button = Button(down,text="Exit Program",width=25,height=3,command=quit)
    button.grid(row=0,column=3)

def userclick() :
    global total
    total = 0
    piece = [0,1,2,3,4,5,6,7,8,9,10]
    cake1 = [0,160,320,480,640,800,960,1120,1280,1440,1600]
    cake2 = [0,170,340,510,680,850,1020,1190,1360,1530,1700]
    cake3 = [0,45,90,135,180,225,270,315,360,405,450]
    for i in range(len(piece)) :
        if spy1.get() == i:
            total += cake1[i]
    for i in range(len(piece)) :
        if spy2.get() == i:
            total +=  cake2[i]
    for i in range(len(piece)) :
        if spy3.get() == i:
            total +=  cake3[i]
    showtotal['bg'] = "#BDCDD6"
    showtotal['fg'] = "#00337C"
    showtotal['text'] = str(total)+" Baths"

root = mainwindow()

img1 = PhotoImage(file="image\cake1.png").subsample(1,1)
img2 = PhotoImage(file="image\cake2.png").subsample(1,1)
img3 = PhotoImage(file="image\cake3.png").subsample(1,1)

spy1,spy2,spy3 = IntVar(),IntVar(),IntVar()
total = 0

(top,left,right,down) = layout(root)
topwidget(top)
leftwidget(left)
showtotal = rightwidget(right)
downwidget(down)
root.mainloop()