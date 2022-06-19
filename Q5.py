'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;
'''


def reverse(word):
    word = list(word)
    halfString = len(word)//2

    for index in range (0, halfString):
        tmp = word[index]
        word[index] = word[-index - 1]
        word[-index - 1] = tmp
    
    return ("".join(word))
    
word = input("Digite uma string: ")
word = reverse(word)
print(f'String invertida: {word}')