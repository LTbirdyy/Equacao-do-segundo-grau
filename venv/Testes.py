from math import sqrt
print('Forneça os valores')
a = int(input('Valor de A:'))
b = int(input('Valor de b:'))
c = int(input('Valor de c:'))
#sinais
sinal = ''
sinal_dois = ''
if b > 0:
    sinal = '+'
if c > 0:
    sinal_dois = '+'
#equação
if c == 0:
    if a == 1 and b != 1:
        print(f'A sua equação é:\033[32mx²{sinal}{b}x{sinal_dois}=0\033[0m')
    elif b == 1 and a != 1:
        print(f'A sua equação é:\033[32m{a}x²{sinal}x{sinal_dois}=0\033[0m')
    elif a == 1 and b == 1:
        print(f'A sua equação é:\033[32mx²{sinal}x{sinal_dois}=0\033[0m')
elif a == 1 and b != 1:
    print(f'A sua equação é:\033[32mx²{sinal}{b}x{sinal_dois}{c}=0\033[0m')
elif b == 1 and a != 1:
    print(f'A sua equação é:\033[32m{a}x²{sinal}x{sinal_dois}{c}=0\033[0m')
elif a == 1 and b == 1:
    print(f'A sua equação é:\033[32mx²{sinal}x{sinal_dois}{c}=0\033[0m')
else:
    print(f'A sua equação é:\033[32m{a}x²{sinal}{b}x{sinal_dois}{c}=0\033[0m')
#delta
delta = (b**2) - (4*a*c)
print(f'O valor do delta é:\033[32m{delta}\033[0m')
#resultados
#DELTA = 0
if delta == 0:
    resposta_1 = (-b + sqrt(delta))/(2 * a)
    print(f'A resposta é \033[32m{resposta_1:.1f}\033[0m')
#DELTA > 0
elif delta > 0:
    resposta_1 = (-b + sqrt(delta))/(2 * a)
    resposta_2 = (-b - sqrt(delta))/(2 * a)
    print(f'Como o delta é maior que zero existe duas respostas, sendo elas (\033[32m{resposta_1:.1f},{resposta_2:.1f}\033[0m)')
#DELTA < 0
else:
    numero_complexo = sqrt(abs(delta))/(2 * a)
    resposta_1 = (-b)/(2 * a)
    resposta_2 = (-b)/(2 * a)
    if numero_complexo == 0 or numero_complexo == 1:
        numero_complexo = ''
    print(f'Como o delta deu menor que zero as respostas estarão em números complexos sendo eles:\n'
          f'{resposta_1:.1f}+{numero_complexo}i e a segunda resposta é {resposta_2:.1f}-{numero_complexo}i')
    print(f'{numero_complexo}')