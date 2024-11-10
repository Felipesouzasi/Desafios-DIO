#Criando a classe Herói
class Hero:
    def __init__(self, name, age, type_):
        self.name = name
        self.age = age
        self.type = type_

    def attack(self):
        attacks = {
            "mago": "usou magia",
            "guerreiro": "usou espada",
            "monge": "usou artes marciais",
            "ninja": "usou shuriken"
        }
        
        attack_action = attacks.get(self.type, "usou um ataque desconhecido")
        print(f"O {self.type} de {self.age} anos atacou e {attack_action}")

# Laço de repetição
option = 1
while option == 1:
    # Criando instancia do herói
    hero_name = input("Digite o nome do herói: ")
    hero_age = int(input("Digite a idade do herói: "))
    hero_type = input("Entre com o tipo do herói(mago, guerreiro, monge, ninja): ").lower()
    
    hero = Hero(hero_name, hero_age, hero_type)
    hero.attack()
    
    # Pergunta ao usuário se deseja jogar novamente
    option = int(input("Deseja jogar de novo? 1[sim] e 0[não]: "))
 
print("----------------------")   
print("Obrigado por jogar!")
