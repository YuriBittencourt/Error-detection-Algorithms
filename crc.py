# coding: utf-8
import sys
import utils

"""
Metodo que realiza as divisoes sucessivas de um binario 
pelo polinimo, funciona tanto para codificacao quanto
para decodificacao do CRC
"""
def calculate_crc(binary, polynomial):

    # Pega os bits do tamanho do polinômio.
    result = binary[: len(polynomial)]

    # indice do valor para ser deslocado para baixo para proxima divisao.
    i = len(result)

    while i <= len(binary):
        # se o primeiro bit for igual a 1 necessita
        # realizar a divisão pelo polinimo
        if result[0] == "1":
            # obtem os bits em forma das colunas
            columns_bits = list(map(list,zip(result,polynomial)))
            # realiza-se a divisao (paridade)
            xor_list = list(map(utils.parity,columns_bits))[1:]
            result = "".join(xor_list)
        # senao realiza uma divisão com elemento neutro(0) o que
        # resulta no próprio elemento
        else:
            result = result[1:]

        if i < len(binary): # necessario para realizar mais um passo da divisao.
                            # pois iria dar indice fora do alcance
            result = result + binary[i]

        # avanca para o proximo bit a ser deslocado para baixo
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


if __name__ == "__main__":

    # se o usuário executar python crc.py -e string polinomio_gerador, executa o encode dessa string
    if sys.argv[1] == '-e':
        string = " ".join(sys.argv[2:-1])
        print(encode(string, sys.argv[-1]))

    # se o usuário executar python crc.py -d hexadecimal polinomio gerador, executa o decode desse hexadecimal
    if sys.argv[1] == '-d':
        print(decode(sys.argv[2], sys.argv[3]))
    