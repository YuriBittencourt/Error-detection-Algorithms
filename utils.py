"""
Autores: Vinicius Cerutti e Yuri Bittencourt
Trabalho de Introdução a Redes de Computadores 2019/1
"""

"""
Metodo que calcula a paridade de n, retorna "1" se impar,
caso contrário retorna "0".
"""
def parity(n):
    if n.count("1") % 2 == 0:
        return "0"
    return "1"

"""
Metodo que converte uma string de caracteres para string de 
binários com padding definido.
"""
def char_to_bin(letter, padding):
    return (bin(ord(letter))[2:]).zfill(padding)

"""
Metodo que converte um inteiro para string de binarios com padding 
definido.
"""
def int_to_bin(number, padding):
    return (bin(number)[2:]).zfill(padding)

"""
Metodo que converte uma string hexadecimal para string de binarios 
com padding definido.
"""
def hex_to_bin(number, padding):
    return bin(int(number, 16))[2:].zfill(padding)

"""
Metodo que converte uma string de binarios para string 
de caracteres ASCII.
"""
def bin_to_ascii(binary):
    return chr(int(binary, 2))

"""
Metodo que converte uma string de binarios para 
string de hexadecimais.
"""
def bin_to_hex(binary):
    return hex(int(binary, 2))[2:]

"""
Metodo que converte uma string de binarios para um inteiro.
"""
def bin_to_int(binary):
	return int(binary,2)