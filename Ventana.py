from tkinter import *
import tkinter as tk
from tkinter import scrolledtext,filedialog, messagebox

class Ventana:
    Data = ""

    def __init__(self, raiz):

        self.raiz = raiz
        self.raiz.title ("Editor")
        self.raiz.geometry(("800x450+300+120"))
        self.raiz.resizable(0,0)


        self.ventana = tk.Frame(raiz)
        self.ventana.config(background="orange")
        self.ventana.pack(fill=tk.BOTH, expand=True)

        self.menu_barra = tk.Menu(self.raiz)
        self.raiz.config(menu = self.menu_barra)

        self.texto_editor = scrolledtext.ScrolledText(self.ventana, height=25, width=80)
        self.texto_editor.pack()
        self.texto_editor.place(x="80",y="20")
        

        self.menu_archivo = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_archivo.add_command(label="Nuevo", command=self.limpiar_texto)
        self.menu_archivo.add_command(label="Abrir", command = self.abrir_archivo)
        self.menu_archivo.add_command(label="Guardar", command= self.guardar)
        self.menu_archivo.add_command(label="Guardar Como", command= self.guardar_como)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=root.quit)

        self.menu_analisis = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_analisis.add_command(label="Analizar")

        self.menu_token = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_token.add_command(label="Reporte Tokens")

        self.menu_errores = tk.Menu(self.menu_barra, tearoff=0)
        self.menu_errores.add_command(label="Reporte Errores")


        self.menu_barra.add_cascade(label="Archivo", menu= self.menu_archivo)
        self.menu_barra.add_cascade(label= "Analisis", menu= self.menu_analisis)
        self.menu_barra.add_cascade(label="Token", menu= self.menu_token)
        self.menu_barra.add_cascade(label="Errores", menu= self.menu_errores)

        self.archivo_abierto = ""
    def abrir_archivo(self):
        archivo = filedialog.askopenfilename()
        if archivo:
            self.archivo_abierto = archivo
            with open(archivo, 'r', encoding="utf8") as file:
                contenido = file.read()
                self.texto_editor.delete(1.0, tk.END)
                global Data
                Data = contenido
                Data = self.texto_editor.insert(tk.INSERT, Data)
                Data = self.texto_editor.get("1.0","end-1c")
                print("===================================================")
                print(Data)
            #self.columna_numeros()

    def guardar_como(self):
        archivo = filedialog.asksaveasfilename(defaultextension = ".lfp")
        if archivo:
            contenido = self.texto_editor.get(1.0, tk.END)
            with open(archivo, "w") as file:
                file.write(contenido)
            messagebox.showinfo("Guardado", "Archivo Guardado")

    
    def guardar(self):
        
        if self.archivo_abierto:
            texto = self.texto_editor.get(1.0, tk.END)
            with open(self.archivo_abierto, "w") as archivo_guardar:
                archivo_guardar.write(texto)
            messagebox.showinfo("Guardar", "El texto ha sido guardado correctamente.")
        else:
            messagebox.showwarning("Advertencia", "No se ha abierto ningún archivo.")

    def limpiar_texto(self):
        self.texto_editor.delete(1.0, tk.END)








if __name__ == "__main__":
    root = tk.Tk()
    app = Ventana(root)
    root.mainloop()