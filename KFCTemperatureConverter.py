from time import sleep
tipo_medida = [('Fahrenheit', 'º F'), ('Celsius', 'º C'), ('Kelvin', ' K')]
print('==============================================================')
print('=-= Bem vindo ao conversor KFC - Kelvin/Fahrenheit/Celsius =-=')
print('==============================================================')
sleep(1)

while True:
    while True:
        index_medida = int(input('''De qual temperatura você tem o valor?
[1] Fahrenheit
[2] Celsius
[3] Kelvin
> ''')) - 1
        if 0 <= index_medida <= 2:
            break
        else:
            print('Opção invalida, tente novamente!')
    while True:
        output_medida = int(input('''E para qual temperatura deseja converter?
[1] Fahrenheit
[2] Celsius
[3] Kelvin
> ''')) - 1
        if 0 <= output_medida <= 2 and output_medida != index_medida:
            break
        else:
            print('Opção invalida, tente novamente!')
    valor_usuario = float(input(f'Qual a temperatura em {tipo_medida[index_medida][0]}? > '))

    if index_medida == 0: #F
        if output_medida == 1: #F-C
            calculo = (valor_usuario - 32) / 1.8
        else: #F-K
            calculo = (valor_usuario + 459.67) * 5/9
    elif index_medida == 1: #C
        if output_medida == 0: #C-F
            calculo = (valor_usuario * 1.8) + 32
        else: #C-K
            calculo = valor_usuario + 273.15
    else: #K
        if output_medida == 0: #K-F
            calculo = valor_usuario * 9 / 5 - 459.67
        else: #K-C
            calculo = valor_usuario - 273.15

    print(f'{valor_usuario}{tipo_medida[index_medida][1]} fica {calculo:.2f}{tipo_medida[output_medida][1]}')
    index_medida = output_medida = None
    while True:
        continuar = int(input('''Deseja continuar?
[1] Sim
[2] Não
> '''))
        if 1<=continuar<=2:
            break
    if continuar == 2:
        print('''
     Até a próxima!
              

      Bruno Soares
https://linktr.ee/darkun''')
        sleep(5)
        break