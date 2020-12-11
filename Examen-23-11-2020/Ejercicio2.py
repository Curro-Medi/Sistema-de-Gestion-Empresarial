class libro:
    
    def __init__(self, nombre, editorial, edicion, autor):
        self.__nombre = nombre
        self.__editorial = editorial
        self.__edicion = edicion
        self.__autor = autor
        
         
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
        
    @property
    def editorial(self):
        return self.__editorial

    @editorial.setter
    def editorial(self,editorial):
        self.__editorial = editorial
        
    @property
    def edicion(self):
        return self.__edicion

    @edicion.setter
    def edicion(self,edicion):
        self.__edicion = edicion
        
    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self,autor):
        self.__autor = autor
        
     

    def descripcion(self):
    
        cadena="Nombre -> "+self.__nombre + "Editorial -> "+self.__editorial+ "Edicion -> "+str(self.__edicion)+ "Autor -> "+self.__autor
        return cadena

class estanteria(libro):
    
    def __init__(self,nombre, editorial, edicion, autor, planta, pasillo, modulo, seccion):
        super().__init__(nombre, editorial, edicion, autor)
        self.__nombre = nombre
        self.__editorial = editorial
        self.__edicion = edicion
        self.__autor = autor
        
        self.__planta = planta
        self.__pasillo = pasillo
        self.__modulo = modulo
        self.__seccion = seccion
        
        
    @property
    def planta(self):
        return self.__planta

    @planta.setter
    def planta(self,planta):
        self.__planta = planta
        
    @property
    def pasillo(self):
        return self.__pasillo

    @pasillo.setter
    def pasillo(self,pasillo):
        self.__pasillo = pasillo
        
    @property
    def modulo(self):
        return self.__modulo

    @modulo.setter
    def modulo(self,modulo):
        self.__modulo = modulo
        
    @property
    def seccion(self):
        return self.__seccion

    @seccion.setter
    def seccion(self,seccion):
        self.__seccion = seccion
        
        
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
        
    @property
    def editorial(self):
        return self.__editorial

    @editorial.setter
    def editorial(self,editorial):
        self.__editorial = editorial
        
    @property
    def edicion(self):
        return self.__edicion

    @edicion.setter
    def edicion(self,edicion):
        self.__edicion = edicion
        
    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self,autor):
        self.__autor = autor
        
     

    def descripcion(self):
    
        cadena="Nombre -> "+self.__nombre + "Editorial -> "+self.__editorial+ "Edicion -> "+str(self.__edicion)+ "Autor -> "+self.__autor+ "Planta -> "+str(self.__planta)+ "Pasillo -> "+str(self.__pasillo)+ "Modulo -> "+str(self.__modulo)+ "Seccion -> "+str(self.__seccion)                        
        return cadena
        
        
        
        
        
        
        
        
    
    
    