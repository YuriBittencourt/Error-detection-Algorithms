import sys
import utils


def get_n(n, str_lst):
    new_str = ""
    for item in str_lst:
        new_str += item[n]
    return new_str

text = "redes"
lst = []
for letter in text:
    binario = utils.to_bin(letter)
    lst.append(binario + utils.paridade(binario))

parity = ""
for i in range(0,8):
    parity += utils.paridade(get_n(i, lst))

lst.append(parity)
print(lst)


#if(sys.argv[1] == '-e'):
#    '''ENCODE'''

#if(sys.argv[1] == '-d'):
#    '''DECODE'''