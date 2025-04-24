import tkinter as tk
from tkinter import ttk #con ttk podemos usar 3 vista
from tkinter import messagebox as mb 
from tkinter scrolledtext as st
import articulos

class FormularioArticulos:
    def _init_(self):
        self.articulo1=articulos.articulos()
        self.ventana1=tk. tk()
        self.ventana1.title("Formulario de Articulos")
        self.cuaderno1=tk.ttk.Notebook(self.ventana1)
        self.cargar_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.cuaderno1.grip(column=0, row=0, padx=10, pady=10)
        self.venata1.mainloop()


    def cargar_articulos(self):
        self.pagina1=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de Articulo")
        self.LabelFrame1=ttk.LabelFrame(self.pagina1, text="Articulos")
        self.LabelFrame1.grid(column=0, row=0 padx=10, pady=10)
        self.label1=ttk.label(self.frame1,text="Description")