"""
Autores: Vinicius Cerutti e Yuri Bittencourt
Trabalho de Introdução a Redes de Computadores 2019/1
"""
import utils
import sys

"""
Metodo que cria um gerador de potencia de 2 inferior ao valor de n

n = limite superior
(2**i)-1 pois como no hamming se trabalha com indices de 1...n e no python 
de 0...n necessita fazer esta adaptacao
"""
def __range_power2__(n):
    i = 0
    while (2**i)-1 <= n:
        yield (2**i)-1
        i+=1 

"""
Metodo que retorna uma lista com indices dos elementos 
que possuem valores iguais a 1
"""
def __get_index_elemt_equals_one__(binary):
    index_list = []
    for i in range (len(binary)):
        if binary[i] == "1":
            index_list.append(utils.int_to_bin(i+1,4))

    return index_list

"""
Metodo que realiza o calculo de codificacao de hamming ou seja recebe um 
sequencia binaria, inverte para ter os indices corretos do algoritmo (0...n),
para cada posicao potencia 2 colocar valores igual a zero para no futuro 
preenche-las. Realiza o xor (paridade) dos indices que possuem valor igual 
a 1 e assim se coloca este bit's gerados nas posicoes de potencia 2, no final 
retorna o binario com estes novos bit's.
"""
def encode_calc_hamming(binary):
    # inverte o binario
    bin_inv = list(binary[::-1])
    # para cada elemento 2^1 colocar 0
    for i in range(len(bin_inv)):
        bin_inv.insert((2**i)-1,"0")
    # pegar os indices que possuem 1
    index_list = __get_index_elemt_equals_one__(bin_inv)
    # pega as colunas de bits
    xor_list = list(map(list,zip(*index_list)))
    # realiza a paridade entre os bits
    xor_list = list(map(utils.parity,xor_list))[::-1]

    for i in range(len(xor_list)):
        # para cada bit gerado do xor por no novo binario
        bin_inv[(2**i)-1] = xor_list[i]

    # converter este binario para hex
    return utils.bin_to_hex("".join(bin_inv[::-1]))

    
"""
Metodo que realiza o calculo de decodificacao de hamming
ou seja recebe um sequencia binária, inverte para ter os indices
corretos do algoritmo (0...n). Realiza-se o xor (paridade) dos indices que 
possuem valor igual a 1 e se este valor gerado for diferente de zero entao
ha bit errado, realiza-se a troca deste bit, remove os bit's dos indices que
sao potencia 2 e retorna o caractere e o valor de erro.
"""
def decode_calc_hamming(binary):
    # inverte o binario
    bin_inv = list(binary[::-1])
    # pegar os indices que possuem 1
    index_list = __get_index_elemt_equals_one__(bin_inv)
    # pega as colunas de bits
    xor_list = list(map(list,zip(*index_list)))
    # realizar a paridade entre os bits
    xor_list = list(map(utils.parity,xor_list))
    # indice errado
    index_error = utils.bin_to_int("".join(xor_list))
    #trocando o bit errado
    if index_error != 0:
        bin_inv[index_error-1] = '1' if bin_inv[index_error-1] == '0' else '0'
    #remove os bits adicionais
    for i in list(__range_power2__(len(bin_inv)))[::-1]:
        bin_inv.pop(i)
    binary = "".join(bin_inv[::-1])
    
    return (utils.bin_to_ascii(binary), index_error)
    

"""
Metodo no qual realiza a codificao para cada caractere da string
retorna uma string em hexa com a codificacao.
"""
def encode(string):
    # converter cada letra para binario
    bin_list = [utils.char_to_bin(letter, 8) for letter in string]
    # de cada binario realizar o hamming
    message_encode = "".join(list(map(encode_calc_hamming,bin_list)))
    return message_encode.upper()

"""
Metodo no qual realiza a decodificao de cada par de hexa, retorna 
a mensagem decodificada e os erros encontrados com a correcao.
"""
def decode(string):
    # converter cada letra para binario
    bin_list = [utils.hex_to_bin(string[i:i+3], 11) for i in range(0,len(string),3) ]
    message = ""
    index_error = []
    for i, binary in enumerate(bin_list):
        #decodifca o binario
        letter, error = decode_calc_hamming(binary)
        message+=letter
        if error != 0:
            index_error.append((letter,i+1))

    return {'message':message, 'index_error': index_error}

if __name__ == '__main__':

    # se o usuario executar python hamming.py -e string,executa o 
    # encode dessa string
    if sys.argv[1] == '-e':
        string = " ".join(sys.argv[2:])
        print(encode(string))

    # se o usuario executar python crc.py -d hexadecimal 
    # executa o decode desse hexadecimal
    if sys.argv[1] == '-d':
        dec = decode(sys.argv[2])
        print(dec['message'])
        for letter, error in dec['index_error']:
            print("ERRO no caractere {} -> Correção: {}".format(error,letter))