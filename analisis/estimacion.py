
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
from scipy.stats import norm

df = pd.read_csv("SuperMarketData.csv")
print(df.head())

# Conversion de dolares a pesos
sales = np.array(df["Sales"]) * 19.88

# Normalizacion de los datos
mx_sales = np.max(sales)
mn_sales = np.min(sales)
if (mx_sales != mn_sales): 
    sales_norm = 1/(mx_sales-mn_sales)*(sales-mn_sales)

# Ajustar modelo
a,b,_,_ = beta.fit(sales)

# Calculo de media y varianza normalizadas
mu_norm = a / (a + b)
var_norm = (a * b) / ((a + b)**2 * (a + b + 1))

# Media y varianza no normalizadas
mu = (mx_sales - mn_sales) * mu_norm + mn_sales
var = (mx_sales - mn_sales)**2 * var_norm

# Salarios mensuales: (mensual) * num. empleados
dias = 24
factor = 1.15
cajeros = (258.25 * dias) * 30
conserjes = (5000) * 20
gerentes_gral = (1e5) * 1
subgerentes = (45000) * 4
almacenistas = (262.13 * dias) * 40
pasillos = (264.65 * dias) * 40
nomina_total = factor * (cajeros+conserjes+almacenistas+pasillos) + gerentes_gral + subgerentes

# Otros gastos
luz_mensual = 120 * 2000 * 12 * 2.3 * 30
agua_mesual = 169179.28 + 20301.51 + 16917.93 + 33023.79
residuos_mensual = 2708.82 * 4

# Minimo de ingresos que se quiere
ingresos = 15e5 + nomina_total + luz_mensual + agua_mesual + residuos_mensual

# Calculo de cuantas personas se necesitan para lograr dichos ingresos
# con una seguridad mayor o igual al 99%
omega = norm.ppf(0.01)
a_ = mu**2
b_ = -2*mu*ingresos - omega**2*var
c_ = ingresos**2
N1 = (-b_ + np.sqrt(b_**2 - 4*a_*c_)) / (2*a_)
N2 = (-b_ - np.sqrt(b_**2 - 4*a_*c_)) / (2*a_)
print(f"Resultados: {N1}, {N2}")

if (ingresos/N1 - mu > 0):
    N = N1
else:
    N = N2

# Porcentaje de poblacion a convencer
poblacion = 16e4
porc_pob = N / poblacion
print(f"Se necesita convencer a {round(porc_pob,3)}% de la poblacion")
