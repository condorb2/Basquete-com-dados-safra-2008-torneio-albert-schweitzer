import matplotlib.pyplot as plt

labels = ['Bom ataque', 'Mau ataque']
sizes = [69.7, 30.3]
colors = ['green', 'red']

plt.figure(figsize=(8, 8))

plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'edgecolor': 'black'}
)

plt.title('Efetividade dos rebotes ofensivos de Isaiah Santos')

plt.text(
    0,
    -1.35,
    '33 rebotes totais | 23 bons | 10 maus\nTotal de jogos: 6',
    ha='center',
    fontsize=11
)

plt.axis('equal')

plt.show()
