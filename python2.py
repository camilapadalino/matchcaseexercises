num = float(input('Insira um número: '))

print('Opção 1 - O dobro')
print('Opção 2 - A metade')
print('Opção 3 - 10% do número')

opcao = int(input('Escolha uma opção: '))

match opcao:
    case 1:
        resultado = num * 2
        print(f'O dobro de {num} é {resultado}')
    case 2:
        resultado = num / 2
        print(f'A metade de {num} é {resultado}')
    case 3:
        resultado = num  * 0.10
        print(f'10% de {num} é {resultado}')
    case _:
        print('Escolha Inválida')