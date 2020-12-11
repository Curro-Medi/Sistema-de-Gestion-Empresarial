class coche:
    
    def __init__(self, nombre, marca, plazas, motor, unidades_disponibles, tipo):
        self.__nombre = nombre
        self.__marca = marca
        self.__plazas = plazas
        self.__motor = motor
        self.__unidades_disponibles = unidades_disponibles
        self.__tipo = tipo
        
         
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
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
        
    @property
    def unidades_disponibles(self):
        return self.__unidades_disponibles

    @unidades_disponibles.setter
    def unidades_disponibles(self,unidades_disponibles):
        self.__unidades_disponibles = unidades_disponibles
     
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self,tipo):
        self.__tipo = tipo
     
    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self,motor):
        self.__motor = motor
     

    def descripcion(self):
    
        cadena="Nombre -> "+self.__nombre + "Marca -> "+self.__marca+ "Plazas -> "+str(self.__plazas)+ "Motor -> "+self.__motor+"Unidades Disponibles -> "+self.__unidades_disponibles+"Tipo -> "+self.__tipo
        return cadena

class concesionario(coche):
    
    def __init__(self, nombre, marca, plazas, motor, unidades_disponibles, tipo, nombre_conce, poblacion, multimarca):
        super().__init__( nombre, marca, plazas, motor, unidades_disponibles, tipo)
        self.__nombre = nombre
        self.__marca = marca
        self.__plazas = plazas
        self.__motor = motor
        self.__unidades_disponibles = unidades_disponibles
        self.__tipo = tipo
        self.__nombre_conce = nombre_conce
        self.__poblacion = poblacion
        self.__multimarca = multimarca
        
         
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
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
        
    @property
    def unidades_disponibles(self):
        return self.__unidades_disponibles

    @unidades_disponibles.setter
    def unidades_disponibles(self,unidades_disponibles):
        self.__unidades_disponibles = unidades_disponibles
     
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self,tipo):
        self.__tipo = tipo
     
    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self,motor):
        self.__motor = motor
        
        
    @property
    def nombre_conce(self):
        return self.__nombre_conce

    @nombre_conce.setter
    def nombre_conce(self,nombre_conce):
        self.__nombre_conce = nombre_conce
        
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
    
        cadena="Nombre -> "+self.__nombre + "Marca -> "+self.__marca+ "Plazas -> "+str(self.__plazas)+ "Motor -> "+self.__motor+"Unidades Disponibles -> "+self.__unidades_disponibles+"Tipo -> "+self.__tipo+ self.__nombre_conce+self.__multimarca+self.__poblacion
        return cadena
        
        
    
    
    


