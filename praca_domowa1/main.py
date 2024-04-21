#instalacja: pip install matplotlib
import matplotlib.pyplot as plt     
import random as rnd
x = [0]     # lista x z wprowadzonym x początkowym x_0 = 0
y = [0]     # lista y z wprowadzonym y początkowym y_0 = 0
for i in range(1, 10000):
    random_number = rnd.random()    #liczba rzeczywista z przedziału [0;1)
    # jeśli wylosowana liczba zawiera się w [0;0.5), to wybierany jest pierwszy układ równań
    if random_number < 0.5:         
        x.append(-0.4 * x[i - 1] - 1)
        y.append(-0.4 * y[i - 1] + 0.1)
    # jeśli wylosowana liczba zawiera się w [0.5;1), to wybierany jest pierwszy układ równań
    else:
        x.append(0.76 * x[i - 1] - 0.4 * y[i - 1])
        y.append(0.4 * x[i - 1] + 0.76 * y[i - 1])
plt.plot(x, y, ".", markersize=1)      #rozmiar punktu wielkości 1
plt.show()