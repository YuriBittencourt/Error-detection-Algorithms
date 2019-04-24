def parity(n):
    if n.count("1") % 2 == 0:
        return "0"
    return "1"


def char_to_bin(letter):
    return bin(ord(letter))[2:]

def int_to_bin(number,size):
    return bin(letter)[2:].zfill(size)


def to_ascii(binary):
    return chr(int(binary, 2))


def bin_to_hex(binary):
    return hex(int(binary, 2))[2:]
