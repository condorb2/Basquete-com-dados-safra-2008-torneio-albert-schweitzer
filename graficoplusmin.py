import matplotlib.pyplot as plt

jogadores = ["Mathias", "Pedrinho", "Gluck"]
medias = [9.7, 4.5, 8.8]

labels = ["M+P+G", "M+P", "M+G", "P+G", "Mathias", "Pedrinho", "Gluck"]
valores = [5.0, 3.0, 11.0, 0.0, 4.3, 2.0, 1.7]

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].bar(jogadores, medias)
axs[0].set_title("Média Final de Plus/Minus")
axs[0].set_ylim(0, 12)

for i, v in enumerate(medias):
    axs[0].text(i, v + 0.2, f"{v}", ha='center')

axs[1].bar(labels, valores)
axs[1].set_title("Impacto das Combinações")
axs[1].set_ylim(0, 12)

for i, v in enumerate(valores):
    axs[1].text(i, v + 0.2, f"{v}", ha='center')

plt.tight_layout()
plt.show()
