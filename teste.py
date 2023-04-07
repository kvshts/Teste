# Resposta 1)
# O valor final da variavel SOMA sera 91. Isso ocorre porque o loop while adiciona cada numero inteiro de 1 a 13 (ou seja, 1 + 2 + 3 + ... + 13), que soma um total de 91.

# Segue abaixo o codigo em Python para calcular a sequencia de Fibonacci e verificar se um numero est presente na sequencia:

def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        return True
    else:
        return False

num = int(input("Digite um numero: "))
if fibonacci(num):
    print("O numero", num, "esta presente na sequencia de Fibonacci.")
else:
    print("O numero", num, "nao esta presente na sequencia de Fibonacci.")

# Este programa solicita ao usuario um numero e, em seguida, verifica se ele esta presente na sequencia de Fibonacci, usando um loop while para calcular a sequencia ate o numero ser maior ou igual ao numero informado pelo usuario. Se o numero estiver presente na sequencia, uma mensagem eh exibida indicando isso. Caso contrario, uma mensagem eh exibida indicando que o numero nao esta presente na sequencia.

# 2)a) A logica eh adicionar 2 ao numero anterior. O proximo elemento eh 9.

# Codigo em Python:
a = [1, 3, 5, 7]
prox_elemento_a = a[-1] + 2
print(prox_elemento_a)

# b) A logica eh multiplicar por 2 o numero anterior. O proximo elemento eh 128.

# Codigo em Python:
b = [2, 4, 8, 16, 32, 64]
prox_elemento_b = b[-1] * 2
print(prox_elemento_b)

# c) A logica eh elevar ao quadrado o indice da posicao (comecando em 0) do numero na sequencia. O proximo elemento eh 49.

# Codigo em Python:
c = [0, 1, 4, 9, 16, 25, 36]
prox_elemento_c = (len(c))**2
print(prox_elemento_c)

# A logica eh elevar ao quadrado o numero anterior. O proximo elemento eh 100.

# Codigo em Python:
d = [4, 16, 36, 64]
prox_elemento_d = d[-1]**2
print(prox_elemento_d)

# e) Alogica eh somar os dois numero anterior. O proximo elemento eh 13.

# Codigo em Python:
e = [1, 1, 2, 3, 5, 8]
prox_elemento_e = e[-1] + e[-2]
print(prox_elemento_e)

# f) A logica ehque os numero da sequencia representam as posicoes das vogais na palavra "dois". O proximo elemento eh 20.

# Codigo em Python:
f = [2, 10, 12, 16, 17, 18, 19]
prox_elemento_f = 20
print(prox_elemento_f)

# 3)Para resolver esse problema, podemos primeiro calcular quanto tempo cada veiculo leva para chegar ao ponto de cruzamento na rodovia. Depois, podemos calcular qual a distancia que cada veiculo percorreu ate chegar nesse ponto, e entao determinar qual veiculo esta mais proximo de Ribeirao Preto.

# Considerando a distancia entre Ribeirao Preto e Franca como 100 km e as velocidades constantes do carro e do caminhao de 110 km/h e 80 km/h, respectivamente, podemos calcular o tempo que cada veiculo leva para chegar ao ponto de cruzamento usando a formula:

tempo = distancia / velocidade

# Para o carro:

tempo_carro = 100 km / 110 km/h
tempo_carro = 0,9091 horas

# Para o caminhao, precisamos levar em consideracao os pedagios que ele precisa passar. Se o caminhao leva 5 minutos a mais para passar em cada pedagio, podemos adicionar 10 minutos (ou 1/6 de hora) ao tempo total do caminhao. Assim, o tempo que o caminhao leva para chegar ao ponto de cruzamento eh:

tempo_caminhao = 100 km / 80 km/h + 1/6 hora
tempo_caminhao = 1,4167 horas

# Agora podemos calcular a distancia que cada veiculo percorreu ate chegar ao ponto de cruzamento:

distancia_carro = tempo_carro * 110 km/h
distancia_carro = 99,999 km (aproximando para 3 casas decimais)

distancia_caminhao = tempo_caminhao * 80 km/h
distancia_caminhao = 113,333 km (aproximando para 3 casas decimais)

# Portanto, quando os veiculos se cruzarem na rodovia, o carro estara mais proximo de Ribeirao Preto, pois percorreu uma distancia menor ate chegar ao ponto de cruzamento.
# Segue abaixo o codigo em Python para calcular qual veiculo esta mais proximo de Ribeirao Preto:

distancia_total = 100  # km
velocidade_carro = 110  # km/h
velocidade_caminhao = 80  # km/h
tempo_carro = distancia_total / velocidade_carro
tempo_caminhao = distancia_total / velocidade_caminhao + 1/6  # 1/6 de hora para cada pedagio
distancia_carro = tempo_carro * velocidade_carro
distancia_caminhao = tempo_caminhao * velocidade_caminhao

if distancia_carro < distancia_caminhao:
    print("O carro esta mais proximo de Ribeirao Preto.")
else:
    print("O caminhao esta mais proximo de Ribeirao Preto.")

# Nesse codigo, definimos as variaveis distancia_total, velocidade_carro e velocidade_caminhao com os valores das distancias e velocidades do problema. Em seguida, calculamos o tempo que cada veiculo leva para chegar ao ponto de cruzamento na rodovia, adicionando o tempo extra dos pedagios para o caminhao. Depois, calculamos a distancia que cada veiculo percorre ate chegar ao ponto de cruzamento e comparamos para determinar qual veiculo esta mais proximo de Ribeirao Preto. Por fim, imprimimos a resposta na tela.

# 4)Segue abaixo um exemplo de codigo em Python que inverte os caracteres de uma string:

# Definindo a string a ser invertida
texto = "Eu amo programar em Python!"

# Convertendo a string para uma lista de caracteres
lista_chars = list(texto)

# Invertendo a ordem dos caracteres na lista
lista_chars.reverse()

# Convertendo a lista de volta para uma string
texto_invertido = ''.join(lista_chars)

# Imprimindo o resultado
print(texto_invertido)

# Nesse codigo, primeiro definimos a string texto que queremos inverter. Em seguida, convertemos a string para uma lista de caracteres, utilizando a funcao list(). Na linha seguinte, utilizamos o metodo reverse() da lista para inverter a ordem dos caracteres. Por fim, utilizamos o metodo join() para unir os caracteres da lista de volta em uma string e imprimimos o resultado na tela.

# Note que evitamos o uso da funcao pronta reverse() para inverter a string diretamente, como solicitado no enunciado.