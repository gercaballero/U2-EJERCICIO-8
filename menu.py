import os
from classConjunto import Conjunto

class Menu:
    __switcher=None
    __c1=None
    __c2=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5,
                            6:self.salir
                         }
        self.__c1=Conjunto([])
        self.__c2=Conjunto([])
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op):
        func= self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Salida del programa')

    def opcion1(self):
        self.__c1=Conjunto([])      #VACIA LOS CONJUNTOS
        self.__c2=Conjunto([])      #VACIA LOS CONJUNTOS
        os.system('cls')
        print('~~~CARGA CONJUNTO 1 (fin para finalizar)~~~')
        self.__c1.carga()
        input()
        os.system('cls')
        print('~~~CARGA CONJUNTO 2 (fin para finalizar)~~~')
        self.__c2.carga()
        input()
        os.system('cls')

    def opcion2(self):
        os.system('cls')
        print('~~~SUMA CONJUNTO 1 + CONJUNTO 2~~~')
        self.__c1.mostrar()
        print('+')
        self.__c2.mostrar()
        print('=')
        suma=self.__c1+self.__c2
        suma.mostrar()
        input()
        os.system('cls')
    
    def opcion3(self):
        os.system('cls')
        print('~~~RESTA CONJUNTO 1 - CONJUNTO 2~~~')
        self.__c1.mostrar()
        print('-')
        self.__c2.mostrar()
        print('=')
        resta=self.__c1-self.__c2
        resta.mostrar()
        input()
        os.system('cls')
    def opcion4(self):
        os.system('cls')
        print('-----¿CONJUNTO 1 == CONJUNTO 2?-----')
        if self.__c1==self.__c2:
            print('CONJUNTO 1 ES IGUAL A CONJUNTO 2')
        else:
            print('CONJUNTO 1 NO ES IGUAL A CONJUNTO 2')
        input()
        os.system('cls')
    def opcion5(self):
        os.system('cls')
        print('~~~CONJUNTO 1~~~')
        self.__c1.mostrar()
        print('~~~CONJUNTO 2~~~')
        self.__c2.mostrar()
        input()
        os.system('cls')

             
