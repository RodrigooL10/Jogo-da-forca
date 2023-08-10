import random
#jogo da forca
topo =   "UU=====U"
corda =  "||     |"
cabeca = "||      "
corpo =  "||      "
pernas = "||      "
base1 =  "||"
base2 =  "||"

dica = ""
l = ["_" for _ in range(9)]
palpites = ""
erro = acerto = 0

palavras = ["BATRANGUE", "AEROPORTO", "CONSELHOS"]
dicas = ["Morcego que vai e volta",
         "Local onde podemos viajar",
         "Se fossem bons, não eram de graça"]

#sorteando a palavra
sorteio = random.randint(0,2)
sorteado = palavras[sorteio]
palavra = []

for i in  range(0,9,1):
    palavra.append(sorteado[i:i+1])

dica = dicas[sorteio]

while(acerto < 9 and erro < 6):
    #exibindo a forca
    print()
    print()
    print(dica)
    print()
    print(topo)
    print(corda)
    print(cabeca)
    print(corpo)
    print(pernas)
    print(base1)
    print(base2)
    print(" ",l)
    print(palpites)

    print("Digite uma letra")
    letra = input().upper()
    print()
    print()
    print()
    palpites += " " + letra
    
    #testando se acertou ou errou
    if letra in palavra: 
        for i in range(len(palavra)):
            if letra == palavra[i]:
                acerto += 1
                palavra[0] = "@"
                l[i] = letra
    
    else:
        erro += 1
    
    #arrumando a forca
    if erro == 1:
        cabeca = "||    (ï)"
    elif erro == 2:
        corpo =  "||    {.}"
    elif erro == 3:
        corpo =  "||   /{.}"
    elif erro == 4:
        corpo =  "||   /{.}\\"
    elif erro == 5:
        pernas = "||    /  "
    elif erro == 6:
        pernas = "||    / \  "

#exibindo a forca final
print()
print()
print(dica)
print()
print(topo)
print(corda)
print(cabeca)
print(corpo)
print(pernas)
print(base1)
print(base2)
print(" ",l)
print(palpites)

if acerto >= 9:
    print("Você acertou!")
else:
    print("VocÊ perdeu!")