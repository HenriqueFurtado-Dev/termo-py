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