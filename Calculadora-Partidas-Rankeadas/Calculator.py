# Função para calcular o saldo de partidas e o nível do jogador
def rankCalculator(v, d):
    # Calculando o saldo de vitórias
    score = v - d
    
    # Determinando o nível com base nas vitórias
    if score <= 10:  # Coloquei <= pois se score for igual a 10, iria dar erro de compilação
        level = "Ferro"
    elif score > 10 and score <= 20:
        level = "Bronze"
    elif score > 20 and score <= 50:
        level = "Prata"
    elif score > 50 and score <= 80:
        level = "Ouro"
    elif score > 80 and score <= 90:
        level = "Diamante"
    elif score > 90 and score <= 100:
        level = "Lendário"
    else:
        level = "Imortal"
        
    # Retorna o saldo e o nível
    return level, score
        
victory = int(input("Numero de vitórias: "))
defeat = int(input("Numero de derrotas: "))

rank, score = rankCalculator(victory, defeat)

print(f"O Herói tem de saldo {score} está no nível de {rank}") 