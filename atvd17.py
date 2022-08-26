
def calculadora():
     
    if (op == 1):
     print(f'Soma: {num1+num2}\n')
    elif(op == 2):
        print(f'Subtração: {num1-num2}\n')
    elif(op == 3):
        print(f'Multiplicação: {num1*num2}\n')
    elif(op == 4):
        print(f'Divisão: {num1/num2}\n')
    elif(op > 4):
        print('Essa operação não existe!\n')

          
print ('====== Calculadora ======\n\n')
opcao = int(input('Digite 1 para iniciar a calculadora: '))


while(opcao == 1):
    
     num1 = float(input('Digite um número: '))
     num2 = float(input('Digite outro número: '))
     op = int(input('''Digite a operação que deseja realizar: 
     \n 1 : Soma 
     \n 2 : Subtração 
     \n 3 : Multiplicação 
     \n 4 : Divisão 
     \n 0 : Sair\n'''))
     
     if(opcao == 1):
        calculadora()   
     if(op == 0):
       break

