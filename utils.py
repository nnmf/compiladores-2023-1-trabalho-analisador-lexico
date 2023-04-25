from dicionarios import *
import re
import sys


def ler_arquivo(teste):
    f = open(teste, 'r')
    program = ""
    buffer = ""
    state = "DEFAULT"
    in_multiline_comment = False
    for line in f:
        i = 0
        while i < len(line):
            if state == "DEFAULT":
                if in_multiline_comment:
                    # Estamos dentro de um comentário de bloco, ignoramos tudo até encontrar o final do comentário
                    if line[i:i + 2] == "*/":
                        in_multiline_comment = False
                        i += 1
                else:
                    # Verifica se há um comentário de linha
                    if line[i:i + 2] == "//":
                        break  # ignoramos o restante da linha
                    elif line[i:i + 2] == "/*":
                        # Início do comentário de bloco
                        in_multiline_comment = True
                        i += 1
                    else:
                        program += line[i]  # Adicionamos o caractere à string do programa
            else:
                # Estamos em um comentário de linha, ignoramos tudo até o final da linha
                break
            i += 1

        # Adicionamos o buffer ao programa se estivermos no estado DEFAULT
        if state == "DEFAULT":
            if not in_multiline_comment:
                program += buffer
                buffer = ""

    f.close()
    return program


def encontrar_Palavras_Reservadas(programa):
    padrao = r"\b(" + "|".join(palavras_reservadas) + r")\b"
    nova_string = re.sub(padrao, lambda match: ' ', programa)
    palavras_reservadas_encontradas = re.findall(padrao, programa)
    palavrasReservadas(palavras_reservadas_encontradas)
    return nova_string


def palavrasReservadas(palavras_reservadas_encontradas):
    if not palavras_reservadas_encontradas:
        print("Não há Palavras Reservadas.")
    for palavra in palavras_reservadas_encontradas:
        print(f"'{palavra}' é uma Palavra Reservada.")


def encontrar_operadores(programa):
    padrao = r"(\s+|)(%s)(\s+|)" % "|".join(map(re.escape, operadores))
    operadores_encontrados = re.findall(padrao, programa)
    imprimir_operadores(operadores_encontrados)
    nova_string = re.sub(padrao, lambda match: ' ', programa)
    return nova_string


def imprimir_operadores(operadores_encontrados):
    if not operadores_encontrados:
        print("Não há Operadores.")
    for op in operadores_encontrados:
        print(f"'{op[1]}' é um Operador.")


def encontrar_numeros(programa):
    padrao = expressoes_regulares['numerais']
    numeros_encontrados = re.findall(padrao, programa)
    inteiros = [num for num in numeros_encontrados if '.' not in num]
    floats = [num for num in numeros_encontrados if '.' in num]

    imprimir_numeros(inteiros, 'Inteiro')
    imprimir_numeros(floats, 'Flutuante')

    nova_string = re.sub(padrao, lambda match: ' ', programa)
    return nova_string


def imprimir_numeros(numeros, tipo):
    if not numeros:
        print(f"Não há nenhum numeral de tipo {tipo}.")
    for num in numeros:
        print(f"'{num}' é um numeral {tipo}.")


def encontrar_constantes_textuais(programa):
    padrao = expressoes_regulares['constantes_textuais']
    constantes_encontradas = re.findall(padrao, programa)
    imprimir_constantes_textuais(constantes_encontradas)
    nova_string = re.sub(padrao, lambda match: ' ', programa)
    return nova_string


def imprimir_constantes_textuais(constantes_encontradas):
    if not constantes_encontradas:
        print("Não há Constantes Textuais.")
    for constante in constantes_encontradas:
        print(f"'{constante}' é uma Constante Textual.")


def encontrar_delimitadores(programa):
    padrao = expressoes_regulares['delimitadores']
    delimitadores_encontrados = re.findall(padrao, programa)
    imprimir_delimitadores(delimitadores_encontrados)
    nova_string = re.sub(padrao, lambda match: ' ', programa)
    return nova_string


