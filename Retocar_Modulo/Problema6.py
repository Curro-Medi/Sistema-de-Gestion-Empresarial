class coche:
    
    def __init__ (self, nombre, marca, plazas, motor, unidades_disponibles, tipos):
        self.nombre = nombre
        self.marca = marca
        self.plazas = plazas
        self.motor = motor
        self.unidades_disponibles = unidades_disponibles
        self.tipos = tipos
    
    @property
    def nombre(self):
        return self.__nombre
     
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
     
    @property
    def marca(self):
        return self.__marca
     
    @marca.setter
    def marca(self,marca):
        self.__marca = marca
     
    @property
    def plazas(self):
        return self.__plazas
     
    @plazas.setter
    def plazas(self,plazas):
        self.__plazas = plazas
         
    @property
    def motor(self):
        return self.__motor
     
    @motor.setter
    def motor(self,motor):
        self.__motor = motor
        
    @property
    def unidades_disponibles(self):
        return self.__unidades_disponibles
     
    @unidades_disponibles.setter
    def unidades_disponibles(self,unidades_disponibles):
        self.__unidades_disponibles = unidades_disponibles
    
    @property
    def tipos(self):
        return self.__tipos
     
    @tipos.setter
    def tipos(self,tipos):
        self.__tipos = tipos
    
 
        
    def descripcion(self):
        cadena=""
        cadena="Nombre: "+ self.__nombre+"\nMarca:"+self.__marca+ "\nPlazas: "+str(self.__plazas) + "\nMotor: "+self.__motor + "\nUnidades_Disponibles: "+str(self.__unidades_disponibles) + "\nTipo: "+self.__tipos
        return cadena  
    
class concesionario(coche):
    
    def __init__ (self,nombre, marca, plazas, motor, unidades_disponibles, tipos, nombre_concesionario, poblacion, multimarca):
        super().__init__(nombre, marca, plazas, motor, unidades_disponibles, tipos)
        self.__nombre_concesionario = nombre_concesionario
        self.__poblacion = poblacion
        self.__multimarca = multimarca
        self.__nombre = nombre
        self.__marca = marca
        self.__plazas = plazas
        self.__motor = motor
        self.__unidades_disponibles = unidades_disponibles
        self.__tipos = tipos
   
    @property
    def nombre(self):
        return self.__nombre
     
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
     
    @property
    def marca(self):
        return self.__marca
     
    @marca.setter
    def marca(self,marca):
        self.__marca = marca
     
    @property
    def plazas(self):
        return self.__plazas
     
    @plazas.setter
    def plazas(self,plazas):
        self.__plazas = plazas
         
    @property
    def motor(self):
        return self.__motor
     
    @motor.setter
    def motor(self,motor):
        self.__motor = motor
        
    @property
    def unidades_disponibles(self):
        return self.__unidades_disponibles
     
    @unidades_disponibles.setter
    def unidades_disponibles(self,unidades_disponibles):
        self.__unidades_disponibles = unidades_disponibles
    
    @property
    def tipos(self):
        return self.__tipos
     
    @tipos.setter
    def tipos(self,tipos):
        self.__tipos = tipos
        
        
    @property
    def nombre_concesionario(self):
        return self.__nombre_concesionario
     
    @nombre_concesionario.setter
    def nombre_concesionario(self,nombre_concesionario):
        self.__nombre_concesionario = nombre_concesionario
        
        
    @property
    def poblacion(self):
        return self.__poblacion
     
    @poblacion.setter
    def poblacion(self,poblacion):
        self.__poblacion = poblacion
        
    @property
    def multimarca(self):
        return self.__multimarca
     
    @multimarca.setter
    def multimarca(self,multimarca):
        self.__multimarca = multimarca
      
    def descripcion(self):
        
        cadena="Nombre: "+ self.nombre+",\nMarca:"+self.marca+ "\nPlazas: "+str(self.plazas) + "\nMotor: "+self.motor + "\nUnidades_Disponibles: "+str(self.unidades_disponibles) + ",\nTipo: "+self.tipos + ",\nNombre_Concesionario: "+self.nombre_concesionario + ",\nPoblacion: "+self.poblacion + ",\nMultimarca: "+self.multimarca      
        return cadena  
    
coche1 = coche('BMW', 'SERIES', 5, 'DIESEL', 100, 'URBANO')  
coche2 = coche('TESLA', 'X', 2, 'ELECTRICO', 38, 'URBANO')  
concesionario = concesionario('Ford', 'Mustang', 7, 'GASOLINA', 23, '4X4', 'La casa de los Mustangs', 'Sevilla' , 'Ford Mustang')  

print(coche1.descripcion())
print('------------------')
print(coche2.descripcion())
print('------------------')
print(concesionario.descripcion())



