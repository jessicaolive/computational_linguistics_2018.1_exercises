# regverbs.py
# coding: utf-8
# Program that informs the pronounciation of the final 'ed' of English regular verbs in the past
# Programa que informa a pronúncia do 'ed' final de verbos regulares no passado em língua inglesa
# por: Adonis Sousa, Brenda Souza, Juliana Gurgel, Pedro Muniz

def main():
    text: str = input("Type a regular verb in the past: ")
    if len(text) > 2 and text[-2:] == "ed":
        for _ in text:  # type: str
            if text[-3:-2] == "k" or text[-3:-2] == "p" or text[-3:-2] == "s" or text[-3:-2] == "h" or text[-3:-2] == "f":
                print("The final 'ed' sound is /t/")
                break;
            elif text[-3:-2] == "i" or text[-3:-2] == "y" or text[-3:-2] == "l" or text[-3:-2] == "n" or text[-3:-2] == "m" or text[-3:-2] == "r" or text[-3:-2] == "g" or text[-3:-2] == "w" or text[-3:-2] == "z" or text[-3:-2] == "e" or text[-3:-2] == "b" or text[-3:-2] == "v":
                print("The final 'ed' sound is /d/")
                break;
            elif text[-3:-2] == "t" or text[-3:-2] == "d":
                print("The final 'ed' sound is /Id/")
                break;
            else:
                print("Not found/Not a regular verb")
                break;
    else:
        print("Not found/Not a regular verb")

main()

def sequence():
    question = input("Would you like to continue? [yes/no]: ")
    while question in "yes":
        main()
        sequence()
    if question not in "yes":
        exit()

sequence()

# Ainda precisamos resolver três problemas principais:
# 1. Inputs com dois ou menos caracteres (exs: bl, 22, l1, 1) causam um erro.
# 1. Inputs do tipo "exitoo" são tratados como verbos regulares (ele dá a resposta Id).
# 2. Como fazer com que o usuário possa sair do programa (minha tentativa de else: exit() não funcionou)
