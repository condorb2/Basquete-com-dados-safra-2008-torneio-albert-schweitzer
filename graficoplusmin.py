import matplotlib.pyplot as plt

jogadores = ["Mathias", "Pedrinho", "Gluck"]
medias = [9.7, 4.5, 8.8]

plt.figure()

plt.bar(jogadores, medias)

plt.title("Média Final de Plus/Minus")
plt.xlabel("Jogadores")
plt.ylabel("Plus/Minus")

for i, v in enumerate(medias):
    plt.text(i, v + 0.2, f"{v}", ha='center')

plt.show()






labels = [
    "M+P+G",
    "M+P",
    "M+G",
    "P+G",
    "Mathias",
    "Pedrinho",
    "Gluck"
]

valores = [5.0, 3.0, 11.0, 0.0, 4.3, 2.0, 1.7]

plt.figure(figsize=(10, 5))  # deixa mais largo pra não ficar apertado

plt.bar(labels, valores)

plt.title("Impacto das Combinações em Quadra")
plt.xlabel("Formações")
plt.ylabel("Plus/Minus")

for i, v in enumerate(valores):
    plt.text(i, v + 0.2, f"{v}", ha='center')

plt.show()
