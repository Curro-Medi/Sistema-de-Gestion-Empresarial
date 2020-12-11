
def consultas():
    
    edad = int(input("Edad --> "))
    
    #No se porque no me coge que si no es int haga el while, en lugar de eso repite siempre el while
    #while edad != int:
     #   print("La edad tiene que ser un numero entero pichita")
      #  edad = int(input("Edad --> "))
    
    while edad<18:
        print("Si no eres mayor de edad no puedes entrar")
        edad = int(input("Edad --> "))

    localidad = input("Localidad --> ")
    
    if edad<30 and localidad=="SEVILLA":
        print("Le atendera el Dr Cifuentes en la planta 1")
        
    elif edad > 30 and localidad == "SEVILLA":
        print("Le atendera la Dra Garcia en la planta 2")
        
    elif edad < 30 and localidad != "SEVILLA":
        print("Le atendera el Dr Huesa en la planta 1")
    
    elif edad > 30 and localidad != "SEVILLA":
        print("Le atendera la Dra Perianiez en la planta 2")
    


consultas()