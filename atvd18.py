
anoCorreto = False
nome = input('Digite seu nome completo: ')
while(anoCorreto == False):
    try:
        anoNas = int(input('Digite seu ano de nascimento: '))
        if(anoNas >= 1922) and (anoNas <= 2021):
            anoCorreto = True
            idade = 2022 - anoNas
            print('Seu nome é:',nome)
            print('Sua idade é:',idade)
        else:
            print('Digite um ano válido (entre 1922 e 2021)!\n')
    except:
        print('Digite um número!\n') 