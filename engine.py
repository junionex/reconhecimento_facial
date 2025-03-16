import face_recognition as fr
import cv2

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos
    
    return False, []

def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    junior = reconhece_face("./img/junior.jpg")
    if(junior[0]):
        rostos_conhecidos.append(junior[1][0])
        nomes_dos_rostos.append("Junior")

    """cecilia = reconhece_face("./img/cecilia.jpg")
    if(cecilia[0]):
        rostos_conhecidos.append(cecilia[1][0])
        nomes_dos_rostos.append("Cecilia")"""
    
    return rostos_conhecidos, nomes_dos_rostos