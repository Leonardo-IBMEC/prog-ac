### Exercício 1: equações de segundo grau

# Solicita os parâmetros ao usuário
a = float(input("Informe o parâmetro a da equação: "))
b = float(input("Informe o parâmetro b da equação: "))
c = float(input("Informe o parâmetro c da equação: "))

# Calcula o delta da equação
delta = b**2 - 4*a*c

# Verifica se existem raízes reais
if delta > 0:
    # Calcula as duas raízes usando a fórmula de Bhaskara
    raiz1 = (-b + (delta)**1/2) / (2*a)
    raiz2 = (-b - (delta)**1/2) / (2*a)
    print(f"A primeira raiz da equação é {raiz1}")
    print(f"A segunda raiz da equação é {raiz2}")
elif delta == 0:
    # Calcula a única raiz quando o delta for zero
    raiz = -b / (2*a)
    print(f"A raiz da equação é {raiz}")
else:
    # Não há raizes reais
    print("A equação não possui raízes reais.")


### Exercício 2: anos bissextos

# Solicita o ano ao usuário
ano = int(input("Informe o ano: "))

# Verifica se o ano é bissexto
bissexto = (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0

# Exibe o resultado
print(bissexto)
