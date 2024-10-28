# sucursal-multinacional

## Descripción 📑

Una empresa multinacional de supermercados quiere abrir una nueva sucursal en una comunidad con 160 000 habitantes. Para ello, se quiere conocer cuál es el porcentaje de la población a la que se necesita convencer para tener una ganancia mensual neta de mínimo 1 500 000 pesos.

## Datos 🗂️

Se cuenta con las ganancias por transacciones en otra comunidad con nivel socioeconómico semejante a la que se quiere llegar. Dichas ganancias ya contemplan el pago de impuestos, así como los costos por la compra de los productos.

## Estimación 📊

Se utilizará la función de densidad de probabilidad beta se estará utilizando para representar la distribución de los datos, debido a su gran flexibilidad para ajustarse a distintas distribuciones.

$B(\alpha,\beta) =
\int_0^1 x^{\alpha-1}(1-x)^{\beta-1} dx$

Para determinar los parámetros de $\alpha$ y $\beta$ de la distribución, se utiliza el método de *maximum likelihood estimation*.

## Costos a considerar 💰

Que se busque una ganancia mínima de millón y medio implica que ya se cubrieron los gastos de operación, por lo que se necesita un ingreso neto de 1 500 000 + gastos. Como los gastos en los productos ya se consideraron dentro de los datos de la base de datos, solo hace falta tomar en cuenta tomar en cuenta el salario de los empleados, la luz, el agua, entre otros.

El total de gastos contemplados es el siguiente:

* Salarios de... (1.15 veces de su salario mínimo respectivamente)
    * 40 personas de almacén
    * 60 personas que atienden a clientes en los pasillos
    * 30 cajeros
    * 20 conserjes
* Un gerente general con salario de 100 000 pesos mensuales
* 4 subgerentes con salario de 45 000 pesos mensuales a cada uno
* Luz: Se toma en cuenta $120 \frac{kW/h}{m^2}$ en un área de $2000 m^2$, y con un costo de $\$ 2.3 \frac{kW}{h}$
* Agua:
    * Costo por $m^3$ consumidos: 169 179.28
    * Saneamiento: 20 301.51
    * Alcantarillado: 16 917.93
    * IVA: 33 023.79
* Gestión de residuos: 2 708.82 por siete días de recolección a la semana
