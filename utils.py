def parity(n):
    if n.count("1") % 2 == 0:
        return "0"
    return "1"


def char_to_bin(letter, padding):
    return (bin(ord(letter))[2:]).zfill(padding)


def int_to_bin(number, padding):
    return (bin(number)[2:]).zfill(padding)


def to_ascii(binary):
    return chr(int(binary, 2))


def bin_to_hex(binary):
    return hex(int(binary, 2))[2:]