def imprimir_delimitadores(delimitadores_encontrados):
    if not delimitadores_encontrados:
        print("Não há Delimitadores.")
    for caracteres in delimitadores_encontrados:
        print(f"'{caracteres}' é um Delimitador.")


def analisar_string(string):
    for caractere in string:
        if caractere not in operadores and caractere not in ignoraveis and not any(
                re.findall(padrao, caractere) for padrao in expressoes_regulares.values()):
            print(f"Erro: o caractere '{caractere}' não é permitido em um nome de identificador.")
            sys.exit()


def encontrar_palavras_com_numeros(programa):
    padrao = r'\b(\d+[a-zA-Z0-9_]*)\b'
    palavras_com_numeros = re.findall(padrao, programa)

    for palavra in palavras_com_numeros:
        if re.match('^\d', palavra):
            print(f'Erro: palavra começando com número encontrada: {palavra}')
            sys.exit()

    return programa


def encontrar_identificadores(programa):
    padrao = expressoes_regulares['identificadores']
    caracteres_identificadores = re.findall(padrao, programa)

    for identificador in caracteres_identificadores:
        if re.match('^\d', identificador) or re.match('[^a-zA-Z0-9_]', identificador):
            print(f'Erro: identificador inválido encontrado: {identificador}')
            exit()

    imprimir_identificadores(caracteres_identificadores)
    nova_string = re.sub(padrao, lambda match: ' ', programa)
    return nova_string


def imprimir_identificadores(identificadores_encontrados):
    if not identificadores_encontrados:
        print("Não há identificadores.")
    for identificadores in identificadores_encontrados:
        print(f"'{identificadores}' é um identificador.")


