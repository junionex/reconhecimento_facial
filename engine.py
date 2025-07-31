import face_recognition as fr
import cv2

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    #num_jitters aumenta a precisão da codificação do rosto
    #quanto maior o número, mais preciso, mas mais lento por padrão ele é 1
    rostos = fr.face_encodings(foto, num_jitters=4)
    if(len(rostos) > 0):
        return True, rostos
    
    return False, []

def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    junior = reconhece_face("./img_com_o_rosto_para_ser_verificado/junior.jpg")
    if(junior[0]):
        rostos_conhecidos.append(junior[1][0])
        nomes_dos_rostos.append("Junior")
#    vo_natalia = reconhece_face("./img_com_o_rosto_para_ser_verificado/vo_natalia.jpg")
#    if(vo_natalia[0]):
#        rostos_conhecidos.append(vo_natalia[1][0])
#        nomes_dos_rostos.append("Vo_natalia")

    """cecilia = reconhece_face("./img/cecilia.jpg")
    if(cecilia[0]):
        rostos_conhecidos.append(cecilia[1][0])
        nomes_dos_rostos.append("Cecilia")"""
    
    return rostos_conhecidos, nomes_dos_rostos