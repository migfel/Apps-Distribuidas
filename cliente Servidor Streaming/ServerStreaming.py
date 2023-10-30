import socket
import tkinter as tk
from tkinter import filedialog

# Función para seleccionar el directorio de destino
def seleccionar_directorio():
    global directorio_destino
    directorio_destino = filedialog.askdirectory()
    directorio_destino_label.config(text="Directorio de destino: {}".format(directorio_destino))

# Función para iniciar el servidor
def iniciar_servidor():
    HOST = direccion_ip_entry.get()
    PORT = 12345

    # Crea un socket del servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)  # Acepta una sola conexión entrante

    print("El servidor está escuchando en {}:{}".format(HOST, PORT))

    # Acepta la conexión entrante
    client_socket, addr = server_socket.accept()
    print("Conexión entrante desde {}".format(addr))

    # Recibe el nombre del archivo
    file_name = client_socket.recv(1024).decode()
    file_path = "{}/{}".format(directorio_destino, file_name)

    # Abre el archivo para escribir los datos recibidos
    with open(file_path, 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)

    print("Archivo recibido y guardado como {}".format(file_path))

    # Cierra la conexión
    client_socket.close()
    server_socket.close()

# Crear una ventana para seleccionar el directorio
root = tk.Tk()
root.title("Servidor de Archivos")

directorio_destino_label = tk.Label(root, text="Seleccione un directorio de destino")
directorio_destino_label.pack(pady=10)

seleccionar_directorio_button = tk.Button(root, text="Seleccionar Directorio", command=seleccionar_directorio)
seleccionar_directorio_button.pack()

direccion_ip_label = tk.Label(root, text="Ingrese la dirección IP del servidor:")
direccion_ip_label.pack(pady=5)

direccion_ip_entry = tk.Entry(root)
direccion_ip_entry.pack()

iniciar_servidor_button = tk.Button(root, text="Iniciar Servidor", command=iniciar_servidor)
iniciar_servidor_button.pack(pady=10)

root.mainloop()
