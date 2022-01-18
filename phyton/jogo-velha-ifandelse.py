import time

posicao1 = '1'
posicao2 = '2'
posicao3 = '3'
posicao4 = '4'
posicao5 = '5'
posicao6 = '6'
posicao7 = '7'
posicao8 = '8'
posicao9 = '9'

turno = 1

win = 0

contador = 0

while win !=3:

    print(f'''
    | {posicao7} | {posicao8} | {posicao9} |
    | - | - | - |
    | {posicao4} | {posicao5} | {posicao6} |
    | - | - | - |
    | {posicao1} | {posicao2} | {posicao3} |
    | - | - | - |

    ''')

    if posicao1 == 'o' and win !=3 :
        if posicao2 == 'o' and  posicao3 == 'o':
            print(' O 2° jogador  ganhou!!!!!!')
            win = 3
        elif posicao4 == 'o' and posicao7 =='o':
            print(' O 2° jogador  ganhou!!!!!!')
            win = 3
        elif posicao5 == 'o' and posicao9 =='o':
            print(' O 2° jogador  ganhou!!!!!!')
            win = 3
    if posicao2 == 'o' and win !=3:
        if posicao5 == 'o' and posicao8 == 'o':
            print(' O 2° jogador  ganhou!!!!!!')
            win = 3
    if posicao3 == 'o' and win !=3:
        if posicao6 == 'o' and posicao9 == 'o':
            print(' O 2° jogador  ganhou!!!!!!')
            win = 3
        elif posicao5 == 'o' and posicao7 =='o':
            print(' O 2° jogador  ganhou!!!!!!')
            win = 3
    if posicao4 == 'o' and win !=3:
        if posicao5 == 'o' and posicao6 == 'o':
            print(' O 2° jogador  ganhou!!!!!!')
            win = 3
    if posicao7 == 'o' and win !=3:
        if posicao8 == 'o' and posicao9 == 'o':
            print(' O 2° jogador  ganhou!!!!!!')
            win = 3

    if posicao1 == 'x' and win !=3:
        if posicao2 == 'x' and posicao3 == 'x':
            print(' O 1° jogador  ganhou!!!!!!')
            win = 3
        elif posicao4 == 'x' and posicao7 == 'x':
            print(' O 1° jogador  ganhou!!!!!!')
            win = 3
        elif posicao5 == 'x' and posicao9 == 'x':
            print(' O 1° jogador  ganhou!!!!!!')
            win = 3
    if posicao2 == 'x' and win !=3:
        if posicao5 == 'x' and posicao8 == 'x':
            print(' O 1° jogador  ganhou!!!!!!')
            win = 3
    if posicao3 == 'x' and win !=3:
        if posicao6 == 'x' and posicao9 == 'x':
            print(' O 1° jogador  ganhou!!!!!!')
            win = 3
        elif posicao5 == 'x' and posicao7 == 'x':
            print(' O 1° jogador  ganhou!!!!!!')
            win = 3
    if posicao4 == 'x' and win !=3:
        if posicao5 == 'x' and posicao6 == 'x':
            print(' O 1° jogador  ganhou!!!!!!')
            win = 3
    if posicao7 == 'x' and win !=3:
        if posicao8 == 'x' and posicao9 == 'x':
            print(' O 1° jogador  ganhou!!!!!!')
            win = 3
    elif contador == 8:
        print('Empate!!!!')

    if win !=3:

        jogador = str(input(f'  Escolha onde quer jogar {turno}° jogador: '))

        if turno == 1:

            if jogador == '1' and posicao1 == '1':
                posicao1 = 'x'
                turno = 2
                contador = contador + 1

            elif jogador =='2' and posicao2 == '2':
                posicao2 = 'x'
                turno = 2
                contador = contador + 1


            elif jogador =='3' and posicao3 == '3':
                posicao3 = 'x'
                turno = 2
                contador = contador + 1

            elif jogador == '4' and posicao4 == '4':
                posicao4 = 'x'
                turno = 2
                contador = contador + 1

            elif jogador == '5' and posicao5 == '5':
                posicao5 = 'x'
                turno = 2
                contador = contador + 1

            elif jogador == '6' and posicao6 == '6':
                posicao6 = 'x'
                turno = 2
                contador = contador + 1

            elif jogador == '7' and posicao7 == '7':
                posicao7 = 'x'
                turno = 2
                contador = contador + 1

            elif jogador == '8' and posicao8 == '8':
                posicao8 = 'x'
                turno = 2
                contador = contador + 1

            elif jogador == '9' and posicao9 == '9':
                posicao9 = 'x'
                turno = 2
                contador = contador + 1
            else:
                print('  Escolha um valor correspondente. ')
                time.sleep(2)


        elif turno == 2  :
            if  jogador == '1' and posicao1 == '1':
                 posicao1 = 'o'
                 turno = 1
                 contador = contador + 1

            elif jogador =='2' and posicao2 == '2':
                posicao2 = 'o'
                turno = 1
                contador = contador + 1

            elif jogador == '3' and posicao3 == '3':
                posicao3 = 'o'
                turno = 1
                contador = contador + 1

            elif jogador == '4' and posicao4 == '4':
                posicao4 = 'o'
                turno = 1
                contador = contador + 1

            elif jogador == '5' and posicao5 == '5':
                posicao5 = 'o'
                turno = 1
                contador = contador + 1

            elif jogador == '6' and posicao6 == '6':
                posicao6 = 'o'
                turno = 1
                contador = contador + 1

            elif jogador == '7' and posicao7 == '7':
                posicao7 = 'o'
                turno = 1
                contador = contador + 1

            elif jogador == '8' and posicao8 == '8':
                posicao8 = 'o'
                turno = 1
                contador = contador + 1

            elif jogador == '9' and posicao9 == '9':
                posicao9 = 'o'
                turno = 1
                contador = contador + 1
            else:
                print('Escolha um valor correspondente ')
                time.sleep(2)
