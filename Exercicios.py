n = 15

for x in range(1, n+1):
    print(x,'- Exercicio',x)

op = int(input('Selecione qual Exercicio quer rodar:'))

###################
### Exercício 1 ###
###################
if op == 1:
    print("Exercício 1: Soma de A e B = C.")

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
    print("Exercício 2: Valor digitado positivo ou negativo/par ou impar.")

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
    print("Exercício 3: Valores iguais soma, diferentes multiplica.")

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
    print("Exercício 4: Recebe numero e mostra antecessor e sucessor.")

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
    print("Exercício 5: Quantos salarios minimos o usuario recebe.")

    sal_min = 1293.20
    sal_usu = float(input('Digite o seu salário:'))

    qnts = round(sal_usu / sal_min, 2)

    print('Você recebe',qnts,'salários minimos aproximadamente.')

###################
### Exercício 6 ###
###################
elif op == 6:
    print("Exercício 6: Recebe um valor e imprime reajuste de 5%.")

    v1 = int(input('Digite um valor:'))

    rea = ((v1 * 5)/100)

    print('Valor escolhido:', v1)
    print('Reajuste de 5%:', rea)

###################
### Exercício 7 ###
###################
elif op == 7:
    print("Exercício 7: Recebe 2 valores booleans e verifica se são verdadeiros ou falsos")

###################
### Exercício 8 ###
###################
elif op == 8:
    print("Exercício 8: Recebe 3 (fiz com 4 pra teste) valores e imprime em ordem decrescente")

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
    print("Exercício 9: IMC")

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
    print("Exercício 10: Média de um aluno")

    a = float(input('Digite a primeira nota:'))
    b = float(input('Digite a segunda nota:'))
    c = float(input('Digite a terceira nota:'))
    
    m = round((a + b + c) / 3, 1)

    print('Sua média é de:', m)

####################
### Exercício 11 ###
####################
elif op == 11:
    print("Exercício 11: Aluno aprovado ou reprovado")

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