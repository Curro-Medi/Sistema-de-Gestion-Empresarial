cuentas = [(300,450),(400,300),(500,350),(450,300)]
# el primer numero indica ingresos, el segundo gastos.
impares = cuentas[::2]
pares = cuentas[1::2]
dosPrimeros = cuentas[:2]
dosUltimos = cuentas[2], cuentas [3]        #cuentas[-2:]
primeroYultimo = cuentas[0], cuentas[3]     #cuentas[::len(cuentas)-1]


print("Los impares son: " , impares)
print("Los pares son: ", pares)
print("Los dos primeros son: ", dosPrimeros)
print("Los dos ultimos son: ", dosUltimos)
print("El primero y ultimo son: " , primeroYultimo)
