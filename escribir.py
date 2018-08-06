# -*- coding: utf-8 -*-

def write_function():
    with open('numeros.txt', 'w') as f:
        for i in range(10):
            f.write(str(" {}".format(i)))

def main():
    write_function()

if __name__ == '__main__':
    main()
