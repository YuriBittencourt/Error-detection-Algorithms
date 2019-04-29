# coding: utf-8
import sys
import utils


def calculate_crc(binary, polynomial):
    # Procura o primeiro bit significativo
    i = binary.find('1')

    # Pega os bits do tamanho do polinômio e desloca o i para depois dele.
    result = binary[i: i + len(polynomial)]
    i += len(result)

    while i < len(binary):
        # Calcula
        i += 1
    return result

def decode(text, polynomial):
    pass


def encode(text, polynomial):
    # transforma texto em uma lista de strings de binario
    bin_list = [utils.char_to_bin(c, 7) for c in text]

    # adiciona o bit de paridade em cada letra que são 7 bits
    for i in range(0, len(bin_list)):
        # calcula crc de um caracter com n-1 0s concatenados à direita, onde n é o tamanho do polinômio gerador
        bin_list[i] = calculate_crc(bin_list[i] + "".zfill(len(polynomial)),  polynomial)


# se o usuário executar python crc.py -e string polinomio_gerador, executa o encode dessa string
if sys.argv[1] == '-e':
    print(encode(sys.argv[2], sys.argv[3]))

# se o usuário executar python crc.py -d hexadecimal polinomio gerador, executa o decode desse hexadecimal
if sys.argv[1] == '-d':
    print(decode(sys.argv[2], sys.argv[3]))
