import os
import shutil

# **Exercício 1: Criar e ler um Arquivo**
def criar():
    with open('arquivo', 'w') as arquivo:
        os.mkdir('arquivo')

def ler():
    with open('arquivo', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

# **Exemplo 2: Entrar em um Diretório**
def diretorio():
    with os.scandir('C:/Users/aluno\Desktop/aula13') as diretorio:
        for n in diretorio:
            print(f'Arquivo: {n.name}')

# **Exercício 3: Renomear um Diretório**
def rename():
    os.rename('arquivo' ,  'arquivo02')
    
# **Exercício 4: Remover um Diretório**
def excluir():
    shutil.rmtree('C:/Users/aluno/Desktop/aula13/pasta teste')

# **Exercício 5: Listar Arquivos em um Diretório** 
def diretorio():
    with os.scandir('C:/Users/aluno/Desktop/aula13') as diretorio:
        for n in diretorio:
            print(f'Arquivo: {n.name}')

# **Exercício 6: Copiar Arquivos em um Diretório**
def copy():
    shutil.copytree('antigo', 'novo')

# criar()
# ler()
# diretorio()
# rename()
# excluir()