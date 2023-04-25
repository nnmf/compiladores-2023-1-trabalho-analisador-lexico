from utils import *
from dicionarios import *


def main():
    arquivo = ler_arquivo('./testes/teste1.c')
    programa = arquivo
    print(programa)
    programa = encontrar_Palavras_Chave(programa)
    print(programa)
    programa = encontrar_operadores(programa)
    print(programa)
    programa = encontrar_numeros(programa)
    print(programa)
    programa = encontrar_caracteres_especiais(programa)
    print(programa)
    analisar_string(programa)
    encontrar_palavras_com_numeros(programa)
    programa = encontrar_identificadores(programa)
    print(programa)


if __name__ == "__main__":
    print("----------------- Programa Iniciado -----------------")
    main()
    print("----------------- Programa Finalizado -----------------")
