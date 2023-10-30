import socket
import tkinter as tk
from tkinter import filedialog

# Función para seleccionar el archivo a enviar
def seleccionar_archivo():
    global archivo_a_enviar
    archivo_a_enviar = filedialog.askopenfilename()
    archivo_seleccionado_label.config(text=f"Archivo seleccionado: {archivo_a_enviar}")

# Función para iniciar el cliente
def iniciar_cliente():
    HOST = direccion_ip_entry.get()
    PORT = 12345

    # Crea un socket del cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    file_name = archivo_a_enviar.split("/")[-1]

    # Envia el nombre del archivo al servidor
    client_socket.send(file_name.encode())

    # Abre el archivo para lectura y envía los datos en streaming
    with open(archivo_a_enviar, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.send(data)

    print(f"Archivo {file_name} enviado con éxito al servidor")

    # Cierra la conexión
    client_socket.close()

# Crear una ventana para seleccionar archivo
root = tk.Tk()
root.title("Cliente de Archivos")

archivo_seleccionado_label = tk.Label(root, text="Seleccione un archivo para enviar")
archivo_seleccionado_label.pack(pady=10)

seleccionar_archivo_button = tk.Button(root, text="Seleccionar Archivo", command=seleccionar_archivo)
seleccionar_archivo_button.pack()

direccion_ip_label = tk.Label(root, text="Ingrese la dirección IP del servidor:")
direccion_ip_label.pack(pady=5)

direccion_ip_entry = tk.Entry(root)
direccion_ip_entry.pack()

iniciar_cliente_button = tk.Button(root, text="Iniciar Cliente", command=iniciar_cliente)
iniciar_cliente_button.pack(pady=10)

root.mainloop()
