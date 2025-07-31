import face_recognition as fr
from engine import reconhece_face, get_rostos
from pathlib import Path

def buscarRostos(url_arquivo):
    desconhecido = reconhece_face("./img/"+url_arquivo)
    #print("\rForam detectados " + str(len(desconhecido[1])) + " faces")
    if(desconhecido[0]):
        for j in range(len(desconhecido[1])):
            rosto_desconhecido = desconhecido[1][j]
            rostos_conhecidos, nomes_dos_rostos = get_rostos()
            #tolerance 0.6 por padrão, quanto menor mais rigorosa é a comparação
            resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido, tolerance=0.4)
            #print("\r" + str(resultados))

            for i in range(len(rostos_conhecidos)):
                resultado = resultados[i]
                if(resultado):
                    #print("\rRosto do", nomes_dos_rostos[i], "foi reconhecido")
                    
                    destino = Path("./img_correspondente_ao_rosto/" + nomes_dos_rostos[i] + "_" + url_arquivo)
                    destino.write_bytes(Path("./img/"+url_arquivo).read_bytes())

    else:
        #print("\rNao foi encontrado nenhum rosto")
        pass