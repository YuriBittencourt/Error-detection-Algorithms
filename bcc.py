# coding: utf-8
import sys
import utils


def get_n(n, str_lst):
    new_str = ""
    for item in str_lst:
        new_str += item[n]
    return new_str

#Recebe String de texto e retorna a codificacao BCC correspondente
def encode(text):
    #transforma texto em binario
    bin_list = list(map(utils.to_bin, text))

    #adiciona o bit de paridade em cada letra que são 7 bits
    for i in range(0, len(bin_list)):
        bin_list[i] += utils.parity(bin_list[i])

    #calcula o bit de paridade da coluna 0 à 7
    #ex         11011100
    #           10111010
    #paridade   01100110
    parity=""
    print(bin_list)
    for i in range(0, 8):
        parity += utils.parity(get_n(i, bin_list))
        print(parity)


    return 0


def decode(text):
    return 0


if sys.argv[1] == '-e':
    print(encode(sys.argv[2]))

if sys.argv[1] == '-d':
    print(decode(sys.argv[2]))

