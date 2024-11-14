# 1: Verificando se o número é par ou ímpar
def par_ou_impar():
    n = int(input('>> '))
    match n:
        case x if x % 2 == 0:
            print('É par')
        case x if x % 2 > 0:
            print('É impar')
        
# 2: Verificando se um número é positivo, negativo ou zero
def pnz():
    n = int(input('>> '))
    match n:
        case 0:
            print('É zero')
        case x if x > 0:
            print('É positivo')
        case x if x < 0:
            print('É negativo')    

# 3: Verificando se uma string é vazia ou não
def verificando():
    n = input('>> ')
    match n:
        case n if a:
            print('Preenchido')
        case _:
            print('Vazio')
# 4: Verificando se um número é maior, menor ou igual a 10
def maior_ou_igual():
    n = int(input('>> '))
    match n:
        case x if x > 10:
            print('Maior que 10')
        case x if x < 10:
            print('Menor que 10')
        case x if x == 10:
            print('igual a 10')

# 5: Classificando uma idade em faixas etárias -  criança, jovem, adulto, idoso
def etarias():
    n = int(input('>> '))
    match n:
        case x if x <= 10:
            print('Criança')
        case x if x == 12 or x <= 24:
            print('jovem')
        case x if x == 25 or x <= 49:
            print('Adulto')
        case x if x >= 50:
            print('idoso')
