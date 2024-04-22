import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def guardar_texto():
    texto = texto_editor.get(1.0, tk.END)
    with open("documento.txt", "w") as archivo:
        archivo.write(texto)
    messagebox.showinfo("Guardar", "El texto ha sido guardado correctamente.")

def abrir_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        with open(archivo, "r") as file:
            contenido = file.read()
            texto_editor.delete(1.0, tk.END)
            texto_editor.insert(1.0, contenido)

def limpiar_texto():
    texto_editor.delete(1.0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Editor de Texto")

# Crear el editor de texto
texto_editor = tk.Text(ventana, height=20, width=60)
texto_editor.pack(pady=10)

# Crear el botón cascada
boton_cascada = tk.Menubutton(ventana, text="Opciones")
boton_cascada.pack(side=tk.TOP, padx=10)

# Crear el menú desplegable
menu = tk.Menu(boton_cascada, tearoff=False)
boton_cascada.configure(menu=menu)

# Añadir opciones al menú
menu.add_command(label="Guardar", command=guardar_texto)
menu.add_command(label="Abrir", command=abrir_archivo)
menu.add_command(label="Limpiar", command=limpiar_texto)

# Ejecutar el bucle de eventos
ventana.mainloop()
