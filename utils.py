from dicionarios import *
import re
import sys


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





def analisar_programa(programa):
    tokens = re.findall(r'({0})|({1})|({2})|({3})'.format(
        '|'.join(map(re.escape, palavras_chave)),
        '|'.join(map(re.escape, operadores)),
        expressoes_regulares['numerais'],
        '|'.join(map(re.escape, expressoes_regulares.values()))
    ), programa)

    for token in tokens:
        if token[0]:
            if token[0] not in palavras_chave:
                print(f'Erro: elemento não esperado encontrado: {token[0]}')
                return
            else:
                print(f'Palavra-chave: {token[0]}')
        elif token[1]:
            if token[1] not in operadores:
                print(f'Erro: elemento não esperado encontrado: {token[1]}')
                return
            else:
                print(f'Operador: {token[1]}')
        elif token[2]:
            print(f'Numeral: {token[2]}')
        elif token[3]:
            if not any(re.match(regex, token[3]) for regex in expressoes_regulares.values()):
                print(f'Erro: elemento não esperado encontrado: {token[3]}')
                return
            else:
                print(f'Identificador, caracter especial ou header: {token[3]}')


def encontrar_Palavras_Chave(programa):
    padrao = r"\b(" + "|".join(palavras_chave) + r")\b"
    nova_string = re.sub(padrao, lambda match: ' ', programa)
    palavras_chave_encontradas = re.findall(padrao, programa)
    palavrasChave(palavras_chave_encontradas)
    return nova_string


def palavrasChave(palavras_chave_encontradas):
    for palavra in palavras_chave_encontradas:
        print(f"'{palavra}' é uma Palavra Reservada.")


def encontrar_operadores(programa):
    padrao = r"(\s+|)(%s)(\s+|)" % "|".join(map(re.escape, operadores))
    operadores_encontrados = re.findall(padrao, programa)
    imprimir_operadores(operadores_encontrados)
    nova_string = re.sub(padrao, lambda match: ' ', programa)
    return nova_string


def imprimir_operadores(operadores_encontrados):
    for op in operadores_encontrados:
        print(f"'{op[1]}' é um Operador.")


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


def encontrar_caracteres_especiais(programa):
    padrao = expressoes_regulares['caracteres_especiais']
    caracteres_encontrados = re.findall(padrao, programa)
    imprimir_caracteres_especiais(caracteres_encontrados)
    nova_string = re.sub(padrao, lambda match: ' ', programa)
    return nova_string


def imprimir_caracteres_especiais(caracteres_encontrados):
    for caracteres in caracteres_encontrados:
        print(f"'{caracteres}' é um Caractere Especial.")


def analisar_string(string):
    for caractere in string:
        if caractere not in operadores and caractere not in ignoraveis and not any(
                re.findall(padrao, caractere) for padrao in expressoes_regulares.values()):
            print(f"Erro: o caractere '{caractere}' não é permitido.")
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

'''
