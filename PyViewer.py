import os
import sys
import keyboard
from tkinter import Tk, Label
from PIL import Image, ImageTk
import winsound

# Função para navegar entre imagens
def navegar(delta):
    global index
    index += delta
    if index < 0:
        index = 0
    elif index >= len(image_files):
        index = len(image_files) - 1
    exibir_imagem()

# Função para copiar a imagem original
def copiar_imagem():
    if 0 <= index < len(image_files):
        caminho_imagem = image_files[index]
        pasta_saida = output_folder_entry
        if not os.path.exists(pasta_saida):
            os.makedirs(pasta_saida)
        arquivo_saida = os.path.join(pasta_saida, os.path.basename(caminho_imagem))
        try:
            imagem_original = Image.open(caminho_imagem)
            imagem_original.save(arquivo_saida)
            copy_label.config(text=f"Imagem copiada para {arquivo_saida}")
            winsound.Beep(500, 100)  # Tocar um som de beep
        except Exception as e:
            copy_label.config(text=f"Erro ao copiar a imagem: {str(e)}")

# Função para atualizar as etiquetas da imagem e do nome do arquivo
def exibir_imagem():
    if 0 <= index < len(image_files):
        caminho_imagem = image_files[index]
        img = Image.open(caminho_imagem)
        img.thumbnail((512, 512))  # Preservar a proporção e ajustar para 512x512
        global foto  # Tornar 'foto' uma variável global
        foto = ImageTk.PhotoImage(img)
        image_label.config(image=foto)
        filename_label.config(text=os.path.basename(caminho_imagem))
        copy_label.config(text="")

# Criar a janela principal
root = Tk()
root.title("PyViewer 1.0")
root.geometry("512x512")

# Verificar os argumentos da linha de comando
if len(sys.argv) != 3:
    print("Uso: python pyViewer.py <pasta_das_imagens> <pasta_de_saida>")
    sys.exit(1)

image_folder_entry, output_folder_entry = sys.argv[1], sys.argv[2]

# Criar etiquetas para a pasta de imagens, pasta de saída e nome do arquivo
image_folder_label = Label(root, text=f"Pasta de Imagens: {image_folder_entry}")
image_folder_label.pack()
output_folder_label = Label(root, text=f"Pasta de Saída: {output_folder_entry}")
output_folder_label.pack()
filename_label = Label(root, text="")
filename_label.pack()

# Criar uma etiqueta para exibir a imagem atual
image_label = Label(root)
image_label.pack()

# Criar uma etiqueta para exibir o status da cópia
copy_label = Label(root, text="")
copy_label.pack()

# Associar as teclas de seta e a tecla "C" às funções correspondentes
keyboard.add_hotkey('right', lambda: navegar(1))
keyboard.add_hotkey('left', lambda: navegar(-1))
keyboard.add_hotkey('c', copiar_imagem)

# Inicializar variáveis
image_files = [os.path.join(image_folder_entry, f) for f in os.listdir(image_folder_entry) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
image_files.sort()
index = 0
foto = None

# Avançar automaticamente para a primeira imagem
navegar(1)

# Iniciar o loop principal
root.mainloop()
