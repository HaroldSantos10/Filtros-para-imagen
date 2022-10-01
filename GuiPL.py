from cgitb import text
from email.mime import image
from msilib.schema import ComboBox
from os import path
from turtle import bgcolor, color, title
from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
from tkinter import StringVar, Tk,Button,Label,ttk, filedialog, messagebox

"""
Harold Enoc Santos Morillo SMIS001621
Meylin Nohely Reyes Medina SMIS032721
"""

def mostrar_imagen():#función que se ejecuta en el boton para cargar imagen
    #abre una ventana para solicitar un archivo(imagen en este caso) para procesar
    file = filedialog.askopenfilename()
    ruta.set(file)#guarda la dirección de acceso del archivo seleccionado y lo envía a la variable StringVar() para poder tratarla en la siguiente función
    imageCargar = Image.open(file).resize((500,400), Image.Resampling.LANCZOS)#abre la imagen según a unas dimensiones predeterminadas
    render1 = ImageTk.PhotoImage(imageCargar)
    #la imagen seleccionada y redimensionada es enviada al label que se encargará de contenerla
    labelImage.configure(image= render1)
    labelImage.image =render1


def aplicar_filtro(event):#función que reacciona al evento bind del combobox
#obtiene el valor de la variable filtro, la cual indica cual es la opción que ha sido seleccionada
    filtrotype= str(filtro.get())
    image = Image.open(ruta.get())#abre la imagen que ha sido seleccionada según la ruta de acceso guardada anteriormente 

    if (filtrotype == "Blanco/Negro"):
        
        image.mode
        imagebn2 = image.convert("L")#Convierte la imagen a blanco y negro
        imagebn2.save("blanco_negro.jpg")#guarda la imagen con el nuevo filtro aplicado con el nombre designado
        messagebox.showinfo(title="Imagen generada correctamente", 
        message=f"Imagen con el filtro {filtrotype} generada y guardada correctamente")#muestra el mensaje de cofirmación
        imagebn2.show()#muestra la nueva imagen generada con el filtro aplicado
        
    elif(filtrotype == "Desenfocar"):

        desenfocar = image.filter(ImageFilter.BoxBlur(10))#Desenfoca la imagen, usó Boxblur en lugar de BLUR debido a que de esta forma se puede regular el nivel de desenfoque aplicado
        desenfocar.save("Desenfocada.jpg")
        messagebox.showinfo(title="Imagen generada correctamente", 
        message=f"Imagen con el filtro {filtrotype} generada y guardada correctamente")
        desenfocar.show()
        
    elif(filtrotype == "Contorno"):
        contorno = image.filter(ImageFilter.CONTOUR)#Resalta las lineas de la imagen
        contorno.save("Contorno.jpg")
        messagebox.showinfo(title="Imagen generada correctamente", 
        message=f"Imagen con el filtro {filtrotype} generada y guardada correctamente")
        contorno.show()
        
    elif(filtrotype == "Resaltar"):
        resaltar = image.filter(ImageFilter.EMBOSS)#Resalta la textura de la imagen
        resaltar.save("Resaltar.jpg")
        messagebox.showinfo(title="Imagen generada correctamente", 
        message=f"Imagen con el filtro {filtrotype} generada y guardada correctamente")
        resaltar.show()
        
    
    


#Creación de la ventana, configuración del tamaño de ventana y su título
ventana = Tk()
ventana.geometry("850x600")
ventana.config(bg="#F0FFFF")
ventana.title("Filtros para imagen")
ruta= tk.StringVar()

#instanciación del label que contendrá la imagen y el boton que permite buscarla y cargarla
labelImage = Label(ventana, image= "")
btnCargarImg= Button(ventana, text="Cargar la imagen", command = mostrar_imagen)
btnCargarImg.config(bg="#E6E6FA")
#instanciación del comboBox que permita la aplicación de los filtros
filtro= StringVar()
#en values designamos el listado de opciones que contendrá el combobox y con textvariable guardamos la selección para según esta realizar una acción u otra
ComboFiltros = ttk.Combobox(ventana,
    values= ["Blanco/Negro","Desenfocar","Contorno","Resaltar"],state="readonly", textvariable= filtro)

#con bind ejecutamos el la funcion que según el eveto ComboboxSelected indica cual opción fue seleccionada
ComboFiltros.bind("<<ComboboxSelected>>", aplicar_filtro)


#asignación del espació que va ocupar cada elemento dentro de la interfaz gráfica

labelImage.place(x=50, y=50, width=500, height=500)
btnCargarImg.place(x=600, y=50, width=100, height=40)
ComboFiltros.place(x=600, y=150, width=200, height=30)

ventana.mainloop()

