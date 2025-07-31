from pathlib import Path
from picture import buscarRostos
from progressBar import progresso_de_carregamento
from multiprocessing import Pool


# Caminho da pasta
caminho_pasta = Path("./img")

# Listar os arquivos
arquivos = [arquivo.name for arquivo in caminho_pasta.iterdir() if arquivo.is_file()]
total_de_arquivos = len(arquivos)
#print("total de img: " + str(total_de_arquivos))
#for i, arquivo in enumerate(arquivos):
#    print("\rBuscando os Rostos do arquivo: " + arquivo)
#    progresso_de_carregamento(i + 1, total_de_arquivos)
#    buscarRostos(arquivo)
#buscarRostos("familia.jpg")

def processa_arquivo(args):
    i, arquivo = args
    print("\rBuscando os Rostos do arquivo: " + arquivo)
    progresso_de_carregamento(i + 1, total_de_arquivos)
    buscarRostos(arquivo)

if __name__ == "__main__":
    # Usar multiprocessing para processar os arquivos em paralelo
    # Isso pode acelerar o processo se houver muitos arquivos
    # Pool(processes=4)  # Usa 4 processos Ideal diminuir se n quiser explodir o pc
    with Pool(processes=6) as pool:
        pool.map(processa_arquivo, list(enumerate(arquivos)))
    