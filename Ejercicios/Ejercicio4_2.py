from Ejercicio4.Ejercicio4_1 import cuentas

cuentas = {"sevilla" : [300,450], "madrid" : [400,300], "segovia" : [500,350], "valencia" :[450,300]} # el primer numero indica ingresos, el segundo gastos.

#cuentasmadridysegovia = cuentas["madrid"] , cuentas["segovia"]
cuentasMadridYSegovia = [cuentas["madrid"][0] + cuentas["segovia"][0] , cuentas["madrid"][1] + cuentas["segovia"][1]]
cuentas["sevilla"] = cuentas["sevilla"] + [True]
sumaIngresos = cuentas["sevilla"][0] + cuentas["madrid"][0] + cuentas["segovia"][0] + cuentas["valencia"][0] 

print()
print("Las cuentas de Madrid y de Segovia son: ", cuentasMadridYSegovia)
print("Las cuentas de Sevilla: ", cuentas["sevilla"])
print("Suma de los ingresos totales: ", sumaIngresos)