'''
def encontrar_numeros(programa):
    padrao = expressoes_regulares['numerais']
    numeros_encontrados = re.findall(padrao, programa)
    imprimir_numeros(numeros_encontrados)
    nova_string = re.sub(padrao, lambda match: ' ', programa)
    return nova_string


def encontrar_caracteres_especiais(programa):
    padrao = expressoes_regulares['caracteres_especiais']
    caracteres_encontrados = re.findall(padrao, programa)
    imprimir_caracteres_especiais(caracteres_encontrados)
    nova_string = re.sub(padrao, lambda match: ' ', programa)
    return nova_string
    
    def encontrar_identificadores(programa):
    padrao = expressoes_regulares['identificadores']
    caracteres_identificadores = re.findall(padrao, programa)
    imprimir_identificadores(caracteres_identificadores)
    nova_string = re.sub(padrao, lambda match: ' ', programa)
    return nova_string



def ler_arquivo(teste):
    f = open(teste, 'r')
    program = ""
    buffer = ""
    state = "DEFAULT"
    in_multiline_comment = False
    for line in f:
        i = 0
        while i < len(line):
            if state == "DEFAULT":
                if in_multiline_comment:
                    # Estamos dentro de um comentário de bloco, ignoramos tudo até encontrar o final do comentário
                    if line[i:i + 2] == "*/":
                        in_multiline_comment = False
                        i += 1
                else:
                    # Verifica se há um comentário de linha
                    if line[i:i + 2] == "//":
                        break  # ignoramos o restante da linha
                    elif line[i:i + 2] == "/*":
                        # Início do comentário de bloco
                        in_multiline_comment = True
                        i += 1
                    else:
                        program += line[i]  # Adicionamos o caractere à string do programa
            else:
                # Estamos em um comentário de linha, ignoramos tudo até o final da linha
                break
            i += 1

        # Adicionamos o buffer ao programa se estivermos no estado DEFAULT
        if state == "DEFAULT":
            if not in_multiline_comment:
                program += buffer
                buffer = ""

    f.close()
    return program



def ler_arquivo(teste):
    f = open(teste, 'r')
    program = ""
    buffer = ""
    state = "DEFAULT"
    in_multiline_comment = False
    in_quotes = False
    for line in f:
        i = 0
        while i < len(line):
            if state == "DEFAULT":
                if in_multiline_comment:
                    # Estamos dentro de um comentário de bloco, ignoramos tudo até encontrar o final do comentário
                    if line[i:i + 2] == "*/":
                        in_multiline_comment = False
                        i += 1
                elif in_quotes:
                    if line[i:i + 1] in ["\"", "\'"]:
                        in_quotes = False
                    else:
                        pass
                else:
                    # Verifica se há um comentário de linha
                    if line[i:i + 2] == "//":
                        break  # ignoramos o restante da linha
                    elif line[i:i + 2] == "/*":
                        # Início do comentário de bloco
                        in_multiline_comment = True
                        i += 1
                    elif line[i:i + 1] in ["\"", "\'"]:
                        in_quotes = True
                        program += line[i]
                    else:
                        program += line[i]  # Adicionamos o caractere à string do programa
            else:
                # Estamos em um comentário de linha, ignoramos tudo até o final da linha
                break
            i += 1

        # Adicionamos o buffer ao programa se estivermos no estado DEFAULT
        if state == "DEFAULT":
            if not in_multiline_comment and not in_quotes:
                program += buffer
                buffer = ""

    f.close()
    return program


def ler_arquivo(teste):
    f = open(teste, 'r')
    program = ""
    buffer = ""
    state = "DEFAULT"
    for line in f:
        i = 0
        while i < len(line):
            if state == "DEFAULT":
                if line[i:i + 2] == "//":
                    # Começamos um comentário de linha
                    break
                elif line[i:i + 2] == "/*":
                    # Começamos um comentário de bloco
                    state = "COMMENT_BLOCK"
                    i += 1
                else:
                    # Adicionamos o caractere à string do programa
                    program += line[i]
            elif state == "COMMENT_LINE":
                # Estamos em um comentário de linha, ignoramos tudo até o final da linha
                break
            elif state == "COMMENT_BLOCK":
                if line[i:i + 2] == "*/":
                    # Fim do comentário de bloco
                    state = "DEFAULT"
                    i += 1
                else:
                    # Adicionamos o caractere ao buffer
                    buffer += line[i]
            i += 1

        # Adicionamos o buffer ao programa se estivermos no estado DEFAULT
        if state == "DEFAULT":
            program += buffer
            buffer = ""

    f.close()
    return program
    
    
def encontrar_numeros(programa):
    padrao = expressoes_regulares['numerais']
    numeros_encontrados = re.findall(padrao, programa)

    for numero in numeros_encontrados:
        if re.match('^[a-zA-Z_]|(\d+[a-zA-Z]+)|([a-zA-Z]+\d+\w*)', numero):
            print(f'Erro: número não permitido encontrado: {numero}')
            exit()

    imprimir_numeros(numeros_encontrados)
    nova_string = re.sub(padrao, lambda match: ' ', programa)
    return nova_string


def imprimir_numeros(numeros_encontrados):
    for num in numeros_encontrados:
        print(f"'{num}' é um Numeral.")
    

    
def encontrar_Palavras_Chave(programa):
    padrao = r"\b(" + "|".join(palavras_chave) + r")\b"
    palavras_chave_encontradas = re.findall(padrao, programa)
    return palavrasChave(palavras_chave_encontradas)

def encontrar_operadores(programa, operadores):
    padrao = r"(\s+|)(%s)(\s+|)" % "|".join(map(re.escape, operadores))
    operadores_encontrados = re.findall(padrao, programa)
    return imprimir_operadores(operadores_encontrados)

def encontrar_caracteres_especiais(programa):
    padrao = expressoes_regulares['caracteres_especiais']
    caracteres_encontrados = re.findall(padrao, programa)
    return imprimir_caracteres_especiais(caracteres_encontrados)
    
def encontra_constantes_textuais(programa):
    in_quotes = False
    nova_string = ""
    frase = ''
    for i in range(len(programa)):
        if programa[i] == '"' or programa[i] == "'":
            in_quotes = not in_quotes
            if not in_quotes:
                print(f"'{frase}' é uma Constante Textual.")
                frase = ''
        elif in_quotes:
            frase += programa[i]
        else:
            nova_string += programa[i]
    return nova_string

'''
