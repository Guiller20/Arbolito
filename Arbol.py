#Trabajando con arboles

#Crear una clase nodo
class Nodo:
    def __init__(self,dato):
        self.izquierdo=None
        self.derecho=None
        self.dato=dato

def insertar(raiz, nodo):
    if raiz is None:
        raiz=nodo
    elif(raiz.dato < nodo.dato):
        if raiz.derecho is None:
            raiz.derecho=nodo
        else:
            insertar(raiz.derecho, nodo) #llamando al mismo metodo
    elif(raiz.izquierdo is None):
        raiz.izquierdo=nodo
    else:
        insertar(raiz.izquierdo, nodo) #llamando al mismo metodo

def buscar(raiz, dato):
    if raiz in None:
        return False
    elif raiz.dato==dato:
        return True
    elif dato < raiz.dato:
        return  buscar(raiz.izquierdo, dato)
    else:
        buscar(raiz.derecha, dato)

#llamando a los metodos
r=int(input('Ingrese raiz: '))
raiz=Nodo(r) #Invocar la clase Nodo

op=0
while op<7:
    valor=int(input('Ingrese item: '))
    insertar(raiz, Nodo(valor))
    op=op+1

busqueda= int(input('Ingrese el valor a buscar: '))
if(buscar(raiz, busqueda)):
    print('Elemento fue encontrado')
else:
    print('Elemento no fue encontrado')

#Metodo de recorrido
#inorde
#Primero pasa al subarbol izquierdo
#luego pasa a la raiz
#luego al subarbol derecho
#Este es recursivo
def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierdo)
        print(raiz.dato, end= ' ')
        inorden(raiz.derecho)

def preOrden(raiz):
    if raiz is not None:
        print(raiz.dato, end= ' ')
        preOrden(raiz.izquierdo)
        preOrden(raiz.derecho)

def postOrden(raiz):
    if raiz is not None:
        postOrden(raiz.izquierdo)
        postOrden(raiz.derecho)
        print(raiz.dato, end= ' ')

print('Recorrido Inorden')
inorden(raiz)
print('')
print('Recorrido Preorden')
preOrden(raiz)
print('')
print('Recorrido Postorden')
postOrden(raiz)
