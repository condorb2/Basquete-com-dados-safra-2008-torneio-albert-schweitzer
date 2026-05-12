import matplotlib.pyplot as plt

jogadores = [
    "Edu Santos",
    "Hanzhi Tu",
    "Hunter Sevil",
    "Gustavs Brutans",
    "Gabrielle Turconi",
    "Aleksa Stikovic",
    "Caspar Vossenberg"
]

pontos = [9.1, 3.0, 4.3, 7.0, 4.8, 4.6, 11.2]

plt.figure(figsize=(10, 5))

plt.bar(jogadores, pontos)

plt.title("Pontos Vindo do Banco")
plt.ylim(0, 13)  # Vai até 13 no eixo Y

for i, v in enumerate(pontos):
    plt.text(i, v + 0.2, f"{v}", ha='center')

plt.xticks(rotation=15)
plt.tight_layout()

plt.show()
