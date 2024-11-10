# Coletando informações do herói
option = 1

# Laço de repetição
while(option == 1):
    name = input("Digite o nome do herói: ")
    xp = int(input("Digite a quantidade de experiência (XP) do herói: "))
    
    # Classificando o nível com base na XP
    if xp < 1000:
        level = "Ferro"
    elif 1001 <= xp <= 2000:
        level = "Bronze"
    elif 2001 <= xp <= 5000:
        level = "Prata"
    elif 5001 <= xp <= 7000:
        level = "Ouro"
    elif 7001 <= xp <= 8000:
        level = "Platina"
    elif 8001 <= xp <= 9000:
        level = "Ascendente"
    elif 9001 <= xp <= 10000:
        level = "Imortal"
    else:
        level = "Radiante"
    
    # Exibindo o resultado
    print(f"O Herói de nome {name} está no nível de {level}")
    
    # Pergunta ao usuário se deseja classificar outro herói
    option = int(input("Deseja ver outro herói? 1[sim] e 0[não]: "))
    
     # Validação para aceitar apenas 0 ou 1 
    while option != 0 and option != 1:
        option = int(input("Código inválido. Deseja checar outro herói? (1 - Sim, 0 - Não): "))
    
# Encerramento do programa
print("------------------")
print("Programa encerrado")