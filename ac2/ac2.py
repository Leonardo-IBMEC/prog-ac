"""
Programação Estruturada
2024.1

AC2
"""

# Exercício 1:

def eq_seg_grau(a, b, c):
    # Calculando o delta
    delta = b**2 - 4*a*c

    # Verificando o tipo de raízes
    if delta > 0:
        # Duas raízes reais distintas
        x1 = (-b + (delta)**(1/2)) / (2*a)
        x2 = (-b - (delta)**(1/2)) / (2*a)
        return x1, x2
    elif delta == 0:
        # Raízes reais iguais
        x = -b / (2*a)
        return x,
    else:
        # Sem raízes reais
        return None

# Solicita os parâmetros ao usuário
a = float(input("Informe o parâmetro a da equação: "))
b = float(input("Informe o parâmetro b da equação: "))
c = float(input("Informe o parâmetro c da equação: "))

# Calcula as raízes
raizes = eq_seg_grau(a, b, c)

# Exibe o resultado
if raizes:
    if len(raizes) == 1:
        print("A raiz da equação é", raizes[0])
    else:
        print("A primeira raiz da equação é", raizes[0])
        print("A segunda raiz da equação é", raizes[1])
else:
    print("A equação não possui raízes reais.")

def e_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0

# Solicita o ano ao usuário
ano = int(input("Informe o ano: "))

# Verifica se o ano é bissexto usando a função
bissexto = e_bissexto(ano)

# Exibe o resultado
print(bissexto)

#Exercício 2:

def calcula_salario(valor_hora, num_horas, irpf=0.275):
    salario_bruto = valor_hora * num_horas
    desconto_irpf = salario_bruto * irpf
    salario_liquido = salario_bruto - desconto_irpf
    return salario_liquido

# Solicita os parâmetros ao usuário

valor_hora = float(input("Informe o valor do salário por hora: "))
num_horas = float(input("Informe o número de horas trabalhadas: "))

# Calcula o salário
salario_liquido = calcula_salario(valor_hora, num_horas, irpf=0.275)

# Exibe o resultado
print("Salário líquido:", salario_liquido)
