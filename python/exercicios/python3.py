numero = int(input('Insira um número inteiro: '))

resto = numero % 3

match resto:
    case 0:
        print('É múltiplo de 3')
    case _:
        print('Não é múltiplo de 3')