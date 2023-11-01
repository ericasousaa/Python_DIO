a = int(input('primeiro bimestre: '))
if a > 10:
    a = int(input('voce digitou errado. primeiro bimestre: '))
b = int(input('segundo bimestre: '))
if b > 10:
    b = int(input('voce digitou errado. segundo bimestre: '))
c = int(input('terceiro bimestre: '))
if c > 10:
    c = int(input('voce digitou errado. terceiro bimestre: '))
d = int(input('quarto bimestre: '))
if d > 10:
    d = int(input('voce digitou errado. quarto bimestre: '))
media = (a + b + c + d) / 4
print('media: {}'.format(media))
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('media: {}'.format(media))
# else:
#     print('foi informada alguma nota errada')

# a = int(input('primeiro valor: '))
# b = int(input('segundo valor: '))
# c = int(input('terceiro valor: '))
#
# if a > b and a > c:
#     print('o maior número é {}'.format(a))
# elif b > a and b > c:
#     print('o maior número é {}'.format(b))
# else:
#     print('o maior número é {}' .format(c))
# print('final do programa')


# solicita ao usuário o ano de nascimento
ano_nascimento = int(input("Digite o ano do seu nascimento: "))

# calcula a idade com relação a 2023
idade = 2023 - ano_nascimento

# verifica se já fez aniversário esse ano
mes_atual = 5 # mês atual é maio
dia_atual = 1 # dia atual é o primeiro
if mes_atual < 1 or (mes_atual == 1 and dia_atual < 1):
    idade -= 1

# informa a idade calculada
print(f"Sua idade em 2023 é {idade} anos.")