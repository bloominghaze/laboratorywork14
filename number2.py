import numpy as np
import matplotlib.pyplot as plt

years = list(range(1990, 2011))
gpi_ukraine = [
    70.1365853658537, 68.8780487804878, 69.0682926829269, 68.4756097560976,
    67.8385365853659, 67.1370731707317, 66.8878048780488, 67.2953658536585,
    67.9887804878049, 68.2134146341463, 67.859512195122, 68.2870731707317,
    68.2756097560976, 68.2107317073171, 68.1853658536585, 67.9568292682927,
    68.0775609756098, 68.2221951219512, 68.2514634146342, 69.19, 70.2653658536586
]
gpi_us = [
    75.2146341463415, 75.3658536585366, 75.6170731707317, 75.419512195122,
    75.619512195122, 75.6219512195122, 76.0268292682927, 76.4292682926829,
    76.5804878048781, 76.5829268292683, 76.6365853658537, 76.8365853658537,
    76.9365853658537, 77.0365853658537, 77.4878048780488, 77.4878048780488,
    77.6878048780488, 77.9878048780488, 78.0390243902439, 78.390243902439,
    78.5414634146342
]

plt.figure(figsize=(10, 6))
plt.plot(years, gpi_ukraine, label='Україна', color='green', marker='o')
plt.plot(years, gpi_us, label='Сполучені Штати', color='blue', marker='o')

plt.title('Тривалість життя при народженні: Україна та Сполучені Штати', fontsize=15)
plt.xlabel('Рік', fontsize=12, color='red')
plt.ylabel('Тривалість життя (роки)', fontsize=12, color='red')

plt.legend()
plt.grid(True)

plt.show()

country1 = input("Введіть першу країну (Україна або Сполучені Штати): ").strip()
country2 = input("Введіть другу країну (Україна або Сполучені Штати): ").strip()

if country1.lower() == 'україна':
    values1 = gpi_ukraine
elif country1.lower() == 'сполучені штати':
    values1 = gpi_us
else:
    print("Перша країна недоступна.")
    values1 = None

if country2.lower() == 'україна':
    values2 = gpi_ukraine
elif country2.lower() == 'сполучені штати':
    values2 = gpi_us
else:
    print("Друга країна недоступна.")
    values2 = None

if values1 is not None and values2 is not None:
    width = 0.35
    x = np.arange(len(years))

    plt.figure(figsize=(10, 6))
    plt.bar(x - width/2, values1, width, label=country1, color='green')
    plt.bar(x + width/2, values2, width, label=country2, color='blue')

    plt.title('Тривалість життя при народженні для обраних країн', fontsize=15)
    plt.xlabel('Рік', fontsize=12)
    plt.ylabel('Тривалість життя (роки)', fontsize=12)
    plt.xticks(x, years)
    plt.legend()
    plt.grid(True)

    plt.show()
