import face_recognition as fr
import cv2
from tkinter import Tk, Label, Canvas, Scrollbar, Frame, HORIZONTAL
from PIL import Image, ImageTk
import numpy as np

def reconhece_face(url_foto):
    # Carregar a imagem usando OpenCV
    foto = cv2.imread(url_foto)  # Carregar a imagem no formato BGR
    if foto is None:
        raise FileNotFoundError(f"Não foi possível carregar a imagem: {url_foto}")
    
    # Converter para RGB para compatibilidade com face_recognition
    foto_rgb = cv2.cvtColor(foto, cv2.COLOR_BGR2RGB)
    localizacoes = fr.face_locations(foto_rgb)  # Obter as localizações dos rostos
    rostos = fr.face_encodings(foto_rgb, localizacoes)  # Obter as codificações dos rostos
    if len(rostos) > 0:
        return True, rostos, foto, localizacoes  # Retorna a imagem original (BGR) e localizações
    
    return False, [], None, []

def mostrar_interface(quantidade_rostos, imagem, localizacoes):
    # Criar uma janela usando tkinter
    janela = Tk()
    janela.title("Reconhecimento Facial")
    janela.geometry("800x600")

    # Adicionar um rótulo para exibir a quantidade de rostos
    texto = f"Quantidade de rostos identificados: {quantidade_rostos}"
    label = Label(janela, text=texto, font=("Arial", 14))
    label.pack(pady=10)

    # Exibir a imagem original no centro da interface (redimensionada)
    if imagem is not None:
        # Garantir que a imagem seja convertida corretamente para RGB
        imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)  # Converter de BGR para RGB
        imagem_pil = Image.fromarray(imagem_rgb)  # Converter para PIL Image

        # Redimensionar a imagem para caber melhor na interface
        largura, altura = imagem_pil.size
        nova_largura = 400  # Definir uma largura menor
        nova_altura = int((nova_largura / largura) * altura)  # Manter a proporção
        imagem_pil = imagem_pil.resize((nova_largura, nova_altura), Image.Resampling.LANCZOS)

        imagem_tk = ImageTk.PhotoImage(imagem_pil)  # Converter para ImageTk

        label_imagem = Label(janela, image=imagem_tk)
        label_imagem.image = imagem_tk  # Manter uma referência para evitar coleta de lixo
        label_imagem.pack(pady=10)

    # Criar um rodapé com rolagem horizontal para exibir os rostos
    frame_rodape = Frame(janela)
    frame_rodape.pack(fill="x", side="bottom")

    canvas = Canvas(frame_rodape, height=150)
    scrollbar = Scrollbar(frame_rodape, orient=HORIZONTAL, command=canvas.xview)
    canvas.configure(xscrollcommand=scrollbar.set)

    scrollbar.pack(side="bottom", fill="x")
    canvas.pack(side="top", fill="x", expand=True)

    # Criar um frame dentro do canvas para adicionar os rostos
    frame_rostos = Frame(canvas)
    canvas.create_window((0, 0), window=frame_rostos, anchor="nw")

    # Exibir cada rosto detectado no rodapé
    if imagem is not None and localizacoes:
        for (top, right, bottom, left) in localizacoes:
            # Recortar o rosto da imagem original
            rosto = imagem[top:bottom, left:right]
            if rosto.size > 0:  # Garantir que o recorte não esteja vazio
                rosto_rgb = cv2.cvtColor(rosto, cv2.COLOR_BGR2RGB)  # Converter de BGR para RGB
                rosto_pil = Image.fromarray(rosto_rgb)  # Converter para PIL Image
                rosto_tk = ImageTk.PhotoImage(rosto_pil)  # Converter para ImageTk

                # Adicionar o rosto ao frame do rodapé
                label_rosto = Label(frame_rostos, image=rosto_tk)
                label_rosto.image = rosto_tk  # Manter uma referência para evitar coleta de lixo
                label_rosto.pack(side="left", padx=5)

    # Ajustar o tamanho do canvas para caber todos os rostos
    frame_rostos.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    # Manter a janela aberta
    janela.mainloop()

# Exemplo de uso
if __name__ == "__main__":
    resultado = reconhece_face("./img/familia.jpg")
    quantidade_rostos = len(resultado[1])
    mostrar_interface(quantidade_rostos, resultado[2], resultado[3])