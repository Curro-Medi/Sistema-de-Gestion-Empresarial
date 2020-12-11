lista =[(1,1,80,None,'producto1',1.5),(2,1,70,None,'producto1',1.5),(3,2,15,None,'producto2',1.8),(4,2,21,None,'producto2',1.8),(5,2,18,None,'producto2',1.8),(6,3,40,None,'producto3',2.1),(7,3,24,None,'producto3',2.1),(8,4,17,None,'producto4',2.4),(9,4,32,None,'producto4',2.4),(10,4,40,None,'producto4',2.4)]
resultado = []



for importe in lista:
    importetotal = (importe.__getitem__(2)*importe.__getitem__(6) ) 

    prod = (importe.__getitem__(5), importe.__getitem__(6), importetotal)
    resultado.append(prod)
    
transformar_compras(lista)

calcular_compras(lista)

calcular_inventario(lista)
    