letra = input('Informe seu estado civil (D,C,S,V): ')

match letra:
    case 'D' | 'd':
        print('Divorciado')
    case 'C' | 'c':
        print('Casado')
    case 'S' | 's':
        print('Solteiro')
    case 'V' | 'v':
        print('Viúvo')
    case _:
        print('Opção Inválida')