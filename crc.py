# coding: utf-8
"""
Autores: Vinicius Cerutti e Yuri Bittencourt
Trabalho de Introdução a Redes de Computadores 2019/1
"""


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
        # senao realiza uma divisao com elemento neutro(0) o que
        # resulta no proprio elemento
        else:
            result = result[1:]

        if i < len(binary): # necessario para realizar mais um passo da divisao.
                            # pois iria dar indice fora do alcance
            result = result + binary[i]

        # avanca para o proximo bit a ser deslocado para baixo
        i += 1

    return result

"""
Metodo no qual realiza a decodificao de cada trio de hexadecimais, retorna 
a mensagem decodificada e uma lista de indices de erros.
"""
def decode(text, polynomial):

    # Quebrar o texto hexadecimal em uma lista de  binario onde cada binario
    # tem 12 bits (3 hexadecimais)
    block_size = 3
    bin_list = [utils.hex_to_bin(text[i:i + block_size], 8) for i in range(0, len(text), block_size)]

    mensagem = ""
    erros = []

    # Calcular o CRC de cada caractere
    for i in range(0,len(bin_list)):
         # se o resultado for igual a zero pega o binario descontando os 
         # ultimos 4 bits (o ultimo hexadecimal e converte para ASCII)
        if utils.bin_to_int(calculate_crc(bin_list[i], polynomial)) == 0:
            mensagem += utils.bin_to_ascii(bin_list[i][:-4])

        # se o resultado for diferente de 0, logo tem erro e deve ser 
        # guardada a posicao.
        else:
            mensagem += "_"
            erros.append(str(i+1))

    # retornar o dict com mensagem e eventuais erros
    return {"message": mensagem, "erros": erros}


"""
Metodo no qual realiza a codificao para cada caractere da string
retorna uma string em hexa com a codificacao.
"""
def encode(text, polynomial):
    # transforma texto em uma lista de strings de binario
    bin_list = [utils.char_to_bin(c, 7) for c in text]

    # adiciona o bit de paridade em cada letra que são 7 bits
    for i in range(0, len(bin_list)):
        # calcula crc de um caracter com n-1 0s concatenados a direita, 
        # onde n é o tamanho do polinomio gerador
        bin_list[i] += calculate_crc(bin_list[i] + "".zfill(len(polynomial) - 1),  polynomial)

        # converter para hexadecimal.
        bin_list[i] = utils.bin_to_hex(bin_list[i])

    # concatena e retorna o resultado.
    result = "".join(bin_list)

    return result.upper()


if __name__ == "__main__":

    # se o usuario executar python crc.py -e string polinomio_gerador, 
    # executa o encode dessa string
    if sys.argv[1] == '-e':

        string = " ".join(sys.argv[2:-1])
        print(encode(string, sys.argv[-1]))

    # se o usuario executar python crc.py -d hexadecimal polinomio gerador, 
    # executa o decode desse hexadecimal
    if sys.argv[1] == '-d':

        dec = decode(sys.argv[2], sys.argv[3])
        print(dec['message'])

        # se tiver erros, imprima os indices
        if dec['erros']:
            print("ERRO nos caracteres {}".format(', '.join(dec['erros'])))
