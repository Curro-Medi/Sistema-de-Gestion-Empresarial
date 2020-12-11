print("--Biemvenido a este programa--")

listainst = []
nombre1 = input("Indique primer centro: ")
listainst.append(nombre1)
nombre2 = input("Indique segundo centro: ")
listainst.append(nombre2)
nombre3 = input("Indique tercer centro: ")
listainst.append(nombre3)
nombre4 = input("Indique cuarto centro: ")
listainst.append(nombre4)
nombre5 = input("Indique quinto centro: ")
listainst.append(nombre5)

def busqueda ():
    if 'FESAC' in listainst :
        print("fesac si esta en la lista")    #busqueda fesac
    else:         
        print("Elcentro no esta en la lista")
         
         
def insert():
    listainst.append("IES Julio Costeau") 
    
def sustitucion():    

    cont = False;
    for list in listainst:
        if list.__eq__('FESAC'):
            cont = True
        else:         
            cont = False
    
    if cont == True:
        listainst.remove('FESAC')
        listainst.insert(0, 'FESAC')    

    elif cont == False:
        listainst.insert(0, 'FESAC')    
     

def eliminar():
    cont = False;
    for list in listainst:
        if list.__eq__('IES Julio Costeau'):
            cont = True
        else:         
            cont = False
    
    if cont == True:
        listainst.remove('IES Julio Costeau')
    elif cont == False:
        print("El centro no esta en la lista")
    
    
def nuevaLista():  
    newLista = []
    
    for list in listainst:
         
        elemento1 = listainst.__getitem__(0)#cojo valores lista
        elemento2 = listainst.__getitem__(1)
   
   
    newLista.append(elemento1)
    newLista.append(elemento2)     #los inserto en nueva lista
    
    listainst.__delitem__(0) #los borro de la vieja lista
    listainst.__delitem__(1)
    
    # imprimo la nueva lista
    print(newLista)
        
        
print(busqueda())
insert()
print(listainst)
sustitucion()
print(listainst)
eliminar()
print(listainst)
nuevaLista()
print(listainst)



        
