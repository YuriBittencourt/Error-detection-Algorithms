import random
import crc
import utils
import sys

#teste sem erros
if sys.argv[1] == '-n':
    with open(sys.argv[2], "r") as f:
        for line in f:
            try:
                line = line.replace("\n","")
                test = crc.encode(line, sys.argv[3])
                test = crc.decode(test, sys.argv[3])
                assert test['message'] == line
                print(line, 'success')

            except AssertionError:
                print(line, 'failure')

