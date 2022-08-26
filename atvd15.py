import time

print('BOMBA')

tempo = int(input('Digite em quantos segundos a bomba irá explodir: '))

print('\nIniciando contagem regressiva....\n')

for i in range(tempo,0,-1):
    print(i)
    time.sleep(1)

print('\nTEMPO ESGOTADO \nBOOOOOOMMMMMMM!!!')
