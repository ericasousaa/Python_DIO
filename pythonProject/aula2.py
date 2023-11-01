a = int(input('entre com o primeiro valor: '))
b = int(input('entre com o segundo valor: '))
print(type(a))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a & b
print('soma: {soma}. \nsubtracao: {sub}. '
      '\nmultiplicacao: {multiplicacao} '
      '\ndivisao: {divisao} '
      '\nresto: {resto} '
      .format(soma=soma,
              sub=subtracao,
              divisao=divisao,
              resto=resto,
              multiplicacao=multiplicacao))

