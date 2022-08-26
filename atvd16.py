print('====== Calculadora ======\n')


num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
op = int(input('''Digite a operação que deseja realizar: 
                1 - Soma
                2 - Subtração
                3 - Multiplicação
                4 - Divisão\n\n'''))


def calculadora (num1,num2, op):
    if(op == 1):
        res = num1 + num2 
        return res
    if(op == 2):
        res = num1 - num2
        return res
    if(op == 3):
        res = num1 * num2
        return res
    if(op == 4):
        res = num1 / num2
        return res
    if(op == 0 or op > 4):
        res = 0 
        return res


resultado = calculadora(num1, num2, op)
print(f'O resultado é: {resultado} ')

