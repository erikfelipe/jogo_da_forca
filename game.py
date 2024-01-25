import random
from IPython.display import clear_output

with open('arquivos/palavras_jogo.txt', 'r') as fileWords:
    words = fileWords.read().split()

resposta = random.choice(words)
acerto = False

dict_letras = {}
dict_underl = {}
tentativas = 5

for i in range(len(resposta)):
    dict_letras[i] = resposta[i]
    dict_underl[i] = '_'

while not acerto and tentativas > 0:
    print('\nTentativas restantes: ' + str(tentativas))
    
    for underl in dict_underl.values():
        print(underl, end=' ')
    
    inputLetra = input('\n\nDigite uma letra: ')
    
    letra_encontrada = False
    
    # Verifica se a letra existe e insere a letra na resposta
    for k, v in dict_letras.items():
        if inputLetra == v:
            dict_underl[k] = inputLetra
            letra_encontrada = True
    
    if letra_encontrada:
        print('\nVocê acertou a letra!')
    else:
        print('\nNão existe essa letra! Tente novamente!!')
        tentativas -= 1
        if tentativas == 0:
            print('\nVocê perdeu!! A palavra era: ' + resposta)
            break
    
    clear_output()
    
    if ''.join(dict_underl.values()) == resposta:
        print('\nVocê acertou a palavra!')
        acerto = True
