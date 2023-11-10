import json
import random
from termcolor import colored

# Selecionando o JSON e inserindo na variavel
arquivo = open('palavras.json')
palavra = json.load(arquivo)

# Explicacao sobre o jogo
def explicacao_jogo():
    print("--" * 10 + "TERMO" + "--" * 10)
    print(" Seja bem vindo ao jogo termo, você precisará inserir palavras que contenham 5 letras.")
    print("-As letras marcadas em verde possuem na palavra e estão na posição correta")
    print("-As letras marcadas em amarelo, possuem na palavra mas estão na posição errada")
    print("-As que não estiverem marcadas, não estão na palavra.")

# Inicia o Jogo
def menu_jogo():
    print("-" * 40 )
    print("1 - Iniciar jogo")
    print("2 - Sair")
    escolha_menu = int(input("Escolha uma opção: "))
    if(escolha_menu == 1): 
        gerar_palavra()
    elif(escolha_menu ==2):
        print("Saiu do jogo!")
        exit()

# Seleciona uma palavra do arquivo JSON
def gerar_palavra():
    quantidade_palavras = len(palavra["palavras"])
    num_aletorio = random.randint(1, quantidade_palavras)

    palavra_gerada = palavra["palavras"][num_aletorio]
    format_palavra_gerada = list(palavra_gerada)
    return format_palavra_gerada

def adicionar_palavra():
    palavra_usuario = input("Digite uma Palavra com 5 caracteres: ")
    while (len(palavra_usuario) != 5):
        print("--" * 20)
        print("Valor inválido, por favor tente novamente")
        palavra_usuario = input("Digite uma Palavra com 5 caracteres: ")

    if len(palavra_usuario) == 5: 
        format_palavra_usuario = list(palavra_usuario)
        print(format_palavra_usuario)
    
    return format_palavra_usuario

def verificar_letra(format_palavra_usuario, format_palavra_gerada):
    letras_formatadas = []

        
    for i in range(len(format_palavra_usuario)):
        letra_usuario = format_palavra_usuario[i]
        letra_gerada = format_palavra_gerada[i]

        if letra_usuario == letra_gerada:
            letra_formatada = colored(letra_usuario, 'green')
        else:
            letra_formatada = colored(letra_usuario, 'red')
        letras_formatadas.append(letra_formatada)

    palavra_formatada_str = ''.join(letras_formatadas)
    print(palavra_formatada_str)

    palavra_gerada = gerar_palavra()
    

    while(format_palavra_usuario != format_palavra_gerada):
        adicionar_palavra()

def verificar_palavra():
    if (adicionar_palavra() == gerar_palavra()):
        print("Voce acertou a palavra!!!")
        exit()


def mostrar_letras_usadas():
    pass


def main():
    explicacao_jogo()
    menu_jogo()

    verificar_letra(adicionar_palavra(), gerar_palavra())
    

if __name__ == "__main__":
    main()