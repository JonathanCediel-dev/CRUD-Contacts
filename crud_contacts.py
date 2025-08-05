# importaciones externas
import customtkinter as ctk

# importaciones standard
import json
import os
import uuid

# Nombre del archivo donde se guardan los contactos
ARCHIVO_CONTACTOS = "contactos.json"

# Crear archivo vacío si no existe
if not os.path.exists(ARCHIVO_CONTACTOS):
    with open(ARCHIVO_CONTACTOS, "w") as archivo:
        json.dump([], archivo)

# Función para cargar contactos desde el archivo
def cargar_contactos():
    with open(ARCHIVO_CONTACTOS, "r") as archivo:
        return json.load(archivo)

# Función para guardar contactos al archivo
def guardar_contactos():
    with open(ARCHIVO_CONTACTOS, "w") as archivo:
        json.dump(lista_contactos, archivo, indent=4)

# Función para agregar un nuevo contacto
def agregar_contacto():
    nombre = entrada_nombre.get().strip()
    telefono = entrada_telefono.get().strip()
    correo = entrada_correo.get().strip()

    if nombre and telefono and correo:
        nuevo_contacto = {
            "id": str(uuid.uuid4()),
            "nombre": nombre,
            "telefono": telefono,
            "correo": correo
        }
        lista_contactos.append(nuevo_contacto)
        guardar_contactos()
        actualizar_lista()
        actualizar_menu_nombres()
        entrada_nombre.delete(0, ctk.END)
        entrada_telefono.delete(0, ctk.END)
        entrada_correo.delete(0, ctk.END)

# Función para actualizar la lista en pantalla
def actualizar_lista():
    lista_caja.configure(state="normal")
    lista_caja.delete("1.0", ctk.END)
    for contacto in lista_contactos:
        lista_caja.insert(ctk.END, f" {contacto['nombre']}\n {contacto['telefono']}\n {contacto['correo']}\n---\n")
    lista_caja.configure(state="disabled")

# Esta función actualiza el menú desplegable con los nombres de los contactos
def actualizar_menu_nombres():
    nombres = [contacto['nombre'] for contacto in lista_contactos]
    menu_nombres.configure(values=nombres)
    if nombres:
        menu_nombres.set(nombres[0])
    else:
        menu_nombres.set("Sin Contactos")

# Esta función elimina el contacto seleccionado del menú desplegable
def eliminar_contacto():
    nombre_seleccionado = menu_nombres.get()
    if nombre_seleccionado == "Sin contactos":
        return

    global lista_contactos
    lista_contactos = [c for c in lista_contactos if c['nombre'] != nombre_seleccionado]
    guardar_contactos()
    actualizar_lista()
    actualizar_menu_nombres()        

# Configuración de la interfaz principal
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("CRUD de Contactos")
ventana.geometry("500x600")

# Entradas de datos
entrada_nombre = ctk.CTkEntry(ventana, placeholder_text="Nombre")
entrada_nombre.pack(pady=5)

entrada_telefono = ctk.CTkEntry(ventana, placeholder_text="Teléfono")
entrada_telefono.pack(pady=5)

entrada_correo = ctk.CTkEntry(ventana, placeholder_text="Correo")
entrada_correo.pack(pady=5)

# Botón para agregar
boton_agregar = ctk.CTkButton(ventana, text="Agregar Contacto", command=agregar_contacto)
boton_agregar.pack(pady=10)

# Caja para mostrar los contactos
lista_caja = ctk.CTkTextbox(ventana, height=300, width=460, state="disabled", wrap="word")
lista_caja.pack(pady=10)

# Crear un menú desplegable con los nombres de los contactos
menu_nombres = ctk.CTkOptionMenu(ventana, values=["Sin contactos"])
menu_nombres.set("Sin contactos")
menu_nombres.pack(pady=5)

# Botón para eliminar
boton_eliminar = ctk.CTkButton(ventana, text="Eliminar Contacto", command=eliminar_contacto)
boton_eliminar.pack(pady=5)

# Cargar contactos existentes
lista_contactos = cargar_contactos()
actualizar_lista()
actualizar_menu_nombres()

# Ejecutar la aplicación
ventana.mainloop()
