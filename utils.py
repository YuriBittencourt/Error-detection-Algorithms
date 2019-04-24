def parity(n):
    if n.count("1") % 2 == 0:
        return "0"
    return "1"


def to_bin(letter):
    return bin(ord(letter))[2:]


def to_ascii(binary):
    return chr(int(binary, 2))


def bin_to_hex(binary):
    return hex(int(binary, 2))[2:]
