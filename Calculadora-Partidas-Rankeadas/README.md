# Calculadora de Partidas Rankeadas
Este projeto faz parte de um desafio da DIO proposto pelo Felipão. Utilizei Python para desenvolver uma calculadora que classifica o nível de um jogador com base no saldo entre vitórias e derrotas. O objetivo é aplicar conceitos fundamentais de programação, especialmente função.

## 📋 Funcionalidades
O programa solicita ao usuário a quantidade de vitórias e derrotas.
A partir desse saldo (vitórias - derrotas), o programa classifica o jogador em diferentes níveis, como Ferro, Bronze, Prata, Ouro, Diamante, Lendário, e Imortal.
Após exibir o nível, o programa pergunta se o usuário deseja verificar outro jogador:
    Se o usuário inserir 1, o programa continua.
    Se inserir 0, o programa encerra.
    Caso o usuário insira um valor diferente de 0 ou 1, uma mensagem de "Código inválido, tente novamente" é exibida até que uma entrada válida seja informada.
Se o saldo for resetado com o código 5, o programa reinicia.

## 💡 Exemplo de Uso
Número de vitórias: 30
Número de derrotas: 5
O Herói tem um saldo de 25 e está no nível Prata

Deseja checar o nível de outro herói? (1 - Sim, 0 - Não): 1

Número de vitórias: 90
Número de derrotas: 5
O Herói tem um saldo de 85 e está no nível Diamante

Deseja checar o nível de outro herói? (1 - Sim, 0 - Não): 0
Programa encerrado.

## 📦 Estrutura do Projeto
calculadora-partidas-rankeadas/
│
├── calculadora_ranked.py   # Código principal da calculadora
└── README.md               # Descrição do projeto
