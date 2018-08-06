# -*- coding: utf-8 -*-

def cypher(message):
    cyphered = []
    for letter in message:
        binary = bin(ord(letter))
        cyphered.append(binary)

    return''.join(cyphered)

def decypher(message):
    chars = message.split('0b')
    chars.pop(0)

    decyphered = []
    for char in chars:
        decyphered.append(chr(int('0b{}'.format(char), 2)))

    return''.join(decyphered)


def main():
    message = raw_input("ingresa el mensaje:")
    cyphered = cypher(message)
    print("cyphered message: \n{}".format(cyphered))
    decyphered = decypher(cyphered)
    print("Decyphered message: \n{}".format(decyphered))


if __name__ == '__main__':
    main()
