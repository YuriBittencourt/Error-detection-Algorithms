# coding: utf-8
import sys
import utils


#Pega a coluna n de str_lst.
def get_col(n, str_lst):
    new_str = ""
    for item in str_lst:
        new_str += item[n]
    return new_str


#Recebe String de texto e retorna a codificacao BCC correspondente
def encode(text):
    #transforma texto em binario
    bin_list = [utils.char_to_bin(c, 7) for c in text]

    #adiciona o bit de paridade em cada letra que são 7 bits
    for i in range(0, len(bin_list)):
        bin_list[i] += utils.parity(bin_list[i])

    #calcula o bit de paridade da coluna 0 à 7
    #ex         11011100
    #           10111010
    #paridade   01100110
    parity=""
    for i in range(0, 8):
        parity += utils.parity(get_col(i, bin_list))

    #Ler cada String de 8bits da lista e converter em hexadecimal e guardar na resultString.
    resultString = ""
    for b in bin_list:
        resultString += utils.bin_to_hex(b)

    return resultString


def decode(text):
    return 0


if sys.argv[1] == '-e':
    print(encode(sys.argv[2]))

if sys.argv[1] == '-d':
    print(decode(sys.argv[2]))

