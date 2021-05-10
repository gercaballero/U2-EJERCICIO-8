from classConjunto import Conjunto
from menu import Menu
import test
import os

if __name__=='__main__':
    os.system('cls')
    t=str(input('DESEA PROBAR EL TEST (S/N) : '))
    if t.lower()=='s':
        test.testar()
    menu= Menu()
    salir= False           
    while not salir:
            print("\n-------------------Menu-------------------")
            print(' 1- CARGAR 2 CONJUNTOS')
            print(' 2- SUMAR LOS 2 CONJUNTOS')
            print(' 3- RESTAR LOS DOS CONJUNTOS')
            print(' 4- COMPARAR LOS CONJUNTOS')
            print(' 5- MOSTRAR LOS CONJUNTOS')
            print(' 6- SALIR')
            op= input('\n INGRESE UNA OPCION: ')
            if op in ('1','2','3','4','5','6'):
                menu.opcion(int(op))
                if op=='6':
                    salir=True
            else:
                os.system('cls')
                print ("---OPCION NO VALIDA---")