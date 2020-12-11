def pedir_datos():

    nombre = input("Nombre --> ")
    apellidos = input("Apellidos --> ")
    direccion = input("Direccion --> ")
    poblacion = input("Poblacion --> ")
    telefono = input("Telefono --> ")
    email = input("Email --> ")
    
    if "@" and "." in email:
        print("El email es correcto")
    else:
        print("El email es incorrecto")
    
   
pedir_datos()
  


