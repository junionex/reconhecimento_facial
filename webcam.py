import numpy as np
import face_recognition as fr
import cv2
from engine import get_rostos

# Carregar rostos conhecidos e seus nomes
rostos_conhecidos, nomes_dos_rostos = get_rostos()

# Iniciar captura de vídeo
video_capture = cv2.VideoCapture(0)

# Verificar se a captura de vídeo foi iniciada corretamente
if not video_capture.isOpened():
    print("Erro ao abrir a câmera")
    exit()

while True: 
    # Capturar frame da webcam
    ret, frame = video_capture.read()
    if not ret:
        print("Falha ao capturar imagem")
        break

    # Converter a imagem de BGR (OpenCV) para RGB (face_recognition)
    rgb_frame = frame[:, :, ::-1]
    code = cv2.COLOR_BGR2RGB
    rgb_frame = cv2.cvtColor(rgb_frame, code)
    # Encontrar todas as localizações de rostos na imagem
    localizacao_dos_rostos = fr.face_locations(rgb_frame)
    if not localizacao_dos_rostos:
        print("Nenhum rosto encontrado")
        cv2.imshow('Webcam_facerecognition', frame)
        if cv2.waitKey(1) == 27:
            break
        continue

    # Obter as codificações dos rostos
    try:
        rosto_desconhecidos = fr.face_encodings(rgb_frame, localizacao_dos_rostos)
    except Exception as e:
        print(f"Erro ao obter codificações dos rostos: {e}")
        cv2.imshow('Webcam_facerecognition', frame)
        

    if not rosto_desconhecidos:
        print("Falha ao obter codificações dos rostos")
        cv2.imshow('Webcam_facerecognition', frame)

    # Percorrer todas as localizações de rostos e codificações
    for (top, right, bottom, left), rosto_desconhecido in zip(localizacao_dos_rostos, rosto_desconhecidos):
        # Comparar rosto desconhecido com rostos conhecidos
        resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
        print(f"Resultados da comparação: {resultados}")

        # Calcular a distância do rosto
        face_distances = fr.face_distance(rostos_conhecidos, rosto_desconhecido)
        print(f"Distâncias dos rostos: {face_distances}")
        
        # Encontrar o rosto conhecido mais próximo
        melhor_id = np.argmin(face_distances)
        if resultados[melhor_id]:
            nome = nomes_dos_rostos[melhor_id]
        else:
            nome = "Desconhecido"
        
        # Desenhar um retângulo ao redor do rosto
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Desenhar um retângulo embaixo do rosto
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX

        # Escrever o nome do rosto
        cv2.putText(frame, nome, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Mostrar a imagem com os rostos reconhecidos
    cv2.imshow('Webcam_facerecognition', frame)

    # Sair do loop se a tecla 'ESC' for pressionada
    if cv2.waitKey(5) == 27:
        break

# Liberar a captura de vídeo e destruir todas as janelas
video_capture.release()
cv2.destroyAllWindows()