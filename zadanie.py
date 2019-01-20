import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import aseegg as ag

dane = pd.read_csv("sub-01-trial-007.csv", delimiter=',', engine='python')
t = np.linspace (0, 38.01, 200*38.01)
sygnal = dane["k2"]
# plt.plot(t, sygnal)
# plt.xlabel("Czas [s]")
# plt.ylabel("Amplituda [-]")
# plt.show()

przefiltrowany = ag.pasmowozaporowy(sygnal, 200, 49, 51)
przefiltrowany = ag.pasmowoprzepustowy(sygnal, 200, 1, 50)

# plt.plot(t, przefiltrowany)
# plt.xlabel("Czas [s]")
# plt.ylabel("Amplituda [-]")
# plt.show()

wartosc = dane["k2"]
wynik = dane["k6"]
wymrugane = ["Cyfry wybrane przez osobę badaną to:"]

for i in range(len(dane["k1"])):
    if wartosc[i] > -0.8:
        if wynik[i] != wymrugane[len(wymrugane) - 1]:
            wymrugane.append(wynik[i])

print(wymrugane)
