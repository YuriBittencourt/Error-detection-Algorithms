import utils
import sys

# n = limite superior
# -1 pois como no hamming se trabalha com indices de 1...n
# e no python de 0...n necessita fazer esta adaptacao
def __range_power2__(n):
    i = 0
    while (2**i)-1 <= n:
        yield (2**i)-1
        i+=1 

def __get_index_elemt_equals_one__(binary):
    index_list = []
    for i in range (len(binary)):
        if binary[i] == "1":
            # converter estes itens para binario
            index_list.append(utils.int_to_bin(i+1,4))
    return index_list


def encode_calc_hamming(binary):
    # inverte o binario
    bin_inv = list(binary[::-1])
    #print(len(bin_inv))
    # para cada elemento 2^1 colocar 0
    for i in range(len(bin_inv)):
        bin_inv.insert((2**i)-1,"0")
    # pegar os indices que possuem 1
    index_list = __get_index_elemt_equals_one__(bin_inv)
    # pega as colunas de bits
    xor_list = list(map(list,zip(*index_list)))
    # realizar a paridade entre os bits
    xor_list = list(map(utils.parity,xor_list))[::-1]

    for i in range(len(xor_list)):
        # para cada bit gerado do xor por no novo binario
        bin_inv[(2**i)-1] = xor_list[i]

    # converter este binario para hex
    return utils.bin_to_hex("".join(bin_inv[::-1]))

    

def decode_calc_hamming(binary):
    # inverte o binario
    bin_inv = list(binary[::-1])
    #print(len(bin_inv))
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
    #removendo os bits adicionais
    for i in list(__range_power2__(len(bin_inv)))[::-1]:
        bin_inv.pop(i)
    binary = "".join(bin_inv[::-1])
    return (utils.bin_to_ascii(binary), index_error)
    

def encode(string):
    # converter cada letra para binario
    bin_list = [utils.char_to_bin(letter, 8) for letter in string]
    message_encode = ""
    for binary in bin_list:
        # de cada binario realizar o hamming
        message_encode += encode_calc_hamming(binary)

    return message_encode.upper()

def decode(string):
    # converter cada letra para binario
    bin_list = [utils.hex_to_bin(string[i:i+3], 11) for i in range(0,len(string),3) ]
    message = ""
    erros = []
    for binary in bin_list:
        letter, error = decode_calc_hamming(binary)
        message+=letter
        if error != 0:
            erros.append((letter,error))

    return {'message':message, 'erros': erros}
"""
encode("maxprint celular telefone 1928312 ,. ! # awidd")
print(utils.hex_to_bin("6676067CB78079964D6797AA28261F62C6607AD6606067992827AA62C66062C63267E67962C28230434F31A34831D30431A2822E32FA28228528229C2826067B464D62B62B",0))
decode("6676067CB78079964D6797AA28261F62C6607AD6606067992827AA62C66062C63267E67962C28230434F31A34831D30431A2822E32FA28228528229C2826067B464D62B62B")
for i in range (0,len(b)):
    aux = b[:]
    aux[i] = '1' if aux[i] == '0' else '0'
    string = "".join(aux)
    decode(utils.bin_to_hex(string))
"""
# codificação com problemas
#853513047F8
#E229B356
#FC5366354FC7D530462C
#853513047F8
#9D2CE618
#CE4B732E
#857CB7B45312D063264A

if sys.argv[1] == '-e':
    print(encode(sys.argv[2]))

if sys.argv[1] == '-d':
    dec = decode(sys.argv[2])
    print(dec['message'])
    for letter, error in dec['erros']:
        print("ERRO no caractere {} -> Correção: {}".format(dec['message'].index(letter)+1,letter))