from utils import *
from dicionarios import *


def main():
    nome = './testes/teste1.c'
    programa = ler_arquivo(nome)
    original = open(nome, 'r')
    print(original.read())

    print('-----------------\n' + programa + '\n-----------------\n')
    programa = encontrar_constantes_textuais(programa)
    print('\n-----------------\n' + programa + '\n-----------------\n')
    programa = encontrar_Palavras_Reservadas(programa)
    print('\n-----------------\n' + programa + '\n-----------------\n')
    programa = encontrar_operadores(programa)
    print('\n-----------------\n' + programa + '\n-----------------\n')
    programa = encontrar_numeros(programa)
    print('\n-----------------\n' + programa + '\n-----------------\n')
    programa = encontrar_delimitadores(programa)
    print('\n-----------------\n' + programa + '\n-----------------\n')
    programa = encontrar_identificadores(programa)
    print('\n-----------------\n' + programa + '\n-----------------\n')


if __name__ == "__main__":
    print("----------------- Programa Iniciado -----------------")
    main()
    print("----------------- Programa Finalizado -----------------")
