"""
Template file for ECMM462 coursework

Academic Year: 2022/23
Version: 1
Author: Diego Marmsoler
"""

import sys
import re


def encrypt(input, rounds, roundkeys):
    # TODO: Implement encryption of "input" in "rounds" rounds, using round keys "roundkeys"
    # split the input into two values by making a string and then back into an int.
    inputstr = str(input)
    # Left part of the plaintext
    bottom = (inputstr[:len(inputstr) // 2])
    # Right part of the plaintext
    top = (inputstr[len(inputstr) // 2:])

    for i in range(rounds):
        print(i, 'Round key used:', roundkeys[i])
        print(i, 'bottom plaintext:', bottom)
        print(i, 'top plaintext:', top)

        # AND operation with the top value and KEY
        topx = ''
        for x in range(4):
            if top[x] == '0' or roundkeys[i][x] == '0':
                topx += "0"
            else:
                topx += "1"
        #top = topx
        print(i, 'After Bitwise AND :', topx)

        # XOR operation with bottom and values from AND
        bottomx = ''
        for x in range(4):
            if bottom[x] == topx[x]:
                bottomx += "0"
            else:
                bottomx += "1"
        print(i, 'After Bitwise XOR:', bottomx)

        bottom = bottomx
        top, bottom = bottom, top
        print(i, 'So we have', bottom, top)


    # SWAP values
    top, bottom = bottom, top
    print(i, 'After Swap: ', bottom, top)

    return bottom, top


def decrypt(input, rounds, roundkeys):
    # TODO: Implement decryption of "input" in "rounds" rounds, using round keys "roundkeys"
    # split the input into two values by making a string and then back into an int.
    inputstr = str(input)
    # Left part of the plaintext
    bottom = (inputstr[:len(inputstr) // 2])
    # Right part of the plaintext
    top = (inputstr[len(inputstr) // 2:])
    roundkeys.reverse()


    for i in range(rounds):
        print(i, 'Round key used:', roundkeys[i])
        print(i, 'bottom plaintext:', bottom)
        print(i, 'top plaintext:', top)

        # AND operation with the top value and KEY
        topx = ''
        for x in range(4):
            if top[x] == '0' or roundkeys[i][x] == '0':
                topx += "0"
            else:
                topx += "1"
        # top = topx
        print(i, 'After Bitwise AND :', topx)

        # XOR operation with bottom and values from AND
        bottomx = ''
        for x in range(4):
            if bottom[x] == topx[x]:
                bottomx += "0"
            else:
                bottomx += "1"
        print(i, 'After Bitwise XOR:', bottomx)

        bottom = bottomx
        top, bottom = bottom, top
        print(i, 'So we have', bottom, top)

    # SWAP values
    top, bottomx = bottomx, top
    print(i, 'After Swap: ', bottom, top)

    return bottom, top


opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

c = re.compile('^[01]{8}$')
try:
    input = args.pop(0)
except IndexError:
    raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")
if not c.search(input):
    raise SystemExit("input is not a valid bit string")

try:
    rounds = int(args.pop(0))
except IndexError:
    raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")
except ValueError:
    raise SystemExit("rounds is not a valid number")

if (len(args) < rounds):
    raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")

roundkeys = args
c = re.compile('^[01]{4}$')
if not all(c.search(elem) for elem in roundkeys):
    raise SystemExit("round key is not a valid bit string")

if "-d" in opts:
    result = decrypt(input, rounds, roundkeys)
else:
    result = encrypt(input, rounds, roundkeys)

print(result)
