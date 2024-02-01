from tkinter import messagebox,ttk,Label,Button,Menu,Tk,Entry
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from abc import ABC,abstractclassmethod

#clase abstracta plantilla comun de todas las interfaces
class functions(ABC):
    @abstractclassmethod
    def destruir(self):
        pass

    @abstractclassmethod
    def volver(self):
        pass

    @abstractclassmethod
    def limpiar(self):
        pass

    @abstractclassmethod
    def calcular(self):
        pass

#clase calculo de determinantes
class determinate():
    def det2x2(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        return "{:.2f}".format((self.a*self.d)-(self.b*self.c))

    def det3x3(self,a,b,c,d,e,f,g,h,i):
        self.v11=a
        self.v21=b
        self.v31=c
        self.v12=d
        self.v22=e
        self.v32=f
        self.v13=g
        self.v23=h
        self.v33=i

        return "{:.2f}".format((self.v11*self.v22*self.v33+self.v21*self.v32*self.v13+self.v31*self.v12*self.v23-self.v13*self.v22*self.v31-self.v23*self.v32*self.v11-self.v33*self.v12*self.v21))

    def det4x4(self,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
        a00=a
        a10=b
        a20=c
        a30=d
        a01=e
        a11=f
        a21=g
        a31=h
        a02=i
        a12=j
        a22=k
        a32=l
        a03=m
        a13=n
        a23=o
        a33=p

        self.respuesta = a00*((a11*a22*a33+a21*a32*a13+a31*a12*a23)-(a13*a22*a31+a23*a32*a11+a33*a12*a21))-a01*((a10*a22*a33+a20*a32*a13+a30*a12*a23)-(a13*a22*a30+a23*a32*a10+a33*a12*a20))+a02*((a10*a21*a33+a20*a31*a13+a30*a11*a23)-(a13*a21*a30+a23*a31*a10+a33*a11*a20))-a03*((a10*a21*a32+a20*a31*a12+a30*a11*a22)-(a12*a21*a30+a22*a31*a10+a32*a11*a20))
        return "{:.2f}".format(self.respuesta)

#clase calculo de matriz inversa
class inversa():
    def iv2x2(self,n00,n01,n10,n11):
        self.matriz=[[0,0,1,0],[0,0,0,1]]
        self.matriz[0][0]=float(n00)
        self.matriz[1][0]=float(n10)
        self.matriz[0][1]=float(n01)
        self.matriz[1][1]=float(n11)
        #calculo de valores
        vf1=self.matriz[0][0]
        vf2=self.matriz[1][0]
        for i in range(4):
            self.matriz[1][i]=self.matriz[0][i]*vf2-self.matriz[1][i]*vf1
        vf1=self.matriz[0][1]
        vf2=self.matriz[1][1]
        for i in range(4):
            self.matriz[0][i]=self.matriz[0][i]*vf2-self.matriz[1][i]*vf1
        vf1=self.matriz[0][0]
        vf2=self.matriz[1][1]
        for i in range(4):
            self.matriz[0][i]=self.matriz[0][i]/vf1
            self.matriz[1][i]=self.matriz[1][i]/vf2

        valor1="{:.2f}".format(self.matriz[0][2])
        valor2="{:.2f}".format(self.matriz[1][2])
        valor3="{:.2f}".format(self.matriz[0][3])
        valor4="{:.2f}".format(self.matriz[1][3])
        self.v1="[ "+valor1+"  "+valor3+" ]"
        self.v2="[ "+valor2+"  "+valor4+" ]"
        return self.v1, self.v2

    def iv3x3(self,a,b,c,d,e,f,g,h,i):
        self.matriz=[[0,0,0,1,0,0],
                     [0,0,0,0,1,0],
                    [0,0,0,0,0,1]]
        
        self.matriz[0][0]=a
        self.matriz[1][0]=b
        self.matriz[2][0]=c

        self.matriz[0][1]=d
        self.matriz[1][1]=e
        self.matriz[2][1]=f
            
        self.matriz[0][2]=g
        self.matriz[1][2]=h
        self.matriz[2][2]=i

        #calculo de valores
        vf1=self.matriz[0][0]
        vf2=self.matriz[1][0]
        vf3=self.matriz[2][0]
        for i in range(6):
            self.matriz[1][i]=self.matriz[1][i]*vf1-self.matriz[0][i]*vf2
            self.matriz[2][i]=self.matriz[2][i]*vf1-self.matriz[0][i]*vf3
        vf2=self.matriz[1][1]
        vf3=self.matriz[2][1]
        for i in range(6):
            self.matriz[2][i]=self.matriz[2][i]*vf2-self.matriz[1][i]*vf3
        vf1=self.matriz[0][2]
        vf2=self.matriz[1][2]
        vf3=self.matriz[2][2]
        for i in range(6):
            self.matriz[1][i]=self.matriz[1][i]*vf3-self.matriz[2][i]*vf2
            self.matriz[0][i]=self.matriz[0][i]*vf3-self.matriz[2][i]*vf1
        vf1=self.matriz[0][1]
        vf2=self.matriz[1][1]
        for i in range(6):
            self.matriz[0][i]=self.matriz[0][i]*vf2-self.matriz[1][i]*vf1
        vf1=self.matriz[0][0]
        vf2=self.matriz[1][1]
        vf3=self.matriz[2][2]
        for i in range(6):
            self.matriz[0][i]=self.matriz[0][i]/vf1
            self.matriz[1][i]=self.matriz[1][i]/vf2
            self.matriz[2][i]=self.matriz[2][i]/vf3

        valor1="{:.2f}".format(self.matriz[0][3])
        valor2="{:.2f}".format(self.matriz[1][3])
        valor3="{:.2f}".format(self.matriz[2][3])

        valor11="{:.2f}".format(self.matriz[0][4])
        valor22="{:.2f}".format(self.matriz[1][4])
        valor33="{:.2f}".format(self.matriz[2][4])

        valor111="{:.2f}".format(self.matriz[0][5])
        valor222="{:.2f}".format(self.matriz[1][5])
        valor333="{:.2f}".format(self.matriz[2][5])

        self.v1="[ "+valor1+"  "+valor11+"  "+valor111+" ]"
        self.v2="[ "+valor2+"  "+valor22+"  "+valor222+" ]"
        self.v3="[ "+valor3+"  "+valor33+"  "+valor333+" ]"

        return self.v1,self.v2,self.v3
        
    def iv4x4(self,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
        self.matriz=[[0,0,0,0,1,0,0,0],
                     [0,0,0,0,0,1,0,0],
                     [0,0,0,0,0,0,1,0],
                     [0,0,0,0,0,0,0,1]]
        
        self.matriz[0][0]=a
        self.matriz[1][0]=b
        self.matriz[2][0]=c
        self.matriz[3][0]=d
        self.matriz[0][1]=e
        self.matriz[1][1]=f
        self.matriz[2][1]=g
        self.matriz[3][1]=h
        self.matriz[0][2]=i
        self.matriz[1][2]=j
        self.matriz[2][2]=k
        self.matriz[3][2]=l
        self.matriz[0][3]=m
        self.matriz[1][3]=n
        self.matriz[2][3]=o
        self.matriz[3][3]=p

        #ceros abajo
        vf1=self.matriz[0][0]
        vf2=self.matriz[1][0]
        vf3=self.matriz[2][0]
        vf4=self.matriz[3][0]
        for i in range(5):
            self.matriz[1][i]=self.matriz[1][i]*vf1-self.matriz[0][i]*vf2
            self.matriz[2][i]=self.matriz[2][i]*vf1-self.matriz[0][i]*vf3
            self.matriz[3][i]=self.matriz[3][i]*vf1-self.matriz[0][i]*vf4
        vf2=self.matriz[1][1]
        vf3=self.matriz[2][1]
        vf4=self.matriz[3][1]
        for i in range(5):
            self.matriz[2][i]=self.matriz[2][i]*vf2-self.matriz[1][i]*vf3
            self.matriz[3][i]=self.matriz[3][i]*vf2-self.matriz[1][i]*vf4
        vf3=self.matriz[2][2]
        vf4=self.matriz[3][2]
        for i in range(5):
            self.matriz[3][i]=self.matriz[3][i]*vf3-self.matriz[2][i]*vf4
        #ceros arriba
        vf1=self.matriz[0][3]
        vf2=self.matriz[1][3]
        vf3=self.matriz[2][3]
        vf4=self.matriz[3][3]
        for i in range(5):
            self.matriz[0][i]=self.matriz[0][i]*vf4-self.matriz[3][i]*vf1
            self.matriz[1][i]=self.matriz[1][i]*vf4-self.matriz[3][i]*vf2
            self.matriz[2][i]=self.matriz[2][i]*vf4-self.matriz[3][i]*vf3
        vf1=self.matriz[0][2]
        vf2=self.matriz[1][2]
        vf3=self.matriz[2][2]
        for i in range(5):
            self.matriz[0][i]=self.matriz[0][i]*vf3-self.matriz[2][i]*vf1
            self.matriz[1][i]=self.matriz[1][i]*vf3-self.matriz[2][i]*vf2
        vf1=self.matriz[0][1]
        vf2=self.matriz[1][1]
        for i in range(5):
            self.matriz[0][i]=self.matriz[0][i]*vf2-self.matriz[1][i]*vf1
        vf1=self.matriz[0][0]
        vf2=self.matriz[1][1]
        vf3=self.matriz[2][2]
        vf4=self.matriz[3][3]
        for i in range(5):
            self.matriz[0][i]=self.matriz[0][i]/vf1
            self.matriz[1][i]=self.matriz[1][i]/vf2
            self.matriz[2][i]=self.matriz[2][i]/vf3
            self.matriz[3][i]=self.matriz[3][i]/vf4
                
        valor1="{:.2f}".format(self.matriz[0][4])
        valor2="{:.2f}".format(self.matriz[1][4])
        valor3="{:.2f}".format(self.matriz[2][4])
        valor4="{:.2f}".format(self.matriz[3][4])

        valor11="{:.2f}".format(self.matriz[0][5])
        valor22="{:.2f}".format(self.matriz[1][5])
        valor33="{:.2f}".format(self.matriz[2][5])
        valor44="{:.2f}".format(self.matriz[3][5])

        valor111="{:.2f}".format(self.matriz[0][6])
        valor222="{:.2f}".format(self.matriz[1][6])
        valor333="{:.2f}".format(self.matriz[2][6])
        valor444="{:.2f}".format(self.matriz[3][6])

        valor1111="{:.2f}".format(self.matriz[0][7])
        valor2222="{:.2f}".format(self.matriz[1][7])
        valor3333="{:.2f}".format(self.matriz[2][7])
        valor4444="{:.2f}".format(self.matriz[3][7])

        self.v1="[ "+valor1+"  "+valor11+"  "+valor111+"  "+valor1111+" ]"
        self.v2="[ "+valor2+"  "+valor22+"  "+valor222+"  "+valor2222+" ]"
        self.v3="[ "+valor3+"  "+valor33+"  "+valor333+"  "+valor3333+" ]"
        self.v4="[ "+valor4+"  "+valor44+"  "+valor444+"  "+valor4444+" ]"

        return self.v1,self.v2,self.v3,self.v4

#clase de calculo de matrices gauss jordan
class matrices():
    def mt2x2(self,a,b,c,d,e,f):
        self.matriz=[[0,0,0],[0,0,0]]
        self.matriz[0][0]=a
        self.matriz[1][0]=b
        self.matriz[0][1]=c
        self.matriz[1][1]=d
        self.matriz[0][2]=e
        self.matriz[1][2]=f

        #calculo de valores
        vf1=self.matriz[0][0]
        vf2=self.matriz[1][0]
        for i in range(3):
            self.matriz[1][i]=self.matriz[0][i]*vf2-self.matriz[1][i]*vf1
        vf1=self.matriz[0][1]
        vf2=self.matriz[1][1]
        for i in range(3):
            self.matriz[0][i]=self.matriz[0][i]*vf2-self.matriz[1][i]*vf1
        vf1=self.matriz[0][0]
        vf2=self.matriz[1][1]
        for i in range(3):
            self.matriz[0][i]=self.matriz[0][i]/vf1
            self.matriz[1][i]=self.matriz[1][i]/vf2
        valor1="{:.2f}".format(self.matriz[0][2])
        valor2="{:.2f}".format(self.matriz[1][2])

        return valor1,valor2

    def mt3x3(self,a,b,c,d,e,f,g,h,i,j,k,l):
        self.matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]

        self.matriz[0][0]=a
        self.matriz[1][0]=b
        self.matriz[2][0]=c
        self.matriz[0][1]=d
        self.matriz[1][1]=e
        self.matriz[2][1]=f   
        self.matriz[0][2]=g
        self.matriz[1][2]=h
        self.matriz[2][2]=i
        self.matriz[0][3]=j
        self.matriz[1][3]=k
        self.matriz[2][3]=l

        #calculo de valores
        vf1=self.matriz[0][0]
        vf2=self.matriz[1][0]
        vf3=self.matriz[2][0]
        for i in range(4):
            self.matriz[1][i]=self.matriz[1][i]*vf1-self.matriz[0][i]*vf2
            self.matriz[2][i]=self.matriz[2][i]*vf1-self.matriz[0][i]*vf3
        vf2=self.matriz[1][1]
        vf3=self.matriz[2][1]
        for i in range(4):
            self.matriz[2][i]=self.matriz[2][i]*vf2-self.matriz[1][i]*vf3
        vf1=self.matriz[0][2]
        vf2=self.matriz[1][2]
        vf3=self.matriz[2][2]
        for i in range(4):
            self.matriz[1][i]=self.matriz[1][i]*vf3-self.matriz[2][i]*vf2
            self.matriz[0][i]=self.matriz[0][i]*vf3-self.matriz[2][i]*vf1
        vf1=self.matriz[0][1]
        vf2=self.matriz[1][1]
        for i in range(4):
            self.matriz[0][i]=self.matriz[0][i]*vf2-self.matriz[1][i]*vf1
        vf1=self.matriz[0][0]
        vf2=self.matriz[1][1]
        vf3=self.matriz[2][2]
        for i in range(4):
            self.matriz[0][i]=self.matriz[0][i]/vf1
            self.matriz[1][i]=self.matriz[1][i]/vf2
            self.matriz[2][i]=self.matriz[2][i]/vf3

        valor1="{:.2f}".format(self.matriz[0][3])
        valor2="{:.2f}".format(self.matriz[1][3])
        valor3="{:.2f}".format(self.matriz[2][3])
        
        return valor1,valor2,valor3

    def mt4x4(self,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t):
        self.matriz=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 
        self.matriz[0][0]=a
        self.matriz[1][0]=b
        self.matriz[2][0]=c
        self.matriz[3][0]=d
        self.matriz[0][1]=e
        self.matriz[1][1]=f
        self.matriz[2][1]=g
        self.matriz[3][1]=h
        self.matriz[0][2]=i
        self.matriz[1][2]=j
        self.matriz[2][2]=k
        self.matriz[3][2]=l
        self.matriz[0][3]=m
        self.matriz[1][3]=n
        self.matriz[2][3]=o
        self.matriz[3][3]=p
        self.matriz[0][4]=q
        self.matriz[1][4]=r
        self.matriz[2][4]=s
        self.matriz[3][4]=t

        #ceros abajo
        vf1=self.matriz[0][0]
        vf2=self.matriz[1][0]
        vf3=self.matriz[2][0]
        vf4=self.matriz[3][0]
        for i in range(5):
            self.matriz[1][i]=self.matriz[1][i]*vf1-self.matriz[0][i]*vf2
            self.matriz[2][i]=self.matriz[2][i]*vf1-self.matriz[0][i]*vf3
            self.matriz[3][i]=self.matriz[3][i]*vf1-self.matriz[0][i]*vf4
        vf2=self.matriz[1][1]
        vf3=self.matriz[2][1]
        vf4=self.matriz[3][1]
        for i in range(5):
            self.matriz[2][i]=self.matriz[2][i]*vf2-self.matriz[1][i]*vf3
            self.matriz[3][i]=self.matriz[3][i]*vf2-self.matriz[1][i]*vf4
        vf3=self.matriz[2][2]
        vf4=self.matriz[3][2]
        for i in range(5):
            self.matriz[3][i]=self.matriz[3][i]*vf3-self.matriz[2][i]*vf4
        #ceros arriba
        vf1=self.matriz[0][3]
        vf2=self.matriz[1][3]
        vf3=self.matriz[2][3]
        vf4=self.matriz[3][3]
        for i in range(5):
            self.matriz[0][i]=self.matriz[0][i]*vf4-self.matriz[3][i]*vf1
            self.matriz[1][i]=self.matriz[1][i]*vf4-self.matriz[3][i]*vf2
            self.matriz[2][i]=self.matriz[2][i]*vf4-self.matriz[3][i]*vf3
        vf1=self.matriz[0][2]
        vf2=self.matriz[1][2]
        vf3=self.matriz[2][2]
        for i in range(5):
            self.matriz[0][i]=self.matriz[0][i]*vf3-self.matriz[2][i]*vf1
            self.matriz[1][i]=self.matriz[1][i]*vf3-self.matriz[2][i]*vf2
        vf1=self.matriz[0][1]
        vf2=self.matriz[1][1]
        for i in range(5):
            self.matriz[0][i]=self.matriz[0][i]*vf2-self.matriz[1][i]*vf1
        vf1=self.matriz[0][0]
        vf2=self.matriz[1][1]
        vf3=self.matriz[2][2]
        vf4=self.matriz[3][3]
        for i in range(5):
            self.matriz[0][i]=self.matriz[0][i]/vf1
            self.matriz[1][i]=self.matriz[1][i]/vf2
            self.matriz[2][i]=self.matriz[2][i]/vf3
            self.matriz[3][i]=self.matriz[3][i]/vf4

        valor1="{:.2f}".format(self.matriz[0][4])
        valor2="{:.2f}".format(self.matriz[1][4])
        valor3="{:.2f}".format(self.matriz[2][4])
        valor4="{:.2f}".format(self.matriz[3][4])

        return valor1,valor2,valor3,valor4

class main():
    def __init__(self):
        #ventana
        self.mainwindow=Tk()
        self.mainwindow.resizable(0,0)
        self.mainwindow.config(bg="gray26")
        self.mainwindow.geometry("500x500")
        self.mainwindow.title("Menu principal")
        self.mainwindow.iconbitmap("images/numero.ico")
        #etiquetas titulo, tamaño, tipo, x,y,z,i
        self.titulo_menu=Label(self.mainwindow,text="Matrices",font="Arial 28 bold",bg="gray",fg="white").place(x=180,y=40)
        self.menu_size=Label(self.mainwindow,text="Seleccione la dimension",font="Arial 12 bold",bg="DarkSeaGreen1",fg="gray18").place(x=30,y=260)
        self.menu_type=Label(self.mainwindow,text="Seleccione algun tipo",font="Arial 12 bold",bg="DarkSeaGreen1",fg="gray18").place(x=280,y=260)
        self.XLB=Label(self.mainwindow,text="3X\n X\n4X",font="Arial 12 bold",bg="gray26",fg="turquoise4").place(x=180,y=130)
        self.YLB=Label(self.mainwindow,text=" +  3Y\n -  7Y\n +  4Y",font="Arial 12 bold",bg="gray26",fg="DarkOrange4").place(x=205,y=130)
        self.ZLB=Label(self.mainwindow,text=" -   Z\n +  2Z\n +  9Z",font="Arial 12 bold",bg="gray26",fg="DarkOliveGreen4").place(x=250,y=130)
        self.RLB=Label(self.mainwindow,text=" =  12\n= -2\n=  0",font="Arial 12 bold",bg="gray26",fg="gold4").place(x=300,y=130)
        
        self.style = ttk.Style()
        self.style.map("TCombobox", fieldbackground=[("readonly", "white")])
        #seleccion tamaño
        self.cbmsizem = ttk.Combobox(self.mainwindow, width=19, font="Arial 12 bold", foreground="olive drab", state="readonly")
        self.cbmsizem.place(x=30, y=300)
        self.optioncmbsize = ("Matriz 2X2", "Matriz 3X3", "Matriz 4X4")
        self.cbmsizem["values"] = self.optioncmbsize
        self.cbmsizem.set(self.optioncmbsize[0])

        self.cbmsizem.bind("<FocusIn>", self.quitar_resaltado)

        #seleccion tipo
        self.cbmstype=ttk.Combobox(self.mainwindow,width=16,font="Arial 12 bold",foreground="navy",state="readonly")
        self.cbmstype.place(x=280,y=300)
        self.optioncmbtype=("Solucion Del Sistema","Determinante","Matriz Inversa")
        self.cbmstype["values"]=self.optioncmbtype
        self.cbmstype.set(self.optioncmbtype[0])

        self.cbmstype.bind("<FocusIn>", self.quitar_resaltado)

        #menu barra
        self.menubar=Menu(self.mainwindow)
        self.mainwindow.config(menu=self.menubar)
        file=Menu(self.menubar,tearoff=0)
        file.add_command(label='Acerca de',command=self.about)
        file.add_separator()
        file.add_command(label='Cerrar',command=self.destruir)
        self.menubar.add_cascade(label='Opciones',menu=file)
        #boton para ingresar
        self.ingresar=Button(self.mainwindow,fg="light sea green",bg="PaleGreen1",text="INGRESAR",font="Arial 13 bold",command=self.ingresar)
        self.ingresar.place(x=200,y=400)

        # Image
        imagen = Image.open("images/ca1.jpg")
        imagen_tk = ImageTk.PhotoImage(imagen)
        self.label = Label(self.mainwindow, image=imagen_tk)
        self.label.image = imagen_tk
        self.label.place(x=60, y=110)
        self.mainwindow.mainloop()
    
    def quitar_resaltado(self, event):
        # Esta función se llama cuando el ComboBox obtiene el foco
        self.mainwindow.focus_set()
        self.cbmstype.config(foreground="navy")
        self.cbmsizem.config(foreground="olive drab")

    #funcion para salir por menubar
    def destruir(self):
        self.mainwindow.destroy()

    #funcion ingresar
    def ingresar(self):
        #aplicamos polimorfismo
        self.tamaño=self.cbmsizem.current()
        self.tipo=self.cbmstype.current()
        self.mainwindow.destroy()
        
        if self.tipo==0:
            if self.tamaño==0:
                imt2X2()
            elif self.tamaño==1:
                imt3X3()
            else:
                imt4X4()
        elif self.tipo==1:
            if self.tamaño==0:
                idet2X2()
            elif self.tamaño==1:
                idet3X3()
            else:
                idet4X4()
        else:
            if self.tamaño==0:
                iiv2X2()
            elif self.tamaño==1:
                iiv3X3()
            else:
                iiv4X4()
    #informacion
    def about(self):
        messagebox.showinfo('Informacion','creador: Daniel S. Gonzalez U. \n\nColaboradores: Andres F. Garcia R.\n                            Nicolas A. Aguilar R.')

#ventana de determinante 2x2
class idet2X2(determinate,functions):
    def __init__(self):
        self.ventana=Tk()
        self.ventana.resizable(0,0)
        self.ventana.geometry("400x440")
        self.ventana.config(bg="dark sea green")
        self.ventana.title("DETERMINANTE 2X2")
        self.ventana.iconbitmap("images/numero.ico")
        #label titulo
        self.titulo=Label(self.ventana,text="DETERMINANTE\n  2X2",font="Arial 22 bold",fg="honeydew4",bg="light sky blue").place(x=80,y=15)
        #entradas de valores
        #numeros izquierda
        self.numero1x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1x.place(x=105,y=140)
        self.numero2x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2x.place(x=105,y=190)
        #numeros derecha
        self.numero1y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1y.place(x=205,y=140)
        self.numero2y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2y.place(x=205,y=190)
        #boton calcular
        self.calculate=Button(self.ventana,bg="gold2",fg="gray26",text="Calcular",font="Arial 19 bold",width=8,command=self.calcular).place(x=130,y=250)
        #texto para mostrar resultado
        self.x=Label(self.ventana,text="Determinante=          ",font=('Arial','20','bold'),bg="khaki",fg="NavajoWhite4")
        self.x.place(x=50,y=340)

        #menu barra
        self.menubar=Menu(self.ventana)
        self.ventana.config(menu=self.menubar)
        file=Menu(self.menubar,tearoff=0)
        file.add_command(label='Volver al menu principal',command=self.volver)
        file.add_separator()
        file.add_command(label="Nuevo calculo",command=self.limpiar)
        file.add_command(label='Cerrar',command=self.destruir)
        self.menubar.add_cascade(label='Opciones',menu=file)

        # Image
        imagen = Image.open("images/ca3.jpg")
        imagen_tk = ImageTk.PhotoImage(imagen)
        self.label = Label(self.ventana, image=imagen_tk)
        self.label.image = imagen_tk
        self.label.place(x=20, y=250)

        self.ventana.mainloop()
        self.s=False

    def destruir(self):
        self.ventana.destroy()

    def volver(self):
        self.ventana.destroy()
        main()

    def limpiar(self):
        self.x['text']="Determinante=          "
        self.numero1x.delete(0, "end")
        self.numero2x.delete(0, "end")
        self.numero1y.delete(0, "end")
        self.numero2y.delete(0, "end")

    def calcular(self):
        try:
            self.value=self.det2x2(float(self.numero1x.get()),
                        float(self.numero2x.get()),
                        float(self.numero1y.get()),
                        float(self.numero2y.get()))
            
            self.x['text']="Determinante="+self.value
        except Exception as e:
            messagebox.showinfo("Error","Debes llenar todos los campos.")
            print(e)

class iiv2X2(inversa,functions):
    def __init__(self):
        self.ventana=Tk()
        self.ventana.resizable(0,0)
        self.ventana.geometry("400x380")
        self.ventana.config(bg="chocolate1")
        self.ventana.title("INVERSA 2X2")
        self.ventana.iconbitmap("images/numero.ico")
        #label titulo
        self.titulo=Label(self.ventana,text="INVERSA\n 2X2",font="Arial 22 bold",fg="dodger blue",bg="CadetBlue1").place(x=130,y=15)
        #entradas de valores
        #numeros izquierda
        self.numero1x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1x.place(x=105,y=140)
        self.numero2x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2x.place(x=105,y=190)
        #numeros derecha
        self.numero1y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1y.place(x=205,y=140)
        self.numero2y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2y.place(x=205,y=190)
        #boton calcular
        self.calculate=Button(self.ventana,bg="OliveDrab2",fg="gray23",text="Calcular",font="Arial 19 bold",width=8,command=self.calcular).place(x=130,y=250)

        #menu barra
        self.menubar=Menu(self.ventana)
        self.ventana.config(menu=self.menubar)
        file=Menu(self.menubar,tearoff=0)
        file.add_command(label='Volver al menu principal',command=self.volver)
        file.add_separator()
        file.add_command(label="Nuevo calculo",command=self.limpiar)
        file.add_command(label='Cerrar',command=self.destruir)
        self.menubar.add_cascade(label='Opciones',menu=file)
        self.ventana.mainloop()

    def destruir(self):
        self.ventana.destroy()

    def volver(self):
        self.ventana.destroy()
        main()

    def limpiar(self):
        self.numero1x.delete(0, "end")
        self.numero2x.delete(0, "end")
        self.numero1y.delete(0, "end")
        self.numero2y.delete(0, "end")
        self.matriz=[[0,0,1,0],[0,0,0,1]]

    def calcular(self):
        try:
            self.values=list(self.iv2x2(self.numero1x.get(),
                                        self.numero2x.get(),
                                        self.numero1y.get(),
                                        self.numero2y.get()))
            
            self.resultado=Tk()
            self.resultado.resizable(0,0)
            self.resultado.geometry("340x280")
            self.resultado.config(bg="DarkOliveGreen1")
            self.resultado.title("INVERSA 2X2")
            self.resultado.iconbitmap("images/numero.ico")
            self.titulo2=Label(self.resultado,text="MATRIZ INVERSA\n   2X2",font="Arial 22 bold",fg="cornflower blue",bg="CadetBlue1").place(x=40,y=15)
            self.valoresf1=Label(self.resultado,bg="yellow3",fg="PaleGreen4",font="Arial 20 bold",text=self.values[0]).place(x=80,y=140)
            self.valoresf2=Label(self.resultado,bg="yellow3",fg="PaleGreen4",font="Arial 20 bold",text=self.values[1]).place(x=80,y=190)
            self.volverif=Button(self.resultado,text="Volver",bg="khaki",fg="gray30",font="Arial 12 bold",width=10,command=self.goback).place(x=110,y=235)
            self.resultado.mainloop()
        except  Exception as e:
            messagebox.showinfo("Error","No has introducido datos correctos.")
            print(e)

    def goback(self):
        self.resultado.destroy()

#ventana de matriz 2x2
class imt2X2(matrices,functions):
    def __init__(self):
        self.s=False
        self.ventana=Tk()
        self.ventana.resizable(0,0)
        self.ventana.geometry("550x450")
        self.ventana.config(bg="dark slate gray")
        self.ventana.title("MATRIZ 2X2")
        self.ventana.iconbitmap("images/numero.ico")
        #label titulo
        self.titulo=Label(self.ventana,text="SISTEMA DE ECUACION\n    2X2",font="Arial 22 bold",fg="gray24",bg="light slate blue")
        self.titulo.place(x=110,y=15)
        #entradas de valores
        #X
        self.rex=Label(self.ventana,bg="dark slate gray",font="Arial 18",fg="turquoise4",text="X").place(x=65,y=110)
        self.numero1x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1x.place(x=40,y=140)
        self.numero2x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2x.place(x=40,y=190)
        #y
        self.rey=Label(self.ventana,bg="dark slate gray",font="Arial 18",fg="DarkOrange4",text="Y").place(x=165,y=110)
        self.numero1y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1y.place(x=140,y=140)
        self.numero2y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2y.place(x=140,y=190)
        #i
        self.rei=Label(self.ventana,bg="dark slate gray",font="Arial 18",fg="DarkOliveGreen4",text="I").place(x=265,y=110)
        self.numero1i=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1i.place(x=240,y=140)
        self.numero2i=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2i.place(x=240,y=190)
        #boton calcular
        self.calculate=Button(self.ventana,bg="DeepSkyBlue2",fg="gray18",text="Calcular",font="Arial 19 bold",width=8,command=self.calcular).place(x=40,y=290)
        #boton hace plano
        self.plano=Button(self.ventana,bg="aquamarine2",fg="gray11",text="Grafica 2D",font="Arial 20 bold",width=8,command=self.graficar).place(x=350,y=160)
        #texto para mostrar resultado
        self.x=Label(self.ventana,text="X=          ",font=('Arial','20','bold'),bg="khaki",fg="NavajoWhite4")
        self.x.place(x=250,y=290)
        self.y=Label(self.ventana,text="Y=          ",font=('Arial','20','bold'),bg="goldenrod1",fg="yellow4")
        self.y.place(x=250,y=350)

        #menu barra
        self.menubar=Menu(self.ventana)
        self.ventana.config(menu=self.menubar)
        file=Menu(self.menubar,tearoff=0)
        file.add_command(label='Volver al menu principal',command=self.volver)
        file.add_separator()
        file.add_command(label="Nuevo calculo",command=self.limpiar)
        file.add_command(label='Cerrar',command=self.destruir)
        self.menubar.add_cascade(label='Opciones',menu=file)
        self.ventana.mainloop()

    def destruir(self):
        self.ventana.destroy()

    def volver(self):
        self.ventana.destroy()
        main()

    def limpiar(self):
        self.x['text']="X=          "
        self.y['text']="Y=          "
        self.numero1x.delete(0, "end")
        self.numero2x.delete(0, "end")
        self.numero1y.delete(0, "end")
        self.numero2y.delete(0, "end")
        self.numero1i.delete(0, "end")
        self.numero2i.delete(0, "end")
        self.matriz=[[0,0,0],[0,0,0]]

    def calcular(self):
        try:
            
            self.values=list(self.mt2x2(float(self.numero1x.get()),
                                        float(self.numero2x.get()),
                                        float(self.numero1y.get()),
                                        float(self.numero2y.get()),
                                        float(self.numero1i.get()),
                                        float(self.numero2i.get())))
                
            self.x['text']="X="+self.values[0]
            self.y['text']="Y="+self.values[1]
            self.s=True
        except  Exception as e:
            messagebox.showinfo("Error","No has introducido datos correctos o\nel sistema no tiene solucion.")
            print(e)

    #boton graficar
    def graficar(self):
        if self.s:
            try:
                a=float(self.numero1x.get())
                b=float(self.numero1y.get())
                c=float(self.numero1i.get())
                d=float(self.numero2x.get())
                e=float(self.numero2y.get())
                f=float(self.numero2i.get())
                # Crear un rango de valores de x
                x = np.linspace(-500, 500, 400)

                # Calcular y para ambas ecuaciones
                y1 = (-a * x + c) / b
                y2 = (-d * x + f) / e

                # Crear el gráfico
                plt.figure(figsize=(8, 6))
                plt.plot(x, y1, label=f'{a}x + {b}y = {c}')
                plt.plot(x, y2, label=f'{d}x + {e}y = {f}')
                plt.xlabel('x')
                plt.ylabel('y')
                plt.grid(True)
                plt.legend()
                plt.title('Gráfico del Sistema de Ecuaciones 2x2')
                plt.axhline(0, color='black', linewidth=0.5)
                plt.axvline(0, color='black', linewidth=0.5)
                plt.xlim(-25, 25)
                plt.ylim(-25, 25)
                plt.show()
                self.s=False
            except  Exception as e:
              messagebox.showwarning("Error","No se puede graficar.")
              print(e)  
        else:
            messagebox.showwarning("Error","No se puede graficar.")

class idet3X3(determinate,functions):
    def __init__(self):
        self.ventana=Tk()
        self.ventana.resizable(0,0)
        self.ventana.geometry("410x490")
        self.ventana.config(bg="dark sea green")
        self.ventana.title("DETERMINANTE 3X3")
        self.ventana.iconbitmap("images/numero.ico")
        #label titulo
        self.titulo=Label(self.ventana,text="DETERMINANTE\n  3X3",font="Arial 22 bold",fg="honeydew4",bg="light sky blue").place(x=80,y=15)
        #entradas de valores
        #X
        self.numero1x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1x.place(x=60,y=140)
        self.numero2x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2x.place(x=60,y=190)
        self.numero3x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3x.place(x=60,y=240)
        #y
        self.numero1y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1y.place(x=160,y=140)
        self.numero2y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2y.place(x=160,y=190)
        self.numero3y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3y.place(x=160,y=240)
        #Z
        self.numero1z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1z.place(x=260,y=140)
        self.numero2z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2z.place(x=260,y=190)
        self.numero3z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3z.place(x=260,y=240)

        #menu barra
        self.menubar=Menu(self.ventana)
        self.ventana.config(menu=self.menubar)
        file=Menu(self.menubar,tearoff=0)
        file.add_command(label='Volver al menu principal',command=self.volver)
        file.add_separator()
        file.add_command(label="Nuevo calculo",command=self.limpiar)
        file.add_command(label='Cerrar',command=self.destruir)
        self.menubar.add_cascade(label='Opciones',menu=file)

        #boton calcular
        self.calculate=Button(self.ventana,bg="gold2",fg="gray26",text="Calcular",font="Arial 19 bold",width=8,command=self.calcular).place(x=140,y=300)

        #solucion del sistema
        self.x=Label(self.ventana,text="Determinante=          ",font=('Arial','20','bold'),bg="khaki",fg="NavajoWhite4")
        self.x.place(x=45,y=390)
        self.ventana.mainloop()

    def destruir(self):
        self.ventana.destroy()

    def volver(self):
        self.ventana.destroy()
        main()

    def limpiar(self):
        self.x['text']="Determinante=            "
        self.numero1x.delete(0, "end")
        self.numero2x.delete(0, "end")
        self.numero3x.delete(0, "end")
        self.numero1y.delete(0, "end")
        self.numero2y.delete(0, "end")
        self.numero3y.delete(0, "end")
        self.numero1z.delete(0, "end")
        self.numero2z.delete(0, "end")
        self.numero3z.delete(0, "end")

    def calcular(self):
        try:
            value=self.det3x3(float(self.numero1x.get()),
                              float(self.numero2x.get()),
                              float(self.numero3x.get()),
                              float(self.numero1y.get()),
                              float(self.numero2y.get()),
                              float(self.numero3y.get()),
                              float(self.numero1z.get()),
                              float(self.numero2z.get()),
                              float(self.numero3z.get()))

            self.x['text']="Determinante="+value
        except  Exception as e:
            messagebox.showinfo("Error","Debes llenar todos los campos.")
            print(e)

class iiv3X3(inversa,functions):
    def __init__(self):
        self.ventana=Tk()
        self.ventana.resizable(0,0)
        self.ventana.geometry("410x410")
        self.ventana.config(bg="chocolate1")
        self.ventana.title("INVERSA 3X3")
        self.ventana.iconbitmap("images/numero.ico")
        #label titulo
        self.titulo=Label(self.ventana,text="INVERSA\n 3X3",font="Arial 22 bold",fg="dodger blue",bg="CadetBlue1").place(x=130,y=15)
        #entradas de valores
        #X
        self.numero1x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1x.place(x=60,y=140)
        self.numero2x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2x.place(x=60,y=190)
        self.numero3x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3x.place(x=60,y=240)
        #y
        self.numero1y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1y.place(x=160,y=140)
        self.numero2y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2y.place(x=160,y=190)
        self.numero3y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3y.place(x=160,y=240)
        #Z
        self.numero1z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1z.place(x=260,y=140)
        self.numero2z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2z.place(x=260,y=190)
        self.numero3z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3z.place(x=260,y=240)

        #menu barra
        self.menubar=Menu(self.ventana)
        self.ventana.config(menu=self.menubar)
        file=Menu(self.menubar,tearoff=0)
        file.add_command(label='Volver al menu principal',command=self.volver)
        file.add_separator()
        file.add_command(label="Nuevo calculo",command=self.limpiar)
        file.add_command(label='Cerrar',command=self.destruir)
        self.menubar.add_cascade(label='Opciones',menu=file)

        #boton calcular
        self.calculate=Button(self.ventana,bg="OliveDrab2",fg="gray23",text="Calcular",font="Arial 19 bold",width=8,command=self.calcular).place(x=140,y=300)
        self.ventana.mainloop()

    def destruir(self):
        self.ventana.destroy()

    def volver(self):
        self.ventana.destroy()
        main()

    def limpiar(self):
        self.numero1x.delete(0, "end")
        self.numero2x.delete(0, "end")
        self.numero3x.delete(0, "end")
        self.numero1y.delete(0, "end")
        self.numero2y.delete(0, "end")
        self.numero3y.delete(0, "end")
        self.numero1z.delete(0, "end")
        self.numero2z.delete(0, "end")
        self.numero3z.delete(0, "end")
        self.matriz=[[0,0,0,1,0,0],
                     [0,0,0,0,1,0],
                     [0,0,0,0,0,1]]

    def calcular(self):
        try:
            self.values=list(self.iv3x3(float(self.numero1x.get()),
                                        float(self.numero2x.get()),
                                        float(self.numero3x.get()),
                                        float(self.numero1y.get()),
                                        float(self.numero2y.get()),
                                        float(self.numero3y.get()),
                                        float(self.numero1z.get()),
                                        float(self.numero2z.get()),
                                        float(self.numero3z.get())))
            
            self.resultado=Tk()
            self.resultado.resizable(0,0)
            self.resultado.geometry("400x330")
            self.resultado.config(bg="DarkOliveGreen1")
            self.resultado.title("INVERSA 3X3")
            self.resultado.iconbitmap("images/numero.ico")
            self.titulo2=Label(self.resultado,text="MATRIZ INVERSA\n   3X3",font="Arial 22 bold",fg="cornflower blue",bg="CadetBlue1").place(x=75,y=15)
            self.valoresf1=Label(self.resultado,bg="yellow3",fg="PaleGreen4",font="Arial 20 bold",text=self.values[0]).place(x=80,y=140)
            self.valoresf2=Label(self.resultado,bg="yellow3",fg="PaleGreen4",font="Arial 20 bold",text=self.values[1]).place(x=80,y=190)
            self.valoresf2=Label(self.resultado,bg="yellow3",fg="PaleGreen4",font="Arial 20 bold",text=self.values[2]).place(x=80,y=240)
            self.volverif=Button(self.resultado,text="Volver",bg="khaki",fg="gray30",font="Arial 12 bold",width=10,command=self.goback).place(x=140,y=290)
            self.resultado.mainloop()
        except  Exception as e:
            messagebox.showinfo("Error","No has introducido datos correctos o\nelsistema no tiene solucion.")
            print(e)
    
    def goback(self):
        self.resultado.destroy()

class imt3X3(matrices,functions):
    def __init__(self):
        self.s=False
        self.ventana=Tk()
        self.ventana.resizable(0,0)
        self.ventana.geometry("590x510")
        self.ventana.config(bg="dark slate gray")
        self.ventana.title("MATRIZ 3X3")
        self.ventana.iconbitmap("images/numero.ico")
        #label titulo
        self.titulo=Label(self.ventana,text="SISTEMA DE ECUACION\n    3X3",font="Arial 22 bold",fg="gray24",bg="light slate blue").place(x=100,y=15)
        #entradas de valores
        #X
        self.rex=Label(self.ventana,bg="dark slate gray",font="Arial 18",fg="turquoise4",text="X").place(x=45,y=110)
        self.rey=Label(self.ventana,bg="dark slate gray",font="Arial 18",fg="DarkOrange4",text="Y").place(x=145,y=110)
        self.rez=Label(self.ventana,bg="dark slate gray",font="Arial 18",fg="DarkOliveGreen4",text="Z").place(x=245,y=110)
        self.rei=Label(self.ventana,bg="dark slate gray",font="Arial 18",fg="gold4",text="I").place(x=345,y=110)
        self.numero1x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1x.place(x=20,y=140)
        self.numero2x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2x.place(x=20,y=190)
        self.numero3x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3x.place(x=20,y=240)
        #y
        self.numero1y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1y.place(x=120,y=140)
        self.numero2y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2y.place(x=120,y=190)
        self.numero3y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3y.place(x=120,y=240)
        #Z
        self.numero1z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1z.place(x=220,y=140)
        self.numero2z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2z.place(x=220,y=190)
        self.numero3z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3z.place(x=220,y=240)
        #i
        self.numero1i=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1i.place(x=320,y=140)
        self.numero2i=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2i.place(x=320,y=190)
        self.numero3i=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3i.place(x=320,y=240)

        #menu barra
        self.menubar=Menu(self.ventana)
        self.ventana.config(menu=self.menubar)
        file=Menu(self.menubar,tearoff=0)
        file.add_command(label='Volver al menu principal',command=self.volver)
        file.add_separator()
        file.add_command(label="Nuevo calculo",command=self.limpiar)
        file.add_command(label='Cerrar',command=self.destruir)
        self.menubar.add_cascade(label='Opciones',menu=file)

        #boton calcular
        self.calculate=Button(self.ventana,bg="DeepSkyBlue2",fg="gray18",text="Calcular",font="Arial 19 bold",width=8,command=self.calcular).place(x=60,y=360)

        #solucion del sistema
        self.x=Label(self.ventana,text="X=          ",font=('Arial','20','bold'),bg="khaki",fg="NavajoWhite4")
        self.x.place(x=250,y=310)
        self.y=Label(self.ventana,text="Y=          ",font=('Arial','20','bold'),bg="goldenrod1",fg="yellow4")
        self.y.place(x=250,y=370)
        self.z=Label(self.ventana,text="Z=          ",font=('Arial','20','bold'),bg="green yellow",fg="dark olive green")
        self.z.place(x=250,y=430)
        
        #boton graficar
        self.plano=Button(self.ventana,bg="aquamarine2",fg="gray11",text="Grafica 3D",font="Arial 20 bold",width=8,command=self.graficar).place(x=410,y=190)
        # Image
        imagen = Image.open("images/ca2.png")
        imagen_tk = ImageTk.PhotoImage(imagen)
        self.label = Label(self.ventana, image=imagen_tk)
        self.label.image = imagen_tk
        self.label.place(x=430, y=360)

        self.ventana.mainloop()

    def destruir(self):
        self.ventana.destroy()

    def volver(self):
        self.ventana.destroy()
        main()

        #metodo del boton calcular
    def calcular(self):
        try:
            self.values=list(self.mt3x3(float(self.numero1x.get()),
                                        float(self.numero2x.get()),
                                        float(self.numero3x.get()),
                                        float(self.numero1y.get()),
                                        float(self.numero2y.get()),
                                        float(self.numero3y.get()),
                                        float(self.numero1z.get()),
                                        float(self.numero2z.get()),
                                        float(self.numero3z.get()),
                                        float(self.numero1i.get()),
                                        float(self.numero2i.get()),
                                        float(self.numero3i.get())))
                

            self.x['text']="X="+self.values[0]
            self.y['text']="Y="+self.values[1]
            self.z['text']="Z="+self.values[2]
            self.s=True
        except Exception as e:
            messagebox.showinfo("Error","No has introducido datos correctos o\nel sistema no tiene solucion.")
            print(e)

    #metodo boton limpiar
    def limpiar(self):
        self.x['text']="X=          "
        self.y['text']="Y=          "
        self.z['text']="Z=          "
        self.numero1x.delete(0, "end")
        self.numero2x.delete(0, "end")
        self.numero3x.delete(0, "end")
        self.numero1y.delete(0, "end")
        self.numero2y.delete(0, "end")
        self.numero3y.delete(0, "end")
        self.numero1z.delete(0, "end")
        self.numero2z.delete(0, "end")
        self.numero3z.delete(0, "end")
        self.numero1i.delete(0, "end")
        self.numero2i.delete(0, "end")
        self.numero3i.delete(0, "end")
        self.matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]    
    
    def graficar(self):
        if self.s:
            try:
                x1=float(self.numero1x.get())
                x2=float(self.numero2x.get())
                x3=float(self.numero3x.get())
                y1=float(self.numero1y.get())
                y2=float(self.numero2y.get())
                y3=float(self.numero3y.get())
                z2=float(self.numero2z.get())
                z3=float(self.numero3z.get())
                i1=float(self.numero1i.get())
                i2=float(self.numero2i.get())
                i3=float(self.numero3i.get())
                # Crear una figura 3D
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')

                # Crear un rango de valores para x y y
                x_range = np.linspace(-500, 500, 500)
                y_range = np.linspace(-500, 500, 500)

                # Crear una cuadrícula de puntos para x y y
                X, Y = np.meshgrid(x_range, y_range)

                # Definir las ecuaciones del sistema
                Z1 = x1*X + y1*Y - i1
                Z2 = x2*X + y2*Y + z2*Z1 - i2
                Z3 = x3*X + y3*Y + z3*Z1  - i3

                ax.plot_surface(X, Y, Z1, alpha=0.5, rstride=100, cstride=100, label=f'{x1}X + {y1}Y - {i1}')
                ax.plot_surface(X, Y, Z2, alpha=0.5, rstride=100, cstride=100, label=f'{x2}X + {y2}Y + {z2}Z1 - {i2}')
                ax.plot_surface(X,Y, Z3, alpha=0.5, rstride=100, cstride=100, label=f'{x3}X + {y3}Y + {z3}Z1 - {i3}')
                # Configurar etiquetas
                ax.set_xlabel('X')
                ax.set_ylabel('Y')
                ax.set_zlabel('Z')
                # Mostrar el gráfico
                plt.show()
                self.s=False
            except Exception as e:
                messagebox.showwarning("Error","No se puede graficar.")
                print(e)
        else:
            messagebox.showwarning("Error","No se puede graficar.")

class imt4X4(matrices,functions):
    def __init__(self):
        self.ventana=Tk()
        self.ventana.resizable(0,0)
        self.ventana.geometry("530x610")
        self.ventana.config(bg="dark slate gray")
        self.ventana.title("MATRIZ 4X4")
        self.ventana.iconbitmap("images/numero.ico")
        #label titulo
        self.titulo=Label(self.ventana,text="SISTEMA DE ECUACION\n    4X4",font="Arial 22 bold",fg="gray24",bg="light slate blue").place(x=100,y=15)
        #entradas de valores
        self.rex=Label(self.ventana,bg="dark slate gray",font="Arial 18",fg="turquoise4",text="X").place(x=45,y=110)
        self.rey=Label(self.ventana,bg="dark slate gray",font="Arial 18",fg="DarkOrange4",text="Y").place(x=145,y=110)
        self.rez=Label(self.ventana,bg="dark slate gray",font="Arial 18",fg="DarkOliveGreen4",text="Z").place(x=245,y=110)
        self.rev=Label(self.ventana,bg="dark slate gray",font="Arial 18",fg="gold4",text="V").place(x=345,y=110)
        self.rei=Label(self.ventana,bg="dark slate gray",font="Arial 18",fg="red4",text="I").place(x=445,y=110)
        #X
        self.numero1x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1x.place(x=20,y=140)
        self.numero2x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2x.place(x=20,y=190)
        self.numero3x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3x.place(x=20,y=240)
        self.numero4x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero4x.place(x=20,y=290)
        #y
        self.numero1y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1y.place(x=120,y=140)
        self.numero2y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2y.place(x=120,y=190)
        self.numero3y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3y.place(x=120,y=240)
        self.numero4y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero4y.place(x=120,y=290)
        #Z
        self.numero1z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1z.place(x=220,y=140)
        self.numero2z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2z.place(x=220,y=190)
        self.numero3z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3z.place(x=220,y=240)
        self.numero4z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero4z.place(x=220,y=290)
        #i
        self.numero1i=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1i.place(x=320,y=140)
        self.numero2i=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2i.place(x=320,y=190)
        self.numero3i=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3i.place(x=320,y=240)
        self.numero4i=Entry(self.ventana,width=5,font="Arial 18")
        self.numero4i.place(x=320,y=290)
        
        self.numero1v=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1v.place(x=420,y=140)
        self.numero2v=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2v.place(x=420,y=190)
        self.numero3v=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3v.place(x=420,y=240)
        self.numero4v=Entry(self.ventana,width=5,font="Arial 18")
        self.numero4v.place(x=420,y=290)

        #boton calcular
        self.calcular=Button(self.ventana,bg="DeepSkyBlue2",fg="gray18",text="Calcular",font="Arial 19 bold",width=8,command=self.calcular).place(x=90,y=420)
        
        #solucion del sistema
        self.v=Label(self.ventana,text="V=          ",font=('Arial','20','bold'),bg="khaki",fg="NavajoWhite4")
        self.v.place(x=340,y=340)
        self.x=Label(self.ventana,text="X=          ",font=('Arial','20','bold'),bg="goldenrod1",fg="yellow4")
        self.x.place(x=340,y=400)
        self.y=Label(self.ventana,text="Y=          ",font=('Arial','20','bold'),bg="green yellow",fg="dark olive green")
        self.y.place(x=340,y=460)
        self.z=Label(self.ventana,text="Z=          ",font=('Arial','20','bold'),bg="cyan",fg="darkred")
        self.z.place(x=340,y=520)

        #menu barra
        self.menubar=Menu(self.ventana)
        self.ventana.config(menu=self.menubar)
        file=Menu(self.menubar,tearoff=0)
        file.add_command(label='Volver al menu principal',command=self.volver)
        file.add_separator()
        file.add_command(label='Nuevo calculo',command=self.limpiar)
        file.add_command(label='Cerrar',command=self.destruir)
        self.menubar.add_cascade(label='Opciones',menu=file)
        self.ventana.mainloop()

    def destruir(self):
        self.ventana.destroy()

    def volver(self):
        self.ventana.destroy()
        main()

        #metodo boton limpiar
    def limpiar(self):
        self.v['text']="V=          "
        self.x['text']="X=          "
        self.y['text']="Y=          "
        self.z['text']="Z=          "
        self.numero1x.delete(0, "end")
        self.numero2x.delete(0, "end")
        self.numero3x.delete(0, "end")
        self.numero4x.delete(0, "end")
        self.numero1y.delete(0, "end")
        self.numero2y.delete(0, "end")
        self.numero3y.delete(0, "end")
        self.numero4y.delete(0, "end")
        self.numero1z.delete(0, "end")
        self.numero2z.delete(0, "end")
        self.numero3z.delete(0, "end")
        self.numero4z.delete(0, "end")
        self.numero1i.delete(0, "end")
        self.numero2i.delete(0, "end")
        self.numero3i.delete(0, "end")
        self.numero4i.delete(0, "end")
        self.numero1v.delete(0, "end")
        self.numero2v.delete(0, "end")
        self.numero3v.delete(0, "end")
        self.numero4v.delete(0, "end")
        self.matriz=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

    #metodo del boton calcular
    def calcular(self):
        try:
            self.values=list(self.mt4x4(float(self.numero1x.get()),
                                        float(self.numero2x.get()),
                                        float(self.numero3x.get()),
                                        float(self.numero4x.get()),
                                        float(self.numero1y.get()),
                                        float(self.numero2y.get()),
                                        float(self.numero3y.get()),
                                        float(self.numero4y.get()),
                                        float(self.numero1z.get()),
                                        float(self.numero2z.get()),
                                        float(self.numero3z.get()),
                                        float(self.numero4z.get()),
                                        float(self.numero1i.get()),
                                        float(self.numero2i.get()),
                                        float(self.numero3i.get()),
                                        float(self.numero4i.get()),
                                        float(self.numero1v.get()),
                                        float(self.numero2v.get()),
                                        float(self.numero3v.get()),
                                        float(self.numero4v.get())))
                
            self.v['text']="V="+self.values[0]
            self.x['text']="X="+self.values[1]
            self.y['text']="Y="+self.values[2]
            self.z['text']="Z="+self.values[3]
        except Exception as e:
            messagebox.showinfo("Error","No has introducido datos correctos.")
            print(e)

class idet4X4(determinate,functions):
    def __init__(self):
        self.ventana=Tk()
        self.ventana.resizable(0,0)
        self.ventana.geometry("490x590")
        self.ventana.config(bg="dark sea green")
        self.ventana.title("DETERMINANTE 4X4")
        self.ventana.iconbitmap("images/numero.ico")
        #label titulo
        titulo=Label(self.ventana,text="DETERMINANTE\n  4X4",font="Arial 22 bold",fg="gray24",bg="light slate blue").place(x=130,y=15)
        #entradas de valores
        #X
        self.numero1x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1x.place(x=60,y=140)
        self.numero2x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2x.place(x=60,y=190)
        self.numero3x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3x.place(x=60,y=240)
        self.numero4x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero4x.place(x=60,y=290)
        #y
        self.numero1y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1y.place(x=160,y=140)
        self.numero2y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2y.place(x=160,y=190)
        self.numero3y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3y.place(x=160,y=240)
        self.numero4y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero4y.place(x=160,y=290)
        #Z
        self.numero1z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1z.place(x=260,y=140)
        self.numero2z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2z.place(x=260,y=190)
        self.numero3z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3z.place(x=260,y=240)
        self.numero4z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero4z.place(x=260,y=290)
        #i
        self.numero1i=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1i.place(x=360,y=140)
        self.numero2i=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2i.place(x=360,y=190)
        self.numero3i=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3i.place(x=360,y=240)
        self.numero4i=Entry(self.ventana,width=5,font="Arial 18")
        self.numero4i.place(x=360,y=290)

        #menu barra
        self.menubar=Menu(self.ventana)
        self.ventana.config(menu=self.menubar)
        file=Menu(self.menubar,tearoff=0)
        file.add_command(label='Volver al menu principal',command=self.volver)
        file.add_separator()
        file.add_command(label="Nuevo calculo",command=self.limpiar)
        file.add_command(label='Cerrar',command=self.destruir)
        self.menubar.add_cascade(label='Opciones',menu=file)

        #boton calcular
        self.calculate=Button(self.ventana,bg="gold2",fg="gray26",text="Calcular",font="Arial 19 bold",width=8,command=self.calcular).place(x=170,y=390)

        #solucion del sistema
        self.x=Label(self.ventana,text="Determinante=          ",font=('Arial','20','bold'),bg="khaki",fg="NavajoWhite4")
        self.x.place(x=75,y=480)
        self.ventana.mainloop()

    def destruir(self):
        self.ventana.destroy()

    def volver(self):
        self.ventana.destroy()
        main()

    def limpiar(self):
        self.x['text']="Determinante=          "
        self.numero1x.delete(0, "end")
        self.numero2x.delete(0, "end")
        self.numero3x.delete(0, "end")
        self.numero4x.delete(0, "end")
        self.numero1y.delete(0, "end")
        self.numero2y.delete(0, "end")
        self.numero3y.delete(0, "end")
        self.numero4y.delete(0, "end")
        self.numero1z.delete(0, "end")
        self.numero2z.delete(0, "end")
        self.numero3z.delete(0, "end")
        self.numero4z.delete(0, "end")
        self.numero1i.delete(0, "end")
        self.numero2i.delete(0, "end")
        self.numero3i.delete(0, "end")
        self.numero4i.delete(0, "end")

    def calcular(self):
        try:
            self.value=self.det4x4(float(self.numero1x.get()),
                                   float(self.numero2x.get()),
                                   float(self.numero3x.get()),
                                   float(self.numero4x.get()),
                                   float(self.numero1y.get()),
                                   float(self.numero2y.get()),
                                   float(self.numero3y.get()),
                                   float(self.numero4y.get()),
                                   float(self.numero1z.get()),
                                   float(self.numero2z.get()),
                                   float(self.numero3z.get()),
                                   float(self.numero4z.get()),
                                   float(self.numero1i.get()),
                                   float(self.numero2i.get()),
                                   float(self.numero3i.get()),
                                   float(self.numero4i.get()))
            
            self.x['text']="Determinante= "+self.value
        except Exception as e:
            messagebox.showinfo("Error","No has introducido datos correctos.")
            print(e)

class iiv4X4(inversa,functions):
    def __init__(self):
        self.ventana=Tk()
        self.ventana.resizable(0,0)
        self.ventana.geometry("490x500")
        self.ventana.config(bg="chocolate1")
        self.ventana.title("INVERSA 4X4")
        self.ventana.iconbitmap("images/numero.ico")
        #label titulo
        self.titulo=Label(self.ventana,text="INVERSA\n 4X4",font="Arial 22 bold",fg="dodger blue",bg="CadetBlue1").place(x=180,y=15)
        #entradas de valores
        #X
        self.numero1x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1x.place(x=60,y=140)
        self.numero2x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2x.place(x=60,y=190)
        self.numero3x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3x.place(x=60,y=240)
        self.numero4x=Entry(self.ventana,width=5,font="Arial 18")
        self.numero4x.place(x=60,y=290)
        #y
        self.numero1y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1y.place(x=160,y=140)
        self.numero2y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2y.place(x=160,y=190)
        self.numero3y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3y.place(x=160,y=240)
        self.numero4y=Entry(self.ventana,width=5,font="Arial 18")
        self.numero4y.place(x=160,y=290)
        #Z
        self.numero1z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1z.place(x=260,y=140)
        self.numero2z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2z.place(x=260,y=190)
        self.numero3z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3z.place(x=260,y=240)
        self.numero4z=Entry(self.ventana,width=5,font="Arial 18")
        self.numero4z.place(x=260,y=290)
        #i
        self.numero1i=Entry(self.ventana,width=5,font="Arial 18")
        self.numero1i.place(x=360,y=140)
        self.numero2i=Entry(self.ventana,width=5,font="Arial 18")
        self.numero2i.place(x=360,y=190)
        self.numero3i=Entry(self.ventana,width=5,font="Arial 18")
        self.numero3i.place(x=360,y=240)
        self.numero4i=Entry(self.ventana,width=5,font="Arial 18")
        self.numero4i.place(x=360,y=290)

        #menu barra
        self.menubar=Menu(self.ventana)
        self.ventana.config(menu=self.menubar)
        file=Menu(self.menubar,tearoff=0)
        file.add_command(label='Volver al menu principal',command=self.volver)
        file.add_separator()
        file.add_command(label="Nuevo calculo",command=self.limpiar)
        file.add_command(label='Cerrar',command=self.destruir)
        self.menubar.add_cascade(label='Opciones',menu=file)

        #boton calcular
        self.calculate=Button(self.ventana,bg="OliveDrab2",fg="gray23",text="Calcular",font="Arial 19 bold",width=8,command=self.calcular).place(x=170,y=390)
        self.ventana.mainloop()

    def destruir(self):
        self.ventana.destroy()

    def volver(self):
        self.ventana.destroy()
        main()

    def limpiar(self):
        self.numero1x.delete(0, "end")
        self.numero2x.delete(0, "end")
        self.numero3x.delete(0, "end")
        self.numero4x.delete(0, "end")
        self.numero1y.delete(0, "end")
        self.numero2y.delete(0, "end")
        self.numero3y.delete(0, "end")
        self.numero4y.delete(0, "end")
        self.numero1z.delete(0, "end")
        self.numero2z.delete(0, "end")
        self.numero3z.delete(0, "end")
        self.numero4z.delete(0, "end")
        self.numero1i.delete(0, "end")
        self.numero2i.delete(0, "end")
        self.numero3i.delete(0, "end")
        self.numero4i.delete(0, "end")
        self.matriz=[[0,0,0,0,1,0,0,0],
                     [0,0,0,0,0,1,0,0],
                     [0,0,0,0,0,0,1,0],
                     [0,0,0,0,0,0,0,1]]

    def calcular(self):
        try:
            self.values=list(self.iv4x4(float(self.numero1x.get()),
                                        float(self.numero2x.get()),
                                        float(self.numero3x.get()),
                                        float(self.numero4x.get()),
                                        float(self.numero1y.get()),
                                        float(self.numero2y.get()),
                                        float(self.numero3y.get()),
                                        float(self.numero4y.get()),
                                        float(self.numero1z.get()),
                                        float(self.numero2z.get()),
                                        float(self.numero3z.get()),
                                        float(self.numero4z.get()),
                                        float(self.numero1i.get()),
                                        float(self.numero2i.get()),
                                        float(self.numero3i.get()),
                                        float(self.numero4i.get())))

            self.resultado=Tk()
            self.resultado.resizable(0,0)
            self.resultado.geometry("460x390")
            self.resultado.config(bg="DarkOliveGreen1")
            self.resultado.title("INVERSA 4X4")
            self.resultado.iconbitmap("images/numero.ico")
            self.titulo2=Label(self.resultado,text="MATRIZ INVERSA\n   4X4",font="Arial 22 bold",fg="cornflower blue",bg="CadetBlue1").place(x=95,y=15)
            self.valoresf1=Label(self.resultado,bg="yellow3",fg="PaleGreen4",font="Arial 20 bold",text=self.values[0]).place(x=80,y=140)
            self.valoresf2=Label(self.resultado,bg="yellow3",fg="PaleGreen4",font="Arial 20 bold",text=self.values[1]).place(x=80,y=190)
            self.valoresf2=Label(self.resultado,bg="yellow3",fg="PaleGreen4",font="Arial 20 bold",text=self.values[2]).place(x=80,y=240)
            self.valoresf2=Label(self.resultado,bg="yellow3",fg="PaleGreen4",font="Arial 20 bold",text=self.values[3]).place(x=80,y=290)
            self.volverif=Button(self.resultado,text="Volver",bg="khaki",fg="gray30",font="Arial 12 bold",width=10,command=self.goback).place(x=170,y=340)
            self.resultado.mainloop()
        except Exception as e:
            messagebox.showinfo("Error","No has introducido datos correctos.")
            print(e)

    def goback(self):
        self.resultado.destroy()

if __name__ == "__main__":
    #iniciador ventana main
    main()