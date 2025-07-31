def progresso_de_carregamento(progresso, total):
    porcentagem = (progresso / total) * 100
    barra = '█' * int(porcentagem // 2)
    espacos = ' ' * (50 - len(barra))
    print(f'\r[{barra}{espacos}] {porcentagem:.2f}%', end='')



'''numeros = [x * 5 for x in range(20000, 80000)]

progresso_de_carregamento(0, len(numeros))
for i, x in enumerate(numeros):
    progresso_de_carregamento(i + 1, len(numeros))'''

