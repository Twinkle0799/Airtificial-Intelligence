from tkinter import *   #Importing modules
from PIL import ImageTk,Image
from tkinter import messagebox
def seatallocation():
    global seat
    seat = Toplevel(info)
    seat.title("Seat Allocation System")
    #seat.configure(bg = "yellow")
    #win.iconbitmap("ap.ico")
    global width
    global height
    width = seat.winfo_screenwidth()
    height = seat.winfo_screenheight()
    seat.geometry('750x450')
    canvas = Canvas(seat,width = width,height = height)
    image = ImageTk.PhotoImage(Image.open("BusBookingSystem.jpg"))
    canvas.create_image(0,0,anchor = "nw",image = image)
    canvas.place(relx = 0,rely = 0)
    #================================================Passenger Of Age above 60==============================================================================
    for i in range(len(namelist1)):
        namelist1[i] = namelist1[i].get()
        print(namelist1[i])
    Label(seat,text = "Name",bg = 'black',fg = 'white',width = 10,font =('comic sans ms','15'),anchor = "w").place(relx = 0.00,rely = 0.1)
    Label(seat,text = "Allocated Seat",bg = 'black',fg = 'white',width = 15,font =('comic sans ms','15'),anchor = "w").place(relx = 0.08,rely = 0.1)
    for i in range(len(namelist1)):
        i += 2
        Label(seat,text = namelist1[i-2],bg = 'green',fg = 'white',width = 15,font =('comic sans ms','15'),anchor = "w").place(relx = 0.00,rely = (i*0.1))
        Label(seat,text = "Seat No."+ str(i-1),bg = 'green',fg = 'white',width = 15,font =('comic sans ms','15'),anchor = "w").place(relx = 0.08,rely = (i*0.1))        
    #=======================================================Passenger of age 30 to 60===================================================================================
    for i in range(len(namelist2)):
        namelist2[i] = namelist2[i].get()
        print(namelist2[i])
    Label(seat,text = "Name",bg = 'black',fg = 'white',width = 8,font =('comic sans ms','15'),anchor = "w").place(relx = 0.20,rely = 0.1)
    Label(seat,text = "Allocated Seat",bg = 'black',fg = 'white',width = 15,font =('comic sans ms','15'),anchor = "w").place(relx = 0.25,rely = 0.1)
    for i in range(len(namelist2)):
        i += 2
        Label(seat,text = namelist2[i-2],bg = 'green',fg = 'white',width = 15,font =('comic sans ms','15'),anchor = "w").place(relx = 0.20,rely = (i*0.1))
        Label(seat,text = "Seat No."+ str(len(namelist1)+i-1),bg = 'green',fg = 'white',width = 15,font =('comic sans ms','15'),anchor = "w").place(relx = 0.26,rely = (i*0.1))        
    #======================================================Passenger OF Age Below30==================================================================
    Label(seat,text = "Name",bg = 'black',fg = 'white',width = 15,font =('comic sans ms','15'),anchor = "w").place(relx = 0.38,rely = 0.1)
    Label(seat,text = "Allocated Seat",bg = 'black',fg = 'white',width = 15,font =('comic sans ms','15'),anchor = "w").place(relx = 0.42,rely = 0.1)
    for i in range(len(namelist3)):
        namelist3[i] = namelist3[i].get()
        print(namelist3[i])
    for i in range(len(namelist3)):
        i += 2
        Label(seat,text = namelist3[i-2],bg = 'green',fg = 'white',width = 15,font =('comic sans ms','15'),anchor = "w").place(relx = 0.38,rely = (i*0.1))
        Label(seat,text = "Seat No."+ str(len(namelist2)+len(namelist1)+i-1),bg = 'green',fg = 'white',width = 15,font =('comic sans ms','15'),anchor = "w").place(relx = 0.42,rely = (i*0.1))        
    Button(seat,text = " EXIT ",command = lambda:destroy(),font =('comic sans ms','20')).place(relx = 0.25,rely = 0.4)

    #=====================================================Page Destroy==============================================================
    def destroy():
        seat.destroy()
        info.destroy()
        win.destroy()
    seat.mainloop()
