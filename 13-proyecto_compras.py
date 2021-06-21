"""

Crearemos un programa que tiene:

- Ventana (ok)
- Tamaño fijo (ok)
- No redimensionable (ok)
- Menu(ok)
- Diferentes pantallas(ok)
- Formulario para añadir productos(ok)
- Guardar datos(ok)
- Mostrar datos listados en la pantalla home
- Opcion de salir(ok)

"""

#Importamos la libreria y paquete de conexion  MYSQL
from tkinter import *
from tkinter import ttk



# Conexion a la BBDD
import mysql.connector
def conectar():
    database= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="formulario1",
    port=3306
)

    cursor= database.cursor(buffered=True)
    return[database,cursor]


connect = conectar()
database = connect[0]
cursor = connect[1]

#Funcion para guardar en la bbdd

def guardar():

    sql="INSERT INTO compras VALUES(null,%s,%s,%s);"
    datos=(name_data.get(), 
    price_data.get(), 
    add_description_entry.get("1.0","end-1c"))

    cursor.execute(sql, datos)
    database.commit()

    
    return True

#Creamos la ventana

ventana=Tk()
ventana.minsize(500,500) #Dimensionamos
ventana.title("Proyecto | Abraham Bravo") #Indicamos en nombre de la ventana
ventana.resizable(0,0) #No redimensionable

# Creacion de pantallas

def home():
    #Encabezado
    home_label.config(
        fg="white",
        bg="blue",
        font=("Arial",30),
        padx=155,
        pady=20
    )
    home_label.grid(row=0, column=0)
    products_box.grid(row=1)

    #listamos los productos

    for product in products:
        if len(product)==3:
            product.append("añadido")
            products_box.insert('', 0,text=product[0], values=(product[1]))
            """
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text="----------------").grid()
            """
    
    #Ocultar otras pantallas
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    add_frame.grid_remove() #Ocultamos el formulario
    

    return True

def add():
    #Encabezado
    add_label.config(
        fg="white",
        bg="blue",
        font=("Arial",30),
        padx=157,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=4)

    #Llamada a los campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, pady=5, padx=5, sticky=E)
    add_name_entry.grid(row=1, column=1, pady=5, padx=5, sticky=W)

    add_price_label.grid(row=2, column=0, pady=5, padx=5,sticky=E)
    add_price_entry.grid(row=2, column=1, pady=5, padx=5, sticky=W)

    add_description_label.grid(row=3, column=0, pady=5, padx=5,sticky=E)
    add_description_entry.grid(row=3, column=1, pady=5, padx=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=7,
        font=("consolas",12),
        pady=15,
        padx=15
    )

    add_sepator.grid(row=5)
    boton.grid(row=6, column=1)

    #Ocultar pantallas
    info_label.grid_remove()
    data_label.grid_remove()
    home_label.grid_remove()
    products_box.grid_remove()
    return True

def infor():
    
    info_label.config(
        fg="white",
        bg="blue",
        font=("Arial",30),
        padx=170,
        pady=20
    )
    info_label.grid(row=0, column=0)


    
    data_label.grid(row=1, column=0)

    #Ocultar pantallas
    home_label.grid_remove()
    add_label.grid_remove()
    products_box.grid_remove()

    add_frame.grid_remove() #Ocultamos el formulario
    return True

def addproducts():

    products.append([name_data.get(), 
    price_data.get(), 
    add_description_entry.get("1.0","end-1c")])

    

def salvar(): # Funcion para agrupar el salvado en bbdd y en variable
    addproducts()
    guardar()

    #Dejamos los campos vacios

    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0",END)

    home() # para volver automaticamente a la ppal





#Variables importantes
products=[]
name_data=StringVar()
price_data=StringVar()


#Definir campos de las pantallas
info_label=Label(ventana, text="Informacion")
add_label=Label(ventana, text="Añadir producto")

#Creamos el formulario de la pantalla añadir
#Creamos un frame opara introducir el formulario dentro 
add_frame= Frame(ventana)


add_name_label=Label(add_frame, text="Nombre del producto")
add_name_entry=Entry(add_frame, textvariable=name_data)

add_price_label=Label(add_frame, text="Precio del producto")
add_price_entry=Entry(add_frame, textvariable=price_data)

add_description_label=Label(add_frame, text="Descripcion")
add_description_entry=Text(add_frame)

#Creamos el boton
add_sepator=Label(add_frame)
boton= Button(add_frame,text="Guardar", command=salvar)

#Definir campos de las pantallas 2
data_label=Label(ventana, text="Creado por Abraham Bravo - 2021")
home_label=Label(ventana, text="Pantalla de inicio")


products_box=ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text='producto', anchor= W)
products_box.heading("#1", text='precio', anchor= W)

#Cargamos la pantalla home

home()

# Creamos los menu superior

menu_superior=Menu(ventana)
ventana.config(menu=menu_superior) # Cargamos el menu

#Crear submenus cascada
inicio=Menu(menu_superior)
inicio.add_command(label="Inicio", command=home)

anadir=Menu(menu_superior)
anadir.add_command(label="Añadir", command=add)

info=Menu(menu_superior)
info.add_command(label="Informacion", command=infor)

salir=Menu(menu_superior)
salir.add_command(label="Salir", command=ventana.quit)

#Indicamos el menu ppal
menu_superior.add_cascade(label="Inicio",menu=inicio)
menu_superior.add_cascade(label="Añadir",menu=anadir)
menu_superior.add_cascade(label="Info",menu=info)
menu_superior.add_cascade(label="Salir",menu=salir)






#Lanzamos la ventana
ventana.mainloop()