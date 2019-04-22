import sys


def paridade(n):
    if n.count("1") % 2 == 0:
        return "0"
    return "1"


def get_n(n, str_lst):
    new_str = ""
    for item in str_lst:
        new_str += item[n]
    return new_str

text = "redes"
lst = []
for letter in text:
    binario = bin(ord(letter))
    lst.append(binario[2:] + paridade(binario[2:]))

parity = ""
for i in range(0,8):
    parity += paridade(get_n(i, lst))

lst.append(parity)
print(lst)

