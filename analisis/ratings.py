
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

df = pd.read_csv("SuperMarketData.csv")

# Histograma de la distribucion de los ratings
plt.hist(df['Rating'],edgecolor="black",color='g')
plt.title('Ratings de los usuarios')
plt.show()

# Datos 
n = 5 # Cantidad de muestras
mu = np.average(df['Rating']) # media de la poblacion
var = np.var(df['Rating']) # varianza de la poblacion

# Probabilidad de obtener un rating mayor o igual
# a 8.5 en una muestra de n personas
Z = (8.5 - mu) / (np.sqrt(var/n))
prob = 1 - norm.cdf(Z)
print(prob)
