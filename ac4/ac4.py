"""
Desenvolva uma versão inicial de CLI (command-line interface) para analisar se um aluno foi ou não aprovado em uma disciplina. A aplicação deve atender aos seguintes requisitos:

*A CLI deve perguntar ao usuário o seu nome. Caso a resposta do usuário seja um texto vazio, o programa deve ser encerrado;
*Em seguida, o programa deve calcular a média do usuário. Para isso, o programa deve ler as notas de AP1, AP2, AS e AC. Em seguida, deve exibir na tela a média final do aluno. Considere que a média é calculada como (AP1 + AP2) * 0.4 + AC * 0.2, sendo que a AS pode substituir a AP1 ou a AP2 (a menor dentre as duas);
*Por fim, a aplicação deve exibir na tela se o aluno foi aprovado ou reprovado, baseado na sua média. A média para aprovação é 7.0.

Organize o seu código em funções com responsabilidades distintas (uma para o cálculo de nota, uma para exibição de informações, uma para leitura de dados, etc.). Caso as notas passadas sejam inválidas (menores que 0 ou maiores que 10), o programa não deve calcular nada e deve ser encerrado.
"""

def ler_nome():
    nome = input("Informe o seu nome: ")
    if not nome:
        exit()
    return nome

def ler_notas():
    ap1 = float(input("Informe a nota da AP1: "))
    ap2 = float(input("Informe a nota da AP2: "))
    asub = float(input("Informe a nota da AS: "))
    ac = float(input("Informe a nota da AC: "))
        
    # Verificar se as notas são válidas (0 a 10)
    if 0 <= ap1 <= 10 and 0 <= ap2 <= 10 and 0 <= asub <= 10 and 0 <= ac <= 10:
        return ap1, ap2, asub, ac
    else:
        exit()

def calcular_media(ap1, ap2, asub, ac):
    menor_ap = min(ap1, ap2)
    media = (ap1 + ap2) * 0.4 + ac * 0.2
    
    # Verificar se AS substitui AP1 ou AP2
    if asub > menor_ap:
        media += asub - menor_ap
    
    return media

def verificar_aprovacao(media):
    if media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"

def exibir_resultado(nome, media, resultado):
    print(f"Nome do aluno: {nome}")
    print(f"Média final: {media}")
    print(f"Resultado: {resultado}")

def main():
    nome = ler_nome()
    ap1, ap2, asub, ac = ler_notas()

    # Calcular a média
    media = calcular_media(ap1, ap2, asub, ac)

    # Verificar aprovação e exibir resultado
    resultado = verificar_aprovacao(media)
    exibir_resultado(nome, media, resultado)

if __name__ == "__main__":
    main()
