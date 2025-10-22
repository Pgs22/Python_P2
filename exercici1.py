#Afegeix en un arxiu de Python cadascuna de les següents sentències com un comentari. 
# #Després de cada comentari escriu el codi corresponent

#1.1 crea una llista de nom "notes" que contingui una de les següents llistes de valors:
#● 5,4,7,2,3,9
#● 5,4,7,2,3
notes = [5,4,7,2,3,9]

#1.2 substitueix el 5 per un 1 i mostra la llista
posicion = notes.index(5) ##Busco primero la posición donde está el 5 y la guardo en la variable
notes.remove(5) ##Elimino el valor 5
notes.insert(posicion, 1) ## Afegir valor 1
print(notes) #[1,4,7,2,3,9]

#1.3 mostra el valor de la última posició (utilitza len() per calcular la última posició)
posicion = len(notes) - 1 ##guardo en una variable l'utlima posicio
notes[posicion] # valor de la posicio 9

#1.4 utilitza index() per buscar i mostrar en quina posició està el número 4
posicio = [notes.index(4)] ## [1,4,7,2,3,9]
print(posicio) # numero de posicio del valor 4: 1

#1.5 utilitza append per afegir un nou valor al final de la llista i mostra-la
notes.append(0)
print(notes) ## [1,4,7,2,3,9,0]

#1.6 utilitza insert() per afegir el valor 88 després del 4 i mostra la llista
posicion = notes.index(4)
notes.insert(posicion,88) ## [1,4,88,7,2,3,9,0]
print(notes)

#1.7 utilitza count per saber i mostrar quantes vegades apareix un valor
total = notes.count(2) ### guarda a la variable les vegades que apareix el 2 a l'array [1,4,88,7,2,3,9,0]
print(total) #resposta una vegada: 1

#1.8 utilitza pop() per treure i mostrar el valor en la última posició
ultimo = notes.pop() # Abans: ## [1,4,88,7,2,3,9,0]
print(ultimo) ## Ara [1,4,88,7,2,3,9,0]

#1.9 utilitza remove() per treure el valor 2 de l'array i mostra la llista
notes.remove(2)
print(notes)

#1.10 utilitza reverse() per invertir la posició dels valors dins l'array i mostra la llista
notes.reverse()
print(notes)

#1.11 utilitza sum() i len() per calcular i mostrar el valor mitg dels valors dins l'array
posicion = len(notes) - 1
suma = 0
for i in notes[posicion]:
    posicion -= i
media = int (suma / 5)
print(media)

#1.12 mostra el valor situat al mig de l'array , si l'array te un número parell, 
# #arrodoneix la posició del mig cap amunt
posicions = len(notes)
if(posicions%0):
    mig = int(posicions/2)
    print(notes[mig])
#elif(!posicions%0):

