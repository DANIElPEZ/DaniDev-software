import math
from tkinter import messagebox,ttk,Label,Button,Menu,Tk,Entry
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
from abc import ABC,abstractclassmethod

class index():
    def __init__(self):
        self.window=Tk()
        self.window.resizable(0,0)
        self.window.geometry("300x430")
        self.window.title("Vectores")
        self.window.iconbitmap("images/ico.ico")
        #imagen
        imagen = Image.open("images/fondo1.jpg")
        imagen_tk = ImageTk.PhotoImage(imagen)
        self.label = Label(self.window, image=imagen_tk)
        self.label.image = imagen_tk
        self.label.place(x=-2, y=0)
        #nombre
        self.labeln=Label(self.window,text="Nombre:",font="Arial 10 bold",bg="#5f83a5",fg="#e4dfdc").place(x=45,y=267)
        self.name=Entry(self.window,font="Arial 15 bold",width=18,bg="#7c7981",border=1,fg="#c6c1c3")
        self.name.place(x=45,y=290)
        #boton
        self.btnin=Button(self.window,text="Acceder",font="Arial 16 bold",
                          width=13,bg="LightSkyBlue1",fg="gray20",
                          borderwidth=0,
                          command=self.ingresar).place(x=55,y=350)
        self.window.mainloop()

    def ingresar(self):
        self.text=self.name.get()
        if self.text=="":
            messagebox.showinfo("Solicitud","Debes ingresar tu nombre.")
        else:
            self.window.destroy()
            vecsel_gui(self.text)

class vecsel_gui():
    def __init__(self,namel):
        self.name=namel
        self.ventana=Tk()
        self.ventana.resizable(0,0)
        self.ventana.geometry("390x400")
        self.ventana.title("Menu principal")
        self.ventana.iconbitmap("images/ico.ico")
        self.ventana.config(bg="LightBlue2")
        self.namel=Label(self.ventana,text="Bienvenido "+self.name,font="Arial 23 bold",bg="LightBlue2",fg="ghost white")
        self.namel.place(x=20,y=10)
        #menu barra
        self.menubar=Menu(self.ventana)
        self.ventana.config(menu=self.menubar)
        file=Menu(self.menubar,tearoff=0)
        file.add_command(label='Volver al inicio',command=self.volver)
        file.add_separator()
        file.add_command(label='Cerrar',command=self.destruir)
        self.menubar.add_cascade(label='Opciones',menu=file)
        #seleccion para calculo
        self.cbmstype=ttk.Combobox(self.ventana,width=18,font="Arial 12 bold",state="readonly")
        self.cbmstype.place(x=100,y=200)
        self.optioncmbtype=("Suma de vectores","Resta de vectores","Vector")
        self.cbmstype["values"]=self.optioncmbtype
        self.cbmstype.bind("<FocusIn>", self.quitar_resaltado)

        self.etiqueta_imagen = Label(self.ventana,borderwidth=0,bg="LightBlue2")
        self.etiqueta_imagen.place(x=103,y=70)

        self.cbmstype.bind("<<ComboboxSelected>>", self.actualizar_imagen)

        self.btnn_gui=Button(self.ventana,text="Entrar",font="Arial 13 bold",borderwidth=0,width=10,bg="DarkOliveGreen1",fg="gray22",command=self.ingresarcalculo).place(x=140,y=310)        
        self.ventana.mainloop()

    def actualizar_imagen(self, event=None):
            seleccion = self.cbmstype.current()
            if seleccion == 0:
                imagen_path = "images/sel1.jpg"
            elif seleccion == 1:
                imagen_path = "images/sel2.jpg"
            else:
                imagen_path = "images/sel3.jpg"

            imagen = ImageTk.PhotoImage(Image.open(imagen_path))
            self.etiqueta_imagen.config(image=imagen)
            self.etiqueta_imagen.image = imagen

    def quitar_resaltado(self, event):
        # Esta función se llama cuando el ComboBox obtiene el foco
        self.ventana.focus_set()

    def destruir(self):
        self.ventana.destroy()

    def volver(self):
        self.ventana.destroy()
        index()

    def ingresarcalculo(self):
        seleccion = self.cbmstype.current()
        self.ventana.destroy()
        if seleccion == 0:
            suma(self.name)
        elif seleccion==1:
            resta(self.name)
        else:
            byscalar(self.name)

