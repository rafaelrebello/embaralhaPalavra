
'''
Embaralha palavra

Crie um jogo que embaralhe uma palavra e a mostre ao jogador. 
O objetivo é acertar a palavra em até 5 tentativas. 
Informe sempre quantas tentativas ele ainda tem. 
Se ele acertar, dê os parabéns; se errar dê uma palavra de ânimo 
(que mude de forma aleatória). Ao final, mostre a 
palavra correta e o número de tentativas que ele utilizou.

'''

import random



dicTema = {  #cria dicionário com os temas
        1: "Animais.txt",
        2: "Frutas.txt",
    }

def stringTemas(): #obtem a string com temas do dicionário
    temas = ([x[0:-4] for x in dicTema.values()])
    strTemas = "Temas: " 
    for x,y in enumerate(temas): strTemas+= (f"{x+1}-{y} ")
    return strTemas

def selecionarTema():
    while True:
        print(stringTemas())
        intTema = int(input("Selecione o seu tema:"))
        if intTema>0 and intTema<=len(dicTema):
            return intTema
        else:
            print("número inválido")

def selecionarDificuldade():
    while True:
        print("1 - Fácil / 2 - Intermediário / 3 - Difícil")
        intDificuldade = int(input("Selecione a dificuldade: "))
        if intDificuldade>0 and intDificuldade<=3:
            return intDificuldade
        else:
            print("número inválido")

def embaralha(s): #função para embaralhar a palavra
    embaralhado = list(s)
    random.shuffle(embaralhado)
    embaralhado = ''.join(embaralhado)
    return embaralhado

def obterPalavras(intTema,intDificuldade): #função para obter a palavra de um arquivo txt
    saida = []
    nomeArq = dicTema.get(intTema)

    with open(nomeArq) as f:
        for line in f:
            saida.append(line.strip())

    return(random.choice(saida[(intDificuldade-1)].split()))



entradaTema = selecionarTema()

entradaDificuldade = selecionarDificuldade()

print("\n")

palavra = obterPalavras(entradaTema,entradaDificuldade).upper() #palavra a ser descobrida

tentativas = 5 #numero de tentativas
palavrasAnimo = { #frases de ânimo
    1:"Não desista!",
    2:"Continue tentando.",
    3:"Seja persistente!",
    4:"Vamos lá!",
    5:"Tente novamente!"
    }

while tentativas > 0:
    palavraEmbaralhada = embaralha(palavra) #palavra a ser descoberta embaralhada

    print("Tentativas restantes: ",tentativas) #mostra o número de tentativas
    print("Palavra para descobrir: "+ palavraEmbaralhada) #mostra a palavra embaralhada
    entrada = input("Digite a sua resposta: ") #recebe a palavra do jogador
    entrada = entrada.upper() #transforma a entrada em maiúscula 
    
    if entrada == palavra: #compara o valor recebido com a palavra a ser adivinhada
        print("Parabéns")
        break #sai do laço de repetição

    print(palavrasAnimo.get(random.randint(1,5))) #dá uma frase de ânimo aleatória para o jogador caso ele erre
    tentativas-= 1 #reduz uma tentativa

if tentativas==0:
    print("Você perdeu")