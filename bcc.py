# coding: utf-8
import sys
import utils


# Pega a coluna n de str_lst.
def get_col(n, str_lst):
    new_str = ""
    for item in str_lst:
        new_str += item[n]
    return new_str


# Recebe String de texto e retorna a codificacao BCC correspondente
def encode(text):
    # transforma texto em uma lista de strings de binario
    bin_list = [utils.char_to_bin(c, 7) for c in text]

    # adiciona o bit de paridade em cada letra que são 7 bits
    for i in range(0, len(bin_list)):
        bin_list[i] += utils.parity(bin_list[i])

    # calcula o bit de paridade da coluna 0 à 7
    # ex linha1  11011100
    #    linha2  10111010
    # paridade   01100110
    parity = ""
    for i in range(0, 8):
        parity += utils.parity(get_col(i, bin_list))

    bin_list.append(parity)

    # Ler cada String de 8bits da lista e converter em hexadecimal e guardar na resultString.
    result_string = ""
    for b in bin_list:
        result_string += utils.bin_to_hex(b)

    return result_string.upper()


# Recebe String de hexadecimal e retorna a decodificacao BCC correspondente
def decode(text):
    # Quebrar o text em strings binárias de 8bits
    block_size = 2
    bin_list = [utils.hex_to_bin(text[i:i + block_size], 8) for i in range(0, len(text), block_size)]

    # Checar paridade das linhas (
    # comparar a paridade de n-1 bits == ao n-ésimo bit, se diferente retorna ERRO
    for b in bin_list:
        if utils.parity(b[:-1]) != b[-1]:
            return "ERRO"

    # Checar paridade das colunas
    # comparar a paridade das colunas para cada coluna comparar n-1 bits == ao n-ésimo bit, se diferente retorna ERRO
    for i in range(0, 8):
        binary_col = get_col(i, bin_list)
        if utils.parity(binary_col[:-1]) != binary_col[-1]:
            return "ERRO"

    # Não há erros, retornar a mensagem correta
    result_string = ""
    for b in bin_list[:-1]:
        result_string += utils.bin_to_ascii(b[:-1])

    return result_string


# se o usuário executar python bcc.py -e string, executa o encode dessa string
if sys.argv[1] == '-e':
    print(encode(sys.argv[2]))

# se o usuário executar python bcc.py -d hexadecimal, executa o decode desse hexadecimal
if sys.argv[1] == '-d':
    print(decode(sys.argv[2]))

