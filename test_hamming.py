import random
import hamming
import utils
import sys

def text_generator():
	for k in range(1,12): # tamanho das palavras
		for j in range (0,15): # quanta vezes repetir aqueles numero de caracteres
			word = ""
			for l in range (0,k):# gerar a palavra
				word += chr(random.randint(32, 126))
			print(word)

def file_test_encoding():
    read_data = []
    with open('words_test_hamming.txt') as f:
        read_data = f.readlines()

    read_data = list(map(lambda s: s.rstrip(),read_data))
    
    for data in read_data:
        hamming.encode(data)

def file_test_decoding():
    read_data = []
    with open('inject_problems.txt') as f:
    #with open('data_enconding.txt') as f:
        read_data = f.readlines()

    read_data = list(map(lambda s: s.rstrip(),read_data))
    
    for data in read_data:
        print(data+"aaaa")
        hamming.decode(data)

def inject_problems():
	read_data = []

	with open('data_enconding.txt') as f:
		read_data = f.readlines()

	read_data = list(map(lambda s: s.rstrip(),read_data))

	for data in read_data:
		print(data)
		binary = utils.hex_to_bin(data,0)
		binary = list(binary)
		index_change = random.randint(1, len(binary)-1)
		binary[index_change] = '1' if binary[index_change] == "0" else '0'
		hexa = utils.bin_to_hex("".join(binary))
		print(hexa.upper())
		#print()

if sys.argv[1] == '-i':
    inject_problems()

if sys.argv[1] == '-d':
	file_test_decoding()

if sys.argv[1] == '-e':
	file_test_encoding()

if sys.argv[1] == '-g':
	text_generator()
