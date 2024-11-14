n = 50

match n:
    case 0:
        print('É zero')
    case 1:
        print('É um')
    case 2:
        print('É dois')
    case _:
        print('desconhecido')


n = 0
x = 20

match n,x:
    case 0,20:
        print('Teste 1')
    case 20,50:
        print('teste 2')
    case _:
        print('teste 3')

l = [1,2,3]

match l:
    case 3,4,5:
        print('teste 1')
    case 1,2,3:
        print('teste 2')