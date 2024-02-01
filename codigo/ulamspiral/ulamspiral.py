import pygame as pg
from tkinter import Tk,messagebox,Button,Label,Entry
class ulamspiral():
    def __init__(self,finaln):
        self.number=1
        self.finaln=finaln
        self.x=347
        self.y=341
        self.xr=5
        self.xl=-5
        self.yd=5
        self.yu=-5

        self.orientation=0
        self.positiontochange1=[347+5,341]
        self.positiontochange2=[347+5,341-5]
        self.positiontochange3=[347-5,341-5]
        self.positiontochange4=[347-5,341+5]
    
    def mostrar(self,fondo):
        if self.isprime(self.number):
            pg.draw.rect(fondo,(255,255,255),[self.x,self.y,5,5])

        if self.orientation==0:
            self.x+=self.xr
            if self.positiontochange1 == [self.x,self.y]:
                self.positiontochange1[1]+=5
                self.positiontochange1[0]+=5
                self.orientation=1

        elif self.orientation==1:
            self.y+=self.yu
            if self.positiontochange2 == [self.x,self.y]:
                self.orientation=2
                self.positiontochange2[0]+=5
                self.positiontochange2[1]+=-5
                
        elif self.orientation==2:
            self.x+=self.xl
            if self.positiontochange3 == [self.x,self.y]:
                self.positiontochange3[1]+=-5
                self.positiontochange3[0]+=-5
                self.orientation=3

        elif self.orientation==3:
            self.y+=self.yd
            if self.positiontochange4 == [self.x,self.y]:
                self.positiontochange4[0]+=-5
                self.positiontochange4[1]+=5
                self.orientation=0        
        
        self.number+=1
        pg.display.flip()
        
        if self.number==self.finaln:
            return False
        else:
            return True
        
    def isprime(self,number):
        self.prime=0
        if number > 1:
            for i in range(1,number+1):
                if number%i == 0:
                    self.prime += 1
        return self.prime==2
    
    def eventos(self):
        for e in pg.event.get():
            if e.type==pg.QUIT:
                return False
        return True
class main():
    def __init__(self):
        self.window=Tk()
        self.window.resizable(0,0)
        self.window.title("ULAM SPIRAL")
        self.window.geometry("290x430")
        self.window.config(bg="dark slate gray")
        self.title=Label(self.window,text="ULAM\nSPIRAL",bg="dark slate gray",fg="cornflower blue",font="arial 22 bold").pack(pady=30)
        self.lbnumbersprimes=Label(self.window,text="2 3 5 7 11 13 17 19 23 \n29 31 37 41 43 47 53 \n59 61 67 71 73\n ........",fg="yellow4",bg="dark slate gray",font="arial 11 bold").pack(pady=40)
        self.lbentry=Label(self.window,text="Please insert a number",bg="dark slate gray",fg="light sea green",font="arial 11 bold").pack()
        self.numberinput=Entry(self.window,width=20,font="arial 13 bold",border=0,borderwidth=0)
        self.numberinput.pack()
        self.btn=Button(self.window,text="Show",width=17,font="arial 12 bold",border=0,borderwidth=0,bg="Slategray2",fg="#000000",command= lambda: self.drawspiral(self.numberinput.get())).pack(pady=30)
        self.window.mainloop()

    def drawspiral(self,number):
        try:
            self.number=int(number)
            if 2 <= self.number <= 18000:
                pg.init()
                self.window=pg.display.set_mode((700,700))
                self.clock=pg.time.Clock()
                self.run=True
                self.rundraw=True
                self.draw=ulamspiral(self.number+1)
                while self.run:
                    self.run=self.draw.eventos()
                    if self.rundraw:
                        self.rundraw=self.draw.mostrar(self.window)
                    self.clock.tick(60)
                pg.quit()
            else:
                messagebox.showinfo("Limit","The range to input are between 2 - 18000")
        except Exception as e:
            print(e)
            messagebox.showwarning("Error","Please insert a integer number.")

if __name__ == "__main__":
    main()