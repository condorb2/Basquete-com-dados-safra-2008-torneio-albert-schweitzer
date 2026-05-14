import matplotlib.pyplot as plt

jogadores = [
    "Edu Santos",
    "Hanzhi Tu",
    "Hunter Sevil",
    "Gustavs Brutans",
    "Gabrielle Turconi",
    "Aleksa Stikovic",
    "Kenan Youdom"
]

pontos = [9.1, 3.0, 4.3, 7.0, 4.8, 4.6, 9.8]

plt.figure(figsize=(11, 5))

plt.bar(jogadores, pontos)

plt.title("Pontos do Banco: Edu Santos vs. média dos jogadores mais pontuaram vindo do banco contra o Brasil")
plt.ylim(0, 12)

for i, v in enumerate(pontos):
    plt.text(i, v + 0.15, f"{v}", ha='center')

plt.xticks(rotation=10)
plt.tight_layout()

plt.show()
