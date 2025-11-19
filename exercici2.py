#2 Afegeix en un arxiu de Python cadascuna de les següents sentències com un comentari. 
# Després de cada comentari escriu el codi corresponent

# 2.1 crea una llista de llistes per emmagatzemar entre 2 i 4 tasques pendents del dia d’avui 
# #assignant a cada tasca un temps en minuts. Per exemple:
# tasques_pendents = [[35,"estudiar python"] ,[20,"plegar roba"] ]
tasques_pendents = [[35, "estudiar python"], [20, "plegar roba"], [22, "fer exercici"]]

#2.2 mostra el temps assignat a la segona tasca
print("Temps assignat a la segona tasca ", tasques_pendents[1][0]) # Temps assignat a la segona tasca 20

#2.3 mostra el número total de tasques
print("Número total de tasques ", len(tasques_pendents)) # Número total de tasques 3

#2.4 mostra el nom de la última tasca
ultima = len(tasques_pendents) -1 #Resultat de l'última posició de la llista principal
print("Nom de la última tasca: ", tasques_pendents[ultima][1]) # posició 1 de la subllista on està el text

#2.5 assigna a la segona tasca un temps de 66 minuts i mostra la llista
tasques_pendents[1][0] = 66 #Es canvia el temps de 20 a 66 de la segona tasca
print("Temps segona tasca: ", tasques_pendents) #Resultat [[35, "estudiar python"], [66, "plegar roba"], [22, "fer exercici"]]

#2.6 afegeix una nova tasca de 25 minuts que sigui "estudiar css" i mostra la llista
nova_tasca = [25, "estudiar css"]
tasques_pendents.append(nova_tasca)
print(tasques_pendents) #[[35, "estudiar python"], [66, "plegar roba"], [22, "fer exercici"], [25, "estudiar css"]]

#2.7 suma els temps de la 1a i 3a tasca i mostra el resultat
temps_tasca1 = tasques_pendents[0][0]
temps_tasca3 = tasques_pendents[2][0]
suma_temps_tasca_1_3 = temps_tasca1 + temps_tasca3
print("Suma del temps tasca 1 i 3: ", suma_temps_tasca_1_3) # 35 + 22 = 57

#2.8 mostra el nom de la 2a i última tasca i mostra el resultat de sumar els seus temps
nom_tasca2 = tasques_pendents[1][1]
temps_tasca2 = tasques_pendents[1][0]
ultima = len(tasques_pendents) -1 #numero de l'última posició
nom_ultima = tasques_pendents[ultima][1]
temps_ultima = tasques_pendents[ultima][0]
suma_temps_tasca_2_ultima = temps_tasca2 + temps_ultima
print("Tasca 2: ", nom_tasca2, " + última tasca: ", nom_ultima, " = ", suma_temps_tasca_2_ultima)

#2.9 inverteix l'ordre de les tasques i mostra la llista
tasques_pendents.reverse()
print("Llista invertida: ", tasques_pendents)
#Abans: [[35, "estudiar python"], [66, "plegar roba"], [22, "fer exercici"], [25, "estudiar css"]]
#Ara: [[25, "estudiar css"], [22, "fer exercici"], [66, "plegar roba"], [35, "estudiar python"]]

#2.10 treu la 2a tasca amb pop()
tasca_eliminada = tasques_pendents.pop(1) # posicion 1 es la segona tasca que el pop elimina
print(tasques_pendents) #[[25, "estudiar css"], [66, "plegar roba"], [35, "estudiar python"]]

#2.11 treu la 2a tasca amb remove()
tarea_a_borrar = tasques_pendents[1]
tasques_pendents.remove(tarea_a_borrar) #El remove busca i elimina, podem fer-ho a la vegada
print(tasques_pendents) #[[25, "estudiar css"], [35, "estudiar python"]]
