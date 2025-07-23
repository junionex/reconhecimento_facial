from pathlib import Path
from picture import buscarRostos

# Caminho da pasta
caminho_pasta = Path("./img")

# Listar os arquivos
arquivos = [arquivo.name for arquivo in caminho_pasta.iterdir() if arquivo.is_file()]
print("total de img: " + str((len(arquivos))))
for arquivo in arquivos:
    print("Buscando os Rostos do arquivo: " + arquivo)
    buscarRostos(arquivo)
#buscarRostos("familia.jpg")