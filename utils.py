"""
Método que calcula a paridade de n, retorna "1" se ímpar, caso contrário retorna "0".
"""
def parity(n):
    if n.count("1") % 2 == 0:
        return "0"
    return "1"

"""
Método que converte uma string de caracteres para string de binários com padding definido.
"""
def char_to_bin(letter, padding):
    return (bin(ord(letter))[2:]).zfill(padding)

"""
Método que converte um inteiro para string de binários com padding definido.
"""
def int_to_bin(number, padding):
    return (bin(number)[2:]).zfill(padding)

"""
Método que converte uma string hexadecimal para string de binários com padding definido.
"""
def hex_to_bin(number, padding):
    return bin(int(number, 16))[2:].zfill(padding)

"""
Método que converte uma string de binários para string de caracteres ASCII.
"""
def bin_to_ascii(binary):
    return chr(int(binary, 2))

"""
Método que converte uma string de binários para string de hexadecimais.
"""
def bin_to_hex(binary):
    return hex(int(binary, 2))[2:]

"""
Método que converte uma string de binários para um inteiro.
"""
def bin_to_int(binary):
	return int(binary,2)