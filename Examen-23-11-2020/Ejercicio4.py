
centros = [ ]
x=0
while x<2:
    centros = input("Dime nombre del centro ->")
    x = x+1

for lista in centros:
    if lista == "FESAC":
        print("Olee Fesac")

centros.append("IES Julio Costeau")
        
for lista in centros:
    print(lista)
    
for lista in centros:
    centros.__setitem__(0, "FESAC" )
    
for lista in centros:
    if lista == "IES Julio Costeau":
        centros.remove("IES Julio Costeau")
        
        
        
        