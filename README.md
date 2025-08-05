# CRUD-Contacts
Este es un proyecto para crear un CRUD de contactos con una GUI, ideal para tener de forma organizada nuestros contactos con sus datos de contacto en caso de requerirlos.

## Características
* Agregar contactos con nombre, teléfono y correo
* Visualizar todos los contactos
* Eliminar contactos seleccionados desde un menú desplegable
* Los datos se guardan automáticamente en un archivo local `contactos.json`

## Como Usar
1. Ejecutar el programa
```bash
python3 crud_contacts.py
```
2. Agregar un nuevo contacto; en la parte superior de la ventana verás tres campos de texto con las opciones de
- Nombre
- Teléfono
- Correo
Escribe los datos en los campos correspondientes
3. Haz clic en el botón **Agregar Contacto**
4. Visualizar los contactos; debajo del botón **Agregar Contacto** verás una caja grande en blanco, allí se veran los contactos guardados con sus respectivos datos (recuerda que no estan organizados, solo se iran agregando uno debajo del otro)
5. Eliminar contacto; en la parte inferior hay una menú desplegable con los nombres de los contactos guardados, seleccionas el contacto que deseas eliminar y luego haces clic en el botón **Eliminar Contacto**
