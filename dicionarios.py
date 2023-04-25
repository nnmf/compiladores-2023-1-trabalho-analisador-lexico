palavras_chave = ["break",
                  "case",
                  "char",
                  "const",
                  "continue",
                  "default",
                  "do",
                  "double",
                  "else",
                  "float",
                  "for",
                  "if",
                  "int",
                  "long",
                  "return",
                  "struct",
                  "switch",
                  "typedef",
                  "void",
                  "while",
                  "string",
                  "class",
                  "struct",
                  "include"]

operadores = ["+=",
              "-=",
              "+",
              "-",
              "=",
              "*",
              "/",
              "%",
              "++",
              "--",
              "<=",
              ">="
              ]

ignoraveis = [" ",
              "'",
              "\n",
              "	"
              ]

expressoes_regulares = {
    'numerais': r'\b(\d+\.?\d*)\b',
    'caracteres_especiais': r"[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""'',
    'identificadores': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'headers': r'([a-zA-Z]+\.[h])',
}


'''
expressoes_regulares = {
    'numerais': r'\b(\d+\.?\d*)\b',
    'caracteres_especiais': r"[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""'',
    'identificadores': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'headers': r'([a-zA-Z]+\.[h])',
}



expressoes_regulares = {
    'numerais': r'\b(\d+\.?\d*)\b',
    'caracteres_especiais': r"[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""'',
    'identificadores': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'headers': r'([a-zA-Z]+\.[h])',
}

'''