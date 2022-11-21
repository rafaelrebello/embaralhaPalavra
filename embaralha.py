"""
Embaralha palavra

Crie um jogo que embaralhe uma palavra e a mostre ao jogador. 
O objetivo é acertar a palavra em até 5 tentativas. 
Informe sempre quantas tentativas ele ainda tem. 
Se ele acertar, dê os parabéns; se errar dê uma palavra de ânimo 
(que mude de forma aleatória). Ao final, mostre a 
palavra correta e o número de tentativas que ele utilizou.

"""

import random
import glob

def cor(cor, texto):
    cores = {
        "P": "\033[95m",
        "B": "\033[94m",
        "G": "\033[92m",
        "Y": "\033[93m",
        "R": "\033[91m",
    }
    return f"{cores.get(cor)}{texto}\033[0m"

listaTemas = glob.glob('Temas/*.txt') 
listaTemas = (x[6:] for x in listaTemas)
dicTema = {x+1:y for x,y in enumerate(listaTemas)}  # cria o dicionário com os temas


def stringTemas():  # obtem a string com temas do dicionário
    temas = [x[0:-4] for x in dicTema.values()]
    strTemas = "Temas: "
    for x, y in enumerate(temas):
        strTemas += f"{x+1}-{y} "
    return cor("P", strTemas)


def selecionarTema():  # seleciona e valida o tema
    while True:
        print(stringTemas())
        intTema = int(input("Selecione o seu tema: "))

        if intTema > 0 and intTema <= len(dicTema):
            print(cor("G", ("Tema selecionado: " + dicTema.get(intTema)[0:-4] + "\n")))
            return intTema

        else:
            print(cor("R", "número inválido"))


def selecionarDificuldade():  # seleciona e valida a dificuldade
    dificuldades = "1 - Fácil / 2 - Intermediário / 3 - Difícil"
    while True:
        print(cor("P", dificuldades))
        intDificuldade = int(input("Selecione a dificuldade: "))

        if intDificuldade > 0 and intDificuldade <= 3:
            dificuldades = dificuldades.split("/")
            print(
                cor(
                    "G",
                    "dificuldade selecionada:"
                    + dificuldades[intDificuldade - 1]
                    + "\n",
                )
            )
            return intDificuldade

        else:
            print(cor("R", "número inválido"))


def embaralha(s):  # função para embaralhar a palavra
    embaralhado = list(s)
    random.shuffle(embaralhado)
    embaralhado = "".join(embaralhado)
    return embaralhado


def obterPalavras(
    intTema, intDificuldade
):  # função para obter a palavra de um arquivo txt
    saida = []
    nomeArq = dicTema.get(intTema)

    with open(nomeArq) as f:
        for line in f:
            saida.append(line.strip())

    return random.choice(saida[(intDificuldade - 1)].split())


palavrasAnimo = {  # frases de ânimo
    1: "Não desista!",
    2: "Continue tentando.",
    3: "Seja persistente!",
    4: "Vamos lá!",
    5: "Tente novamente!",
}

entradaTema = selecionarTema()

entradaDificuldade = selecionarDificuldade()

palavra = obterPalavras(
    entradaTema, entradaDificuldade
).upper()  # palavra a ser descobrida

tentativas = 5  # numero de tentativas

palavraEmbaralhada = embaralha(palavra)
while tentativas > 0: 

    print("Tentativas restantes: ", tentativas)  # mostra o número de tentativas
    print(
        "Palavra para descobrir: " + palavraEmbaralhada
    )  # mostra a palavra embaralhada
    entrada = input("Digite a sua resposta: ")  # recebe a palavra do jogador
    entrada = entrada.upper()  # transforma a entrada em maiúscula

    if entrada == palavra:  # compara o valor recebido com a palavra a ser adivinhada
        print(cor("G", "Parabéns, você acertou"))
        break  # sai do laço de repetição

    print(
        cor("Y", palavrasAnimo.get(random.randint(1, 5)) + "\n")
    )  # dá uma frase de ânimo aleatória para o jogador caso ele erre
    tentativas -= 1  # reduz uma tentativa

if tentativas == 0:
    print(cor("R", "Você perdeu"))