class functions(ABC):
    
    @abstractclassmethod
    def more(self):
        pass

    @abstractclassmethod
    def grados(self):
        pass

    @abstractclassmethod
    def plano(self):
        pass

    @abstractclassmethod
    def operar(self):
        pass

    @abstractclassmethod
    def limpiar(self):
        pass

    @abstractclassmethod
    def destruir(self):
        pass

    @abstractclassmethod
    def volver(self):
        pass
    
    @abstractclassmethod
    def volvermain(self):
        pass

class information():
    def grados(self,x,y):
        grados = math.degrees(math.atan2(y, x))
        # Asegura que los grados estén dentro del rango de 0 a 359
        grados_en_rango = (grados % 360 + 360) % 360
        return grados_en_rango
    
    def distance(self,x,y):
        return ((x)**2+(y)**2)**(0.5)
    
    def dotproduct(self,x1,y1,x2,y2):
        return x1*x2+y1*y2
    
class operar():
    def suma(self,v1,v2):
        return v1+v2
    
    def resta(self,v1,v2):
        return v1-v2

class grafico():
    def onevector(self,x,y):
        plt.figure()
        plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='r', label='Vector 1')
        plt.xlim(0, max(x,  x) + 1)
        plt.ylim(0, max(y,  y) + 1)
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.grid(True)
        plt.legend()
        plt.show()

    def sumoftwovectors(self,v1y,v1x,v2y,v2x):
        vector1 = [v1x, v1y]
        vector2 = [v2x, v2y]
        resultado = (vector1[0] + vector2[0], vector1[1] + vector2[1])
        plt.figure()
        plt.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector 1')
        plt.quiver(0, 0, vector2[0], vector2[1], angles='xy', scale_units='xy', scale=1, color='g', label='Vector 2')
        plt.quiver(0, 0, resultado[0], resultado[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector Resultante')
        plt.plot([vector1[0], resultado[0]], [vector1[1], resultado[1]], linestyle='dashed', color='g')
        plt.plot([vector2[0], resultado[0]], [vector2[1], resultado[1]], linestyle='dashed', color='r')
        plt.xlim(0, max(vector1[0], vector2[0], resultado[0]) + 1)
        plt.ylim(0, max(vector1[1], vector2[1], resultado[1]) + 1)
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.grid(True)
        plt.legend()
        plt.show()

    def subtractionoftwovectors(self,v1y,v1x,v2y,v2x):
        vector1 = [v1x, v1y]
        vector2 = [v2x, v2y]
        resultado = (vector1[0] - vector2[0], vector1[1] - vector2[1])
        plt.figure()
        plt.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector 1')
        plt.quiver(0, 0, vector2[0], vector2[1], angles='xy', scale_units='xy', scale=1, color='g', label='Vector 2')
        plt.quiver(vector2[0], vector2[1],resultado[0], resultado[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector Resultante')
        plt.xlim(0, max(vector1[0], vector2[0], resultado[0]))
        plt.ylim(0, max(vector1[1], vector2[1], resultado[1]))
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.grid(True)
        plt.legend()
        plt.show()

class byscalar(information,grafico,functions):
    def __init__(self,namel):
        self.name=namel
        self.ok=False
        self.ventana=Tk()
        self.ventana.config(bg="light cyan")
        self.ventana.resizable(0,0)
        self.ventana.geometry("400x370")
        self.ventana.title("sesion de - "+self.name)
        self.ventana.iconbitmap("images/ico.ico")
        #menu barra
        self.menubar=Menu(self.ventana)
        self.ventana.config(menu=self.menubar)
        file=Menu(self.menubar,tearoff=0)
        file.add_command(label='Volver al menu principal',command=self.volver)
        file.add_command(label='Volver al inicio',command=self.volvermain)
        file.add_separator()
        file.add_command(label="Nuevo calculo",command=self.limpiar)
        file.add_command(label='Cerrar',command=self.destruir)
        self.menubar.add_cascade(label='Opciones',menu=file)

        self.otrasacciones=Menu(self.menubar,tearoff=0)
        self.otrasacciones.add_command(label="Plano",command=self.plano)
        self.otrasacciones.add_command(label="Mas Informacion",command=self.more)
        self.menubar.add_cascade(label="Acciones",menu=self.otrasacciones)
        #imagenes
        imagen = Image.open("images/row1.jpg")
        imagen_tk = ImageTk.PhotoImage(imagen)
        self.label = Label(self.ventana, image=imagen_tk)
        self.label.image = imagen_tk
        self.label.place(x=190, y=45)
        #labels
        self.ly2=Label(self.ventana,text="Y",bg="light cyan",fg="black",font="Arial 10 bold").place(x=140,y=114)
        self.lx2=Label(self.ventana,text="X",bg="light cyan",fg="black",font="Arial 10 bold").place(x=140,y=48)
        #lbresultado
        self.mulv=Label(self.ventana,text="Vector ingresado:",bg="light cyan",fg="black",font="Arial 15 bold")
        self.mulv.place(x=20,y=290)
        #boton
        self.btncal=Button(self.ventana,borderwidth=0,text="Mostrar",font="Arial 15 bold",fg="white",bg="dark orange",width=11,command=self.operar).place(x=170,y=200)
        #entradas
        #vector1
        self.v1x=Entry(self.ventana,width=3,font="Arial 11 bold",borderwidth=0.5,bg="gray70",fg="black")
        self.v1x.place(x=110,y=48)
        self.v1y=Entry(self.ventana,width=3,font="Arial 11 bold",borderwidth=0.5,bg="gray70",fg="black")
        self.v1y.place(x=110,y=114)
        #escalar
        self.ventana.mainloop()

    def more(self):
        try:
            y=float(self.v1y.get())
            x=float(self.v1x.get())
            self.ifn=Tk()
            self.ifn.resizable(0,0)
            self.ifn.title("Inf. adicional")
            self.ifn.geometry("225x215")
            self.ifn.iconbitmap("images/ico.ico")
            self.ifn.config(bg="DeepSkyBlue4")
            #resultados
            #numero
            self.distancev1="{:.2f}".format(self.distance(x,y))
            vector1=[x/float(self.distancev1), y/float(self.distancev1)]
            gradosv1="{:.2f}".format(self.grados(x,y))

            #label
            Label(self.ifn,text="Distancia\nvector #1: "+self.distancev1,bg="SkyBlue4",fg="azure",font="Arial 13 bold").place(x=20,y=15)
            Label(self.ifn,text="Grados\nvector #1: "+gradosv1+"°",bg="LightSkyBlue4",fg="white",font="Arial 13 bold").place(x=20,y=80)
            Label(self.ifn,text="Vector Unitario\nvector #1: ["+"{:.2f}".format(vector1[0])+", "+"{:.2f}".format(vector1[1])+"]",bg="LightBlue3",fg="alice blue",font="Arial 13 bold").place(x=20,y=145)

            self.ifn.mainloop()
        except Exception as e:
            print(e)
            messagebox.showinfo("Sugerencia","Debes llenar todos los campos.")

    def plano(self):
        if self.ok:
            try:
                self.onevector(float(self.v1x.get()),float(self.v1y.get()))
                self.ok=False
            except:
                messagebox.showinfo("Error","Datos incorrectos.")
        else:
            messagebox.showinfo("Sugerencia","Debes calcular.")

    def operar(self):
        try:
            self.mulv['text']="Vector ingresado: ["+"{:.2f}".format(float(self.v1x.get()))+", "+"{:.2f}".format(float(self.v1y.get()))+"]"
            self.ok=True
        except:
            messagebox.showinfo("Error","Datos incorrectos.")
    
    def limpiar(self):
        self.mulv['text']="Vector resultante:"
        self.v1y.delete(0, "end")
        self.v1x.delete(0, "end")

    def destruir(self):
        self.ventana.destroy()

    def volver(self):
        self.ventana.destroy()
        vecsel_gui(self.name)

    def volvermain(self):
        self.ventana.destroy()
        index()

class suma(operar,information,grafico,functions):
    def __init__(self,namel):
        self.name=namel
        self.ok=False
        self.ventana=Tk()
        self.ventana.config(bg="light cyan")
        self.ventana.resizable(0,0)
        self.ventana.geometry("500x400")
        self.ventana.title("sesion de - "+self.name)
        self.ventana.iconbitmap("images/ico.ico")
        #menu barra
        self.menubar=Menu(self.ventana)
        self.ventana.config(menu=self.menubar)
        file=Menu(self.menubar,tearoff=0)
        file.add_command(label='Volver al menu principal',command=self.volver)
        file.add_command(label='Volver al inicio',command=self.volvermain)
        file.add_separator()
        file.add_command(label="Nuevo calculo",command=self.limpiar)
        file.add_command(label='Cerrar',command=self.destruir)
        self.menubar.add_cascade(label='Opciones',menu=file)

        self.otrasacciones=Menu(self.menubar,tearoff=0)
        self.otrasacciones.add_command(label="Plano",command=self.plano)
        self.otrasacciones.add_command(label="Mas Informacion",command=self.more)
        self.menubar.add_cascade(label="Acciones",menu=self.otrasacciones)

        #imagenes
        imagen = Image.open("images/row1.jpg")
        imagen_tk = ImageTk.PhotoImage(imagen)
        self.label = Label(self.ventana, image=imagen_tk)
        self.label.image = imagen_tk
        self.label.place(x=50, y=40)
        imagen = Image.open("images/row2.jpg")
        imagen_tk = ImageTk.PhotoImage(imagen)
        self.label = Label(self.ventana, image=imagen_tk)
        self.label.image = imagen_tk
        self.label.place(x=300, y=88)
        #labels
        self.ly2=Label(self.ventana,text="Y",bg="light cyan",fg="black",font="Arial 10 bold").place(x=174,y=41)
        self.lx2=Label(self.ventana,text="X",bg="light cyan",fg="black",font="Arial 10 bold").place(x=100,y=15)
        self.ly22=Label(self.ventana,text="Y",bg="light cyan",fg="black",font="Arial 10 bold").place(x=424,y=114)
        self.lx22=Label(self.ventana,text="X",bg="light cyan",fg="black",font="Arial 10 bold").place(x=424,y=90)
        #lbresultado
        self.rta=Label(self.ventana,text="Vector resultante:",bg="light cyan",fg="black",font="Arial 15 bold")
        self.rta.place(x=40,y=290)
        #boton
        self.btncal=Button(self.ventana,borderwidth=0,text="Sumar",font="Arial 15 bold",fg="white",bg="dark orange",width=11,command=self.operar).place(x=170,y=200)
        #entradas
        #vector1
        self.v1x=Entry(self.ventana,width=3,font="Arial 11 bold",borderwidth=0.5,bg="gray70",fg="black")
        self.v1x.place(x=115,y=15)
        self.v1y=Entry(self.ventana,width=3,font="Arial 11 bold",borderwidth=0.5,bg="gray70",fg="black")
        self.v1y.place(x=146,y=41)
        #vector2
        self.v2x=Entry(self.ventana,width=3,font="Arial 11 bold",borderwidth=0.5,bg="gray70",fg="black")
        self.v2x.place(x=397,y=90)
        self.v2y=Entry(self.ventana,width=3,font="Arial 11 bold",borderwidth=0.5,bg="gray70",fg="black")
        self.v2y.place(x=397,y=114)
        self.ventana.mainloop()

    def more(self):
        try:
            vp1y=float(self.v1y.get())
            vp1x=float(self.v1x.get())
            vp2y=float(self.v2y.get())
            vp2x=float(self.v2x.get())
            self.ifn=Tk()
            self.ifn.resizable(0,0)
            self.ifn.title("Informacion adicional")
            self.ifn.geometry("410x300")
            self.ifn.iconbitmap("images/ico.ico")
            self.ifn.config(bg="DeepSkyBlue4")
            #resultados
            #numero
            self.distancev1="{:.2f}".format(self.distance(vp1x,vp1y))
            self.distancev2="{:.2f}".format(self.distance(vp2x,vp2y))
            vector1=[vp1x/float(self.distancev1),vp1y/float(self.distancev1)]
            vector2=[vp2x/float(self.distancev2),vp2y/float(self.distancev2)]
            gradosv1="{:.2f}".format(self.grados(vp1x,vp1y))
            gradosv2="{:.2f}".format(self.grados(vp2x,vp2y))
            pdot="{:.2f}".format(self.dotproduct(vp1x,vp2x,vp1y,vp2y))
            #label
            Label(self.ifn,text="Distancia\nvector #1: "+self.distancev1,bg="SkyBlue4",fg="azure",font="Arial 13 bold").place(x=20,y=15)
            Label(self.ifn,text="Grados\nvector #1: "+gradosv1+"°",bg="LightSkyBlue4",fg="white",font="Arial 13 bold").place(x=20,y=80)
            Label(self.ifn,text="Vector Unitario\nvector #1: ["+"{:.2f}".format(vector1[0])+" "+"{:.2f}".format(vector1[1])+"]",bg="LightBlue3",fg="alice blue",font="Arial 13 bold").place(x=20,y=145)

            Label(self.ifn,text="Distancia\nvector #2: "+self.distancev2,bg="SkyBlue4",fg="azure",font="Arial 13 bold").place(x=220,y=15)
            Label(self.ifn,text="Grados\nvector #2: "+gradosv2+"°",bg="LightSkyBlue4",fg="white",font="Arial 13 bold").place(x=220,y=80)
            Label(self.ifn,text="Vector Unitario\nvector #1: ["+"{:.2f}".format(vector2[0])+", "+"{:.2f}".format(vector2[1])+"]",bg="LightBlue3",fg="alice blue",font="Arial 13 bold").place(x=220,y=145)
            
            Label(self.ifn,text="Producto punto: "+pdot,bg="LightSteelBlue3",fg="snow2",font="Arial 13 bold").place(x=110,y=230)
            self.ifn.mainloop()
        except Exception as e:
            print(e)
            messagebox.showinfo("Sugerencia","Debes llenar todos los campos.")
    
    def plano(self):
        if self.ok:
            try:
                self.sumoftwovectors(float(self.v1y.get()),
                                     float(self.v1x.get()),
                                     float(self.v2y.get()),
                                     float(self.v2x.get()))
                self.ok=False
            except Exception as e:
                print(e)
                messagebox.showinfo("Error","Datos incorrectos.")
        else:
            messagebox.showinfo("Sugerencia","Debes calcular.")

    def operar(self):
        try:
            vsum1="{:.2f}".format(self.suma(float(self.v1x.get()),float(self.v2x.get())))
            vsum2="{:.2f}".format(self.suma(float(self.v1y.get()),float(self.v2y.get())))
            self.rta['text']="Vector resultante: ["+vsum1+", "+vsum2+"]"
            self.ok=True
        except Exception as e:
            print(e)
            messagebox.showinfo("Error","Datos incorrectos.")

    def limpiar(self):
        self.rta['text']="Vector resultante:"
        self.v1y.delete(0, "end")
        self.v1x.delete(0, "end")
        self.v2y.delete(0, "end")
        self.v2x.delete(0, "end")

    def destruir(self):
        self.ventana.destroy()

    def volver(self):
        self.ventana.destroy()
        vecsel_gui(self.name)

    def volvermain(self):
        self.ventana.destroy()
        index()

class resta(operar,information,grafico,functions):
    def __init__(self,namel):
        self.name=namel
        self.ok=False
        self.ventana=Tk()
        self.ventana.config(bg="DarkOliveGreen1")
        self.ventana.resizable(0,0)
        self.ventana.geometry("500x400")
        self.ventana.title("sesion de - "+self.name)
        self.ventana.iconbitmap("images/ico.ico")
        #menu barra
        self.menubar=Menu(self.ventana)
        self.ventana.config(menu=self.menubar)
        file=Menu(self.menubar,tearoff=0)
        file.add_command(label='Volver al menu principal',command=self.volver)
        file.add_command(label='Volver al inicio',command=self.volvermain)
        file.add_separator()
        file.add_command(label="Nuevo calculo",command=self.limpiar)
        file.add_command(label='Cerrar',command=self.destruir)
        self.menubar.add_cascade(label='Opciones',menu=file)

        self.otrasacciones=Menu(self.menubar,tearoff=0)
        self.otrasacciones.add_command(label="Plano",command=self.plano)
        self.otrasacciones.add_command(label="Mas Informacion",command=self.more)
        self.menubar.add_cascade(label="Acciones",menu=self.otrasacciones)
        #imagenes
        imagen = Image.open("images/row1.jpg")
        imagen_tk = ImageTk.PhotoImage(imagen)
        self.label = Label(self.ventana, image=imagen_tk)
        self.label.image = imagen_tk
        self.label.place(x=50, y=40)
        imagen = Image.open("images/row2.jpg")
        imagen_tk = ImageTk.PhotoImage(imagen)
        self.label = Label(self.ventana, image=imagen_tk)
        self.label.image = imagen_tk
        self.label.place(x=300, y=88)
        #labels
        self.ly2=Label(self.ventana,text="Y",bg="DarkOliveGreen1",fg="black",font="Arial 10 bold").place(x=174,y=41)
        self.lx2=Label(self.ventana,text="X",bg="DarkOliveGreen1",fg="black",font="Arial 10 bold").place(x=100,y=15)
        self.ly22=Label(self.ventana,text="Y",bg="DarkOliveGreen1",fg="black",font="Arial 10 bold").place(x=424,y=114)
        self.lx22=Label(self.ventana,text="X",bg="DarkOliveGreen1",fg="black",font="Arial 10 bold").place(x=424,y=90)
        #lbresultado
        self.rta=Label(self.ventana,text="Vector resultante:",bg="DarkOliveGreen1",fg="black",font="Arial 15 bold")
        self.rta.place(x=40,y=290)
        #boton
        self.btncal=Button(self.ventana,borderwidth=0,text="Restar",font="Arial 15 bold",fg="white",bg="medium aquamarine",width=11,command=self.operar).place(x=170,y=200)
        #entradas
        #vector1
        self.v1x=Entry(self.ventana,width=3,font="Arial 11 bold",borderwidth=0.5,bg="gray70",fg="black")
        self.v1x.place(x=115,y=15)
        self.v1y=Entry(self.ventana,width=3,font="Arial 11 bold",borderwidth=0.5,bg="gray70",fg="black")
        self.v1y.place(x=146,y=41)
        #vector2
        self.v2x=Entry(self.ventana,width=3,font="Arial 11 bold",borderwidth=0.5,bg="gray70",fg="black")
        self.v2x.place(x=397,y=90)
        self.v2y=Entry(self.ventana,width=3,font="Arial 11 bold",borderwidth=0.5,bg="gray70",fg="black")
        self.v2y.place(x=397,y=114)
        self.ventana.mainloop()

    def more(self):
        try:
            vp1y=float(self.v1y.get())
            vp1x=float(self.v1x.get())
            vp2y=float(self.v2y.get())
            vp2x=float(self.v2x.get())
            self.ifn=Tk()
            self.ifn.resizable(0,0)
            self.ifn.title("Informacion adicional")
            self.ifn.geometry("410x300")
            self.ifn.iconbitmap("images/ico.ico")
            self.ifn.config(bg="DeepSkyBlue4")
            #resultados
            #numero
            self.distancev1="{:.2f}".format(self.distance(vp1x,vp1y))
            self.distancev2="{:.2f}".format(self.distance(vp2x,vp2y))
            vector1=[vp1x/float(self.distancev1),vp1y/float(self.distancev1)]
            vector2=[vp2x/float(self.distancev2),vp2y/float(self.distancev2)]
            gradosv1="{:.2f}".format(self.grados(vp1x,vp1y))
            gradosv2="{:.2f}".format(self.grados(vp2x,vp2y))
            pdot="{:.2f}".format(self.dotproduct(vp1x,vp2x,vp1y,vp2y))
            #label
            Label(self.ifn,text="Distancia\nvector #1: "+self.distancev1,bg="SkyBlue4",fg="azure",font="Arial 13 bold").place(x=20,y=15)
            Label(self.ifn,text="Grados\nvector #1: "+gradosv1+"°",bg="LightSkyBlue4",fg="white",font="Arial 13 bold").place(x=20,y=80)
            Label(self.ifn,text="Vector Unitario\nvector #1: ["+"{:.2f}".format(vector1[0])+" "+"{:.2f}".format(vector1[1])+"]",bg="LightBlue3",fg="alice blue",font="Arial 13 bold").place(x=20,y=145)

            Label(self.ifn,text="Distancia\nvector #2: "+self.distancev2,bg="SkyBlue4",fg="azure",font="Arial 13 bold").place(x=220,y=15)
            Label(self.ifn,text="Grados\nvector #2: "+gradosv2+"°",bg="LightSkyBlue4",fg="white",font="Arial 13 bold").place(x=220,y=80)
            Label(self.ifn,text="Vector Unitario\nvector #1: ["+"{:.2f}".format(vector2[0])+", "+"{:.2f}".format(vector2[1])+"]",bg="LightBlue3",fg="alice blue",font="Arial 13 bold").place(x=220,y=145)
            
            Label(self.ifn,text="Producto punto: "+pdot,bg="LightSteelBlue3",fg="snow2",font="Arial 13 bold").place(x=110,y=230)
            self.ifn.mainloop()
        except Exception as e:
            print(e)
            messagebox.showinfo("Sugerencia","Debes llenar todos los campos.")

    def plano(self):
        if self.ok:
            try:
                self.subtractionoftwovectors(float(self.v1y.get()),
                                             float(self.v1x.get()),
                                             float(self.v2y.get()),
                                             float(self.v2x.get()))                
                self.ok=False
            except Exception as e:
                print(e)
                messagebox.showinfo("Error","Datos incorrectos.")
        else:
            messagebox.showinfo("Sugerencia","Debes calcular.")

    def operar(self):
        try:
            vsum1="{:.2f}".format(self.resta(float(self.v1x.get()),float(self.v2x.get())))
            vsum2="{:.2f}".format(self.resta(float(self.v1y.get()),float(self.v2y.get())))
            self.rta['text']="Vector resultante: ["+vsum1+", "+vsum2+"]"
            self.ok=True
        except Exception as e:
            print(e)
            messagebox.showinfo("Error","Datos incorrectos.")

    def limpiar(self):
        self.rta['text']="Vector resultante:"
        self.v1y.delete(0, "end")
        self.v1x.delete(0, "end")
        self.v2y.delete(0, "end")
        self.v2x.delete(0, "end")

    def destruir(self):
        self.ventana.destroy()

    def volver(self):
        self.ventana.destroy()
        vecsel_gui(self.name)

    def volvermain(self):
        self.ventana.destroy()
        index()

if __name__ == "__main__":
    index()