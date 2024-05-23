#Criando a função do Juros Simples
def juros_simples(capital, taxa_juros, tempo):
    juros = capital * taxa_juros * tempo
    montante = capital + juros
    print(f"Investido: R${capital:.2f}. Rendeu: R${juros:.2f}. Total: R${montante:.2f}")

#Criando a função do Juros Composto
def juros_composto(capital, taxa_juros, tempo):
    montante = capital * (1 + taxa_juros) ** tempo
    rendimento = montante - capital
    print(f"Investido: R${capital:.2f}. Rendeu: R${rendimento:.2f}. Total: R${montante:.2f}")

print("Calculadora de Juros")
#Laço de repetição para as opções do menu
while True:
    print("Escolha o tipo de cálculo:")
    print("1. Juros Simples")
    print("2. Juros Compostos")
    print("0. Sair")
    
    escolha = input("Digite 1, 2 ou 0: ")
    # IF saindo do WHILE com o BREAK
    if escolha == '0':
        print("Saindo do programa.")
        break
    # Escolhendo o tipo do Juros
    elif escolha in ['1', '2']:
        capital = float(input("Digite o valor inicial do investimento (R$): "))
        taxa_juros = float(input("Digite a taxa de juros mensal (em %): ")) / 100
        tempo = int(input("Digite o número de mêses: "))
        
        if escolha == '1':
            juros_simples(capital, taxa_juros, tempo)
        elif escolha == '2':
            juros_composto(capital, taxa_juros, tempo)
    # Caso a entrada for diferente de 0, 1 ou 2
    else:
        print("Digite 1, 2 ou 0 para sair.")