def landingpage():
    global win
    win = Tk()
    win.title("Seat Allocation System")
   
    #win.iconbitmap("ap.ico")
    global width
    global height
    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()
  
    canvas = Canvas(win,width = width,height = height)

    label = Label(win,text = "Enter number of passengers:",font =('comic sans ms','19'),bg = "black",fg = "white",anchor = "w",width = 30)
    label.place(relx = '0.2',rely = '0.2')
    label = Label(win,text = "Worry Less, Travel More",font =('Times new roman','35'),fg = "black",anchor = "w",width = 19)
    label.place(relx = '0.38',rely = '0.8')
    global entry
    passengers = IntVar()
    passengers.set(0)
    entry = Entry(win,text = passengers,font =('comic sans ms','20'),width = 5)
    entry.place(relx = '0.47',rely = '0.2')
    button = Button(win,text = "OK",bg = 'black',fg = 'white',font =('comic sans ms','25'),command = lambda:get_count())
    button.place(relx = '0.45',rely = '0.29')
    def get_count():
        if(int(entry.get())<=0 or int(entry.get())>18):
            messagebox.showinfo("Warning","Invalid number of passengers.")
        else:
            getlist = [int(0) for i in range(3)]
            print(getlist)
            for _ in range(3):
                getlist[_] = IntVar()
                getlist[_].set(0)
                l = ['greater than 60 :','Between 30 and 60 :','Below 30 :']
                label1 = Label(win,text = "Enter number of passengers Of age "+l[_],font =('comic sans ms','15'),bg = "green",fg = "white",anchor = "w",width = 60)
                label1.place(relx = '0.20',rely = (_*0.1)+0.4)
                entry1 = Entry(win,text = getlist[_],font =('comic sans ms','15'),width = 5)
                entry1.place(relx = '0.71',rely = (_*0.1)+0.4)
                Button(win,text = " OK ",command = lambda:get_data(),font =('comic sans ms','20')).place(relx = 0.45,rely = 0.7)
            
            def get_data():
               
                
                for _ in range(3):
                    getlist[_] = int(getlist[_].get())
                global namelist1,namelist2,namelist3
                namelist1 = [0 for i in range(int(getlist[0]))]
                namelist2 = [0 for i in range(int(getlist[1]))]
                namelist3 = [0 for i in range(int(getlist[2]))]                
                if(sum(getlist) != int(passengers.get())):
                    messagebox.showinfo("Warning","Invalid number of passengers.")
                else:
                    global info
                    info = Toplevel(win)
                    info.title("Name_Page")
                    info.configure(bg = "yellow")
                    #win.iconbitmap("ap.ico")
                    
                    global width
                    global height
                    width = info.winfo_screenwidth()
                    height = info.winfo_screenheight()
                    info.geometry('730x405')
                    canvas = Canvas(info,width = width,height = height)
                    image = ImageTk.PhotoImage(Image.open("BusBookingSystem.jpg"))
                    canvas.create_image(0,0,anchor = "nw",image = image)
                    canvas.place(relx = 0,rely = 0)
                    #global f = 0
            
                    Label(info,text = "Enter names of passengers of age above 60",font =('comic sans ms','20'),bg = "blue",fg = "white",anchor = "w",width = 50).place(relx = 0.01,rely = 0.01)
                    for i in range(getlist[0]):
                        Name_label = Label(info,text = "Enter name of passenger "+str(i+1),font =('comic sans ms','15'),bg = "green",fg = "white",anchor = "w",width = 50)
                        Name_label.place(relx = '0.05',rely = ((i*0.08)+0.10))
                        namelist1[i] = StringVar()
                        namelist1[i].set("Enter name here")
                        nameentry = Entry(info,text = namelist1[i],font =('comic sans ms','12'),width = 15)
                        nameentry.place(relx = '0.5',rely = ((i*0.08)+0.10))
                        f = ((i*0.05)+0.06)
                    if(getlist[1] == 0 and getlist[2] != 0):
                        b = Button(info,text = "OK",font =('comic sans ms','12'),command = lambda:BelowThirty())
                        b.place(relx = 0.16,rely = f + 0.1)
                    elif(getlist[1] == 0 and getlist[2] == 0):
                        b = Button(info,text = "OK",font =('comic sans ms','12'),command = lambda:seatallocation())
                        b.place(relx = 0.16,rely = f + 0.1)
                    else:
                        b = Button(info,text = "OK",font =('comic sans ms','12'),command = lambda:ThirtyTOSixty())
                        b.place(relx = 0.16,rely = f + 0.1)
                    
                    def ThirtyTOSixty():
                        l1 = Label(info,text = "Enter names of passengers of age 30 to 60:",font =('comic sans ms','20'),bg = "blue",fg = "white",anchor = "w",width = 50)
                        l1.place(relx = 0.01,rely = 0.17)
                        for i in range(getlist[1]):
                            Name_label = Label(info,text = "Enter name of passenger "+str(i+1),font =('comic sans ms','15'),bg = "green",fg = "white",anchor = "w",width = 50)
                            Name_label.place(relx = '0.05',rely = ((i*0.10)+0.30))
                            namelist2[i] = StringVar()
                            namelist2[i].set("Enter name here")
                            nameentry = Entry(info,text = namelist2[i],font =('comic sans ms','12'),width = 15)
                            nameentry.place(relx = '0.5',rely = ((i*0.10)+0.30)) 
                            f = ((i*0.05)+0.06)
                        print("getlist2 is:",getlist[2])
                        print(type(getlist[2]))
                        if(getlist[2] == 0):
                            b = Button(info,text = "OK",font =('comic sans ms','12'),command = lambda:seatallocation())
                            b.place(relx = 0.46,rely = f + 0.3)
                        else:
                            b = Button(info,text = "OK",font =('comic sans ms','12'),command = lambda:BelowThirty())
                            b.place(relx = 0.46,rely = f + 0.3)
                    def BelowThirty():
                        
                        Label(info,text = "Enter names of passengers of age below 30",font =('comic sans ms','20'),bg = "blue",fg = "white",anchor = "w",width = 50).place(relx = 0.01,rely = 0.30)
                        for i in range(getlist[2]):
                            Name_label = Label(info,text = "Enter name of passenger "+str(i+1),font =('comic sans ms','12'),bg = "green",fg = "white",anchor = "w",width = 50)
                            Name_label.place(relx = '0.05',rely = ((i*0.15)+0.50))
                            namelist3[i] = StringVar()
                            namelist3[i].set("Enter name here")
                            nameentry = Entry(info,text = namelist3[i],font =('comic sans ms','12'),width = 15)
                            nameentry.place(relx = '0.5',rely = ((i*0.05)+0.50))
                        Button(info,text = "OK",font =('comic sans ms','15'),command = lambda:seatallocation()).place(relx = 0.4,rely = f+0.5)  
                            
                    info.mainloop()
                
    win.mainloop()
landingpage()
