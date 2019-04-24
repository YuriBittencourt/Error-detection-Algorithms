import utils

# n = limite superior
# -1 pois como no hamming se trabalha com indices de 1...n
# e no python de 0...n necessita fazer esta adaptacao
def __range_power2__(n):
    i = 0
    while (2**i)-1 <= n:
        yield (2**i)-1
        i+=1 

def calc_hamming(binary):
    # inverte o binario
    bin_inv = list(binary[::-1])

    # para cada elemento 2^1 colocar 0
    for i in __range_power2__(len(bin_inv)):
        bin_inv.insert(i,"0")
    # pegar os indices que possuem 1
    index_list = []
    for i in range (len(bin_inv)):
        if bin_inv[i] == "1":
             # converter estes itens para binario
            index_list.append(utils.int_to_bin(i+1,4))

    # pega as colunas de bits
    xor_list = list(map(list,zip(*index_list)))
    # realizar a paridade entre os bits
    xor_list = list(map(utils.parity,xor_list))[::-1]

    for i in range(len(xor_list)):
        # para cada bit gerado do xor por no novo binario
        bin_inv[(2**i)-1] = xor_list[i]

    # converter este binario para hex
    return utils.bin_to_hex("".join(bin_inv[::-1]))

    
    

def encode(string):
    # converter cada letra para binario
    bin_list = list(map(utils.char_to_bin,string))
    message_encode = ""
    for binary in bin_list:
        message_encode += calc_hamming(binary)
    return message_encode.upper()
    # de cada binario realizar o hamming


a = encode("redes")
print(a)

