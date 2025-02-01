import tkinter as tk

def mostrar_texto():
    texto = entrada.get()  # Obtiene el texto de la caja de entrada
    etiqueta.config(text=f"Has escrito: {texto}")  # Modifica el texto de la etiqueta

# Configurar ventana
root = tk.Tk()  
root.title("Ejemplo con entrada de texto")  

# Entrada de texto
entrada = tk.Entry(root)  
entrada.pack(pady=10)  

# Botón para mostrar el texto
boton = tk.Button(root, text="Continuar", command=mostrar_texto)  
boton.pack()  

# Etiqueta para mostrar el resultado
etiqueta = tk.Label(root, text="Escribe algo y presiona el botón")  
etiqueta.pack(pady=10)  

root.mainloop()  # Inicia la aplicación y muestra la ventana
