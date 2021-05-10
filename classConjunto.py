
class Conjunto:
    __lista=[]

    def __init__(self,conjunto=[]):
        #SI ALGUNO DE LOS ELEMENTOS DEL CONJUNTO NO ES UN ENTERO
        #SE CREA UN CONJUNTO VACIO DIRECTAMENTE
        i=0
        for elem in conjunto:
            if type(elem)==int:         
                i=i+1                   
        if i==len(conjunto):
            self.__lista=conjunto
        else:
            self.__lista=[]
        self.ordenar()
    def mostrar(self):                      #MUESTRA EL CONJUNTO
        print (self.__lista)
    def longitud(self):                     #RETORNA LA LONGITUD DEL CONJUNTO
        return len(self.__lista)
    def agregarElem(self,elem):
        self.__lista.append(elem)           #AGREGA UN ELEMENTO AL CONJUNTO
    def ordenar(self):
        self.__lista.sort()                  #ORDENA NUMERICAMENTE AL CONJUNTO
    def elementoIgual(self,elemento,otro):
        band=True
        i=0
        while band and i<otro.longitud():
            if elemento == otro.__lista[i]:     
                band=False                  #SI ENCUENTRA UN ELEMENTO IGUAL RETORNA FALSE
            else:                           #SI NO ENCUENTRA UN ELEMENTO IGUAL RETORNA TRUE
                i=i+1
        return band
    def carga(self):
        elemento=input('INGRESE UN ELEMENTO--> ')
        while elemento!='fin':              #SI SE INGRESA FIN DEJA DE AÑADIR
            if elemento.isdigit():          #PREGUNTA SI LA CADENA ELEMENTO PUEDE CONVERTIRSE A ENTERO
                if type(int(elemento))==int:    #PREGUNTA SI LA CADENA ELEMENTO ES ENTERO
                     if self.elementoIgual(int(elemento), self): #PREGUNTA SI EL ELEMENTO YA ESTÁ EN EL CONJUNTO
                            self.agregarElem(int(elemento))
                     else:
                         print('[[ELEMENTO REPETIDO]]')
                else:
                    print('Error: ingrese elemento del tipo entero')
            else:
                    print('Error: ingrese elemento del tipo entero')
            elemento=input('INGRESE UN ELEMENTO--> ')
        self.ordenar()                  #ORDENA EL CONJUNTO

    def __add__(self,otro):
        suma=Conjunto([])
        if type(otro)==Conjunto:
            for elem in self.__lista:
                if self.elementoIgual(elem, otro):
                    suma.agregarElem(elem)
            for elemO in otro.__lista:
                suma.agregarElem(elemO)
            suma.ordenar()
        return suma
    def __sub__(self,otro):
        resta=Conjunto([])
        if type(otro)==Conjunto:
            for elem in self.__lista:
                if self.elementoIgual(elem, otro):
                    resta.__lista.append(elem)
        return resta
    def __eq__(self,otro):
        band=None
        i=0
        if type(otro)==Conjunto:
            if self.longitud()==otro.longitud():
                for elem in self.__lista:
                    if not self.elementoIgual(elem, otro):
                        i=i+1
            
                if i==otro.longitud():
                    band=True
                else:
                    band=False
            else:
                band=False
        return band






    