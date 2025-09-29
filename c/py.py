import random

numero = random.randint(1, 5000)
palpite = 0

while palpite == numero:
    palpite = int(input("tente adivinhar o numero entre 1 e 5000: "))
    if palpite < numero:
        print("Esta abaixo")
    elif palpite > numero:
        print("Esta acima")
    else:
        print("Acertou")
    