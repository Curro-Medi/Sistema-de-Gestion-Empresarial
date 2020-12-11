
def transformar_compras(lista):
    
    res = []
    dic = dict()
    for linea in lista:
        dic["id"] = linea.__getitem__(0)
        dic["cod_prod_vend"] = linea.__getitem__(1)
        dic["cantidad"] = linea.__getitem__(2)
        dic["ciudad"] = linea.__getitem__(3)
        dic["importe"] = linea.__getitem__(4)
        dic["nombre_producto"] = linea.__getitem__(5)
        dic["precio_venta"] = linea.__getitem__(6)
        res.append(dic)
        
    return res
    
    
def calcular_compras(compra):

    res = []
    dic = dict()
    for linea in lista:
        total = (linea.__getitem__(2)*linea.__getitem__(6) - 94 ) 
        dic["id"] = linea.__getitem__(0)
        dic["cod_prod_vend"] = linea.__getitem__(1)
        dic["cantidad"] = linea.__getitem__(2)
        dic["ciudad"] = linea.__getitem__(3)
        dic["importe"] = total
        dic["nombre_producto"] = linea.__getitem__(5)
        dic["precio_venta"] = linea.__getitem__(6)
        dic["costeprod"] = linea.__getitem__(7)
        res.append(dic)
        
    return res





def calcular_inventario(lista):

    res = []
    dic = dict()
    for linea in lista:
        total = (linea.__getitem__(2) - 47 ) 
        dic["Cantidad total--> "] = total
        importotal = (linea.__getitem__(3) - 94 ) 
        dic["Importe total--> "] = importotal
    return res
    