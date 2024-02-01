from tkinter import Button,Label,Tk
from PIL import Image, ImageTk
from random import choice
class play():
    def __init__(self):
        #points
        self.ptsuser=0
        self.ptsmachine=0
        self.txtmachinesel=["ROCK","PAPER","SCISSOR"]
        self.on=True
        #main configuration
        self.window=Tk()
        self.window.resizable(0,0)
        self.window.title("My gift to you ")
        self.window.geometry("620x540")
        self.window.config(bg="RoyalBlue2")
        self.window.iconbitmap("images\icono.ico")
        #load images
        self.vectorimages=["images\piedra.jpg","images\papel.jpg","images\Tijera.jpg"]
        self.img1 = Image.open(self.vectorimages[0])
        self.img2 = Image.open(self.vectorimages[1])
        self.img3 = Image.open(self.vectorimages[2])

        self.imgrock = ImageTk.PhotoImage(self.img1)
        self.imgpaper= ImageTk.PhotoImage(self.img2)
        self.imgscissor = ImageTk.PhotoImage(self.img3)

        #buttons with images
        self.btnrock=Button(self.window,image=self.imgrock,border=0,borderwidth=0,command=lambda: self.ingame(0)).place(x=50,y=350)
        self.btnpaer=Button(self.window,image=self.imgpaper,border=0,borderwidth=0,command=lambda: self.ingame(1)).place(x=240,y=350)
        self.btnscissor=Button(self.window,image=self.imgscissor,border=0,borderwidth=0,command=lambda: self.ingame(2)).place(x=430,y=350)
        Label(self.window,bg="RoyalBlue2",fg="cyan2",text="ROCK",font="arial 14 bold").place(x=85,y=315)
        Label(self.window,bg="RoyalBlue2",fg="SkyBlue1",text="PAPER",font="arial 14 bold").place(x=270,y=315)
        Label(self.window,bg="RoyalBlue2",fg="SeaGreen3",text="SCISSOR",font="arial 14 bold").place(x=460,y=315)
        #label points
        self.pointsuser=Label(self.window,text="YOU: "+str(self.ptsuser),font="arial 15 bold",fg="#ffffff",bg="Royal Blue2")
        self.pointsuser.place(x=30,y=20)
        self.pointsmachine=Label(self.window,text="MACHINE: "+str(self.ptsmachine),font="arial 15 bold",fg="#ffffff",bg="Royal Blue2")
        self.pointsmachine.place(x=30,y=50)
        #image and label machine selecction
        self.imgselmachine = Label(self.window,borderwidth=0)
        self.imgselmachine.place(x=240,y=100)
        
        self.lbselma=Label(self.window,bg="RoyalBlue2",fg="SeaGreen3",text="",font="arial 14 bold")
        self.lbselma.place(x=250,y=70)
        self.window.mainloop()

    def ingame(self,number):
        if self.on:
            selmachine=choice([0,1,2])
            imgsel=ImageTk.PhotoImage(Image.open(self.vectorimages[selmachine]))
            self.imgselmachine.config(image=imgsel)
            self.imgselmachine.image=imgsel
            self.lbselma['text']=self.txtmachinesel[selmachine]
            
            if number==selmachine:
                print("Nobody win")
            elif (number==0 and selmachine==2) or (number==1 and selmachine==0) or (number==2 and selmachine==1):
                self.ptsuser+=1
            else:
                self.ptsmachine+=1

            if self.ptsuser == 5 or self.ptsmachine == 5:
                self.on=False

            self.pointsuser['text']="YOU: "+str(self.ptsuser)
            self.pointsmachine['text']="MACHINE: "+str(self.ptsmachine)

        else:
            self.txtwinner=""
            if self.ptsuser == 5:
                self.txtwinner="YOU"
            else:
                self.txtwinner="MACHINE"
            self.Msg=Tk()
            self.Msg.resizable(0,0)
            self.Msg.title("Menu")
            self.Msg.iconbitmap("images\icono.ico")
            self.Msg.geometry("200x170")
            self.Msg.config(bg="SeaGreen")
            self.winner=Label(self.Msg,bg="aquamarine2",fg="red4",font="arial 12 bold",text="WIN "+self.txtwinner)
            self.winner.pack(pady=10)
            self.btreboot=Button(self.Msg,text="RESTART GAME",bg="PaleGreen1",font="arial 13 bold",fg="navy",border=0,borderwidth=0,command=self.reboot).pack(pady=10)
            self.btexit=Button(self.Msg,text="EXIT",bg="PaleGreen1",font="arial 13 bold",fg="navy",border=0,borderwidth=0,width=13,command=self.exit).pack(pady=10)
            self.Msg.mainloop()

    def reboot(self):
        self.on=True
        self.ptsmachine=0
        self.ptsuser=0
        self.pointsuser['text']="YOU: "+str(self.ptsuser)
        self.pointsmachine['text']="MACHINE: "+str(self.ptsmachine)
        self.Msg.destroy()

    def exit(self):
        self.Msg.destroy()
        self.window.destroy()

if __name__ == "__main__":
    play()