import datetime

n = 15

for x in range(1, n+1):
    print(x,'- Exercicio',x)

op = int(input('\nSelecione qual Exercicio quer rodar: '))

###################
### Exercício 1 ###
###################
if op == 1:
    print("\nExercício 1: Soma de A e B = C.\n")

    A = int(input('Digite o Valor de A: '))
    B = int(input('Digite o Valor de B: '))
    C = int(input('Digite o Valor de C: '))

    soma = A + B

    if soma > C:
        print('A soma entre A e B é:', soma)
        print('C é igual a:', C)
        print('A soma é maior do que C')
    else:
        print('A soma entre A e B é:', soma)
        print('C é igual a:', C)
        print('A soma não é maior do que C')

###################
### Exercício 2 ###
###################
elif op == 2:
    print("\nExercício 2: Valor digitado positivo ou negativo/par ou impar.\n")

    v1 = int(input('Digite um valor: '))

    if v1 > 0:
        print('O valor digitado é positivo!')
    elif v1 < 0:
        print('O valor digitado é negativo!')
    else:
        print('O valor digitado é neutro!')

    if v1 % 2 == 0:
        print('O número',v1,'é par!')
    else:
        print('O número',v1,'é ímpar!')

###################
### Exercício 3 ###
###################
elif op == 3:
    print("\nExercício 3: Valores iguais soma, diferentes multiplica.\n")

    A = int(input('Digite o Valor de A: '))
    B = int(input('Digite o Valor de B: '))

    if A == B:
        C = A + B
        print('Os valores são iguais então a soma é:', C)
    else:
        C = A * B
        print('Os valores são diferentes então a multiplicação destes é:', C)

###################
### Exercício 4 ###
###################
elif op == 4:
    print("\nExercício 4: Recebe numero e mostra antecessor e sucessor.\n")

    n1 = int(input('Digite o número desejado: '))

    ant = n1 - 1
    suc = n1 + 1

    print('Número digitado:', n1)
    print('Antecessor do número:', ant)
    print('Sucessor do número:', suc)

###################
### Exercício 5 ###
###################
elif op == 5:
    print("\nExercício 5: Quantos salarios minimos o usuario recebe.\n")

    sal_min = 1293.20
    sal_usu = float(input('Digite o seu salário:'))

    qnts = round(sal_usu / sal_min, 2)

    print('Você recebe',qnts,'salários minimos aproximadamente.')

###################
### Exercício 6 ###
###################
elif op == 6:
    print("\nExercício 6: Recebe um valor e imprime reajuste de 5%.\n")

    v1 = int(input('Digite um valor:'))

    rea = ((v1 * 5)/100)

    print('Valor escolhido:', v1)
    print('Reajuste de 5%:', rea)

###################
### Exercício 7 ###
###################
elif op == 7:
    print("\nExercício 7: Recebe 2 valores booleans e verifica se são verdadeiros ou falsos\n")

###################
### Exercício 8 ###
###################
elif op == 8:
    print("\nExercício 8: Recebe 3 (fiz com 4 pra teste) valores e imprime em ordem decrescente\n")

    A = int(input('Digite o primeiro valor:'))
    B = int(input('Digite o segundo valor:'))
    C = int(input('Digite o terceiro valor:'))
    D = int(input('Digite o quarto valor:'))

    valores = [A, B, C, D]
    valores.sort(reverse=True)

    print("Ordem decrescente:", valores)

###################
### Exercício 9 ###
###################
elif op == 9:
    print("\nExercício 9: IMC\n")

    peso = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))
    
    imc = round(peso/(altura**2), 1)

    if imc < 18.5:
        print('IMC:', imc)
        print('Abaixo do peso!')
    elif imc > 18.6 and imc < 24.9:
        print('IMC:', imc)
        print('Peso ideal, parabéns!')
    elif imc > 25.0 and imc < 29.9:
        print('IMC:', imc)
        print('Levemente acima do peso!')
    elif imc > 30.0 and imc < 34.9:
        print('IMC:', imc)
        print('Obesidade grau 1!')
    elif imc > 35.0 and imc < 39.9:
        print('IMC:', imc)
        print('Obesidade grau 2! (Severa)')
    elif imc >= 40.0:
        print('IMC:', imc)
        print('Obesidade grau 3! (Mórbida)')
    else:
        print('Valores incorretos!')


####################
### Exercício 10 ###
####################
elif op == 10:
    print("\nExercício 10: Média de um aluno\n")

    a = float(input('Digite a primeira nota:'))
    b = float(input('Digite a segunda nota:'))
    c = float(input('Digite a terceira nota:'))
    
    m = round((a + b + c) / 3, 1)

    print('Sua média é de:', m)

####################
### Exercício 11 ###
####################
elif op == 11:
    print("\nExercício 11: Aluno aprovado ou reprovado\n")

    a = float(input('Digite a primeira nota:'))
    b = float(input('Digite a segunda nota:'))
    c = float(input('Digite a terceira nota:'))
    d = float(input('Digite a quarta nota:'))
    
    m = round((a + b + c + d) / 4, 1)

    if m <= 6.9:
        print('Média final:', m)
        print('Aluno reprovado!')
    elif m >= 7.0:
        print('Média final:', m)
        print('Aluno aprovado!')
    else:
        print('Valores incorretos!')

####################
### Exercício 12 ###
####################
elif op == 12:
    print("\nExercício 12: Caixa de mercado")

    v = float(input('\nDigite o valor do produto: '))
    FP = int(input('\nEscolha a forma de pagamento: \n1- A vista(Dinheiro ou Pix) \n2- A vista(Crédito) \n3- Parcelado em até 2x sem juros \n4- Parcelado em 3x ou mais com juros\n\n'))

    if FP == 1:
        desconto = round(v * 0.15, 2)
        v = v - desconto
        print('A vista em dinheiro ou pix recebe 15% de desconto, valor a pagar:', v)
    elif FP == 2:
        desconto = round(v * 0.10, 2)
        v = v - desconto
        print('A vista no cartão de crédito recebe 10% de desconto, valor a pagar:', v)
    elif FP == 3:
        print('Parcelado em 2x no cartão preço normal sem juros, valor a pagar:', v)
    elif FP == 4:
        juros = round(v * 0.10, 2)
        v = v + juros
        print('Parcelado em 3x ou mais no cartão com 10% de juros, valor a pagar:', v)
    else:
        print('Valor incorreto')

####################
### Exercício 13 ###
####################
elif op == 13:
    print("\nExercício 13: Receber nome e idade e dizer se é maior ou menor de idade\n")

    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))

    if idade >= 18 and idade > 0 and idade < 100:
        print(f'\nOlá {nome}! Você tem {idade} anos, portanto você é maior de idade!\n')
    elif idade <= 17 and idade > 0 and idade < 100:
        print(f'\nOlá {nome}! Você tem {idade} anos, portanto você é menor de idade!\n')
    elif idade < 0 or idade > 100:
        print('\nIdade fora dos padrões')
    else:
        print('\nEntrada incorreta')

####################
### Exercício 14 ###
####################
elif op == 14:
    print("\nExercício 14: Receber 2 valores e inverte-los\n")

    A = int(input('Digite o valor de A: '))
    B = int(input('Digite o valor de B: '))

    A, B = B, A

    print(f'\nValor de A: {A}')
    print(f'Valor de B: {B}\n')

####################
### Exercício 15 ###
####################
elif op == 15:
    print("\nExercício 15: Anos, meses e dias de vida de uma pessoa (365 dias e 30 dias no mes)\n")

    nasc = int(input('Digite o ano em que você nasceu: '))
    ano_atual = datetime.date.today().year

    anos = ano_atual - nasc
    meses = anos * 12
    dias = anos * 365

    print(f'Anos: {anos}, Meses: {meses}, Dias: {dias}')