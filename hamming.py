import utils

# n = limite superior
def range_power2(n):
    i = 0
    print(n)
    while (2**i)-1 <= n:
        yield (2**i)-1
        i+=1 

def calc_hamming(binary):
    # inverte o binario
    bin_inv = list(binary[::-1])
    print(bin_inv)
    # para cada elemento 2^1 colocar 0
    for i in range_power2(len(bin_inv)):
        #print(i)
        bin_inv.insert(i,"0")
    
    print(bin_inv)
    # pegar os indices que possuem 1
    # converter estes itens para binario
    # realizar a paridade entre os bits
    # para cada bit gerado do xor por no novo binario
    # converter este binario para hex

def encode(string):
    # converter cada letra para binario
    bin_list = list(map(utils.to_bin,string))
    print(bin)
    # de cada binario realizar o hamming

    # resultado do final de cada caractere binario 
    # converter para hex

calc_hamming("1110010")

