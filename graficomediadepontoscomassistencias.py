import matplotlib.pyplot as plt

jogadores = [
    "Pietro Melo",
    "Yuxiu Chen",
    "Arana Robertson",
    "Raivo Kudrjavcevs",
    "Federico Bottelli",
    "Aleksej Ivkovic",
    "Jamie Edoka"
]

medias = [20.0, 13.2, 9.9, 12.5, 20.1, 11.7, 17.8]

plt.figure(figsize=(11, 5))

plt.bar(jogadores, medias)

plt.title("Armadores que Mais Combinaram Médias de Assistências e Pontos")
plt.ylim(0, 22)

for i, v in enumerate(medias):
    plt.text(i, v + 0.2, f"{v}", ha='center')

plt.xticks(rotation=10)
plt.tight_layout()

plt.show()
