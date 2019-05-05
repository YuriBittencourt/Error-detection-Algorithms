import random
import crc
import utils
import sys

# testa encode-decode sem erros
if sys.argv[1] == '-n':
    with open(sys.argv[2], "r") as f:
        failures = []
        count = 0
        for line in f:
            count += 1
            try:
                line = line.replace("\n","")
                test = crc.encode(line, sys.argv[3])
                test = crc.decode(test, sys.argv[3])
                assert test['message'] == line

            except AssertionError:
                failures.append(line)

        print("Finished with {}/{} successes".format(count-len(failures),count))
        if len(failures):
            print(','.join(failures))


# testa decode com erros
if sys.argv[1] == '-w':
    pass