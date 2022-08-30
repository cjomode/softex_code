candidato_X = 0
candidato_Y = 0
candidato_Z = 0
nulo = 0
branco = 0

while True:

    try:
        opcao = int(input('''\nDigite o número de qual candidato deseja votar: 
                        Candidato_X = 889
                        Candidato_Y = 847
                        Candidato_Z = 515
                        Branco = 0\n'''))

        if(opcao == 889):
            print('Você escolheu o Candidato_X')
            candidato_X = candidato_X + 1
        elif(opcao == 847):
            print('Você escolheu o Candidato_Y')
            candidato_Y = candidato_Y + 1  
        elif(opcao == 515):
            print('Você escolheu o Candidato_Z')
            candidato_Z = candidato_Z + 1
        elif(opcao == 0):
            print('Você votou Branco')
            branco = branco + 1
        else:
            print('Você votou Nulo')
            nulo = nulo + 1
    except:
      print('Digite um número válido')
      

    fim = int(input('Deseja finalizar seu voto? \n 1 - Sim\n 2 - Não\n'))
    if(fim == 1):
        print('Obrigada pelo seu voto!\n')
    
        if candidato_X > candidato_Y and candidato_X > candidato_Z:
            print(f'Vencedor: Candidato X com {candidato_X} votos\n')
            print(f'Candidato Y: {candidato_Y} votos')
            print(f'Candidato Z: {candidato_Z}')
        elif candidato_Y > candidato_X and candidato_y > candidato_Z:
            print(f'Vencedor: Candidato Y com {candidato_Y} votos\n')
            print(f'Candidato X: {candidato_X} votos')
            print(f'Candidato Z: {candidato_Z}')
        elif candidato_Z > candidato_X and candidato_Z > candidato_Y:
            print(f'Vencedor: Candidado Z com {candidato_Z} votos\n')
            print(f'Candidato X: {candidato_X} votos')
            print(f'Candidato Y: {candidato_Y}')
        break
    if(fim == 2):
        print('Corrija seu voto')
    
print(f'Total votos nulos: {nulo} \nTotal votos brancos: {branco}')