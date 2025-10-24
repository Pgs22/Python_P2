#2 Afegeix en un arxiu de Python cadascuna de les següents sentències com un comentari. 
# Després de cada comentari escriu el codi corresponent
# 2.1 crea una llista de llistes per emmagatzemar entre 2 i 4 tasques pendents del dia d’avui assignant a cada tasca un temps en minuts. Per exemple:
# tasques_pendents = [[35,"estudiar python"] ,[20,"plegar roba"] ]
tasques_pendents = [[35, "estudiar python"], [20, "plegar roba"], [45, "fer exercici"]]

#2.2 mostra el temps assignat a la segona tasca
temps_segona_tasca = tasques_pendents[1][0]
print(f"Temps de la segona tasca: {temps_segona_tasca} minuts") # 20

#2.3 mostra el número total de tasques
numero_total_tasques = len(tasques_pendents)
print(f"Número total de tasques: {numero_total_tasques}") # 3

#2.4 mostra el nom de la última tasca
nom_ultima_tasca = tasques_pendents[-1][1]
print(f"Nom de la última tasca: {nom_ultima_tasca}") # "fer exercici"

#2.5 assigna a la segona tasca un temps de 66 minuts i mostra la llista
tasques_pendents[1][0] = 66
print(f"Llista després d'assignar nou temps: {tasques_pendents}")

#2.6 afegeix una nova tasca de 25 minuts que sigui "estudiar css" i mostra la llista
nova_tasca = [25, "estudiar css"]
tasques_pendents.append(nova_tasca)
print(f"Llista després d'afegir tasca: {tasques_pendents}")

#2.7 suma els temps de la 1a i 3a tasca i mostra el resultat
temps_1a = tasques_pendents[0][0]
temps_3a = tasques_pendents[2][0]
suma_temps_1a_3a = temps_1a + temps_3a
print(f"Suma dels temps de la 1a i 3a tasca: {suma_temps_1a_3a} minuts") # 35 + 45 = 80

#2.8 mostra el nom de la 2a i última tasca i mostra el resultat de sumar els seus temps
nom_2a = tasques_pendents[1][1]
temps_2a = tasques_pendents[1][0]
nom_ultima = tasques_pendents[-1][1]
temps_ultima = tasques_pendents[-1][0]
suma_temps_2a_ultima = temps_2a + temps_ultima

print(f"Nom de la 2a tasca: {nom_2a}")
print(f"Nom de la última tasca: {nom_ultima}")
print(f"Suma dels seus temps: {suma_temps_2a_ultima} minuts") # 66 + 25 = 91

#2.9 inverteix l'ordre de les tasques i mostra la llista
tasques_pendents.reverse()
print(f"Llista invertida: {tasques_pendents}")

#2.10 treu la 2a tasca amb pop()
tasca_eliminada_pop = tasques_pendents.pop(1) 
print(f"Tasca eliminada amb pop(): {tasca_eliminada_pop}") # [45, 'fer exercici']
print(f"Llista després de pop(1): {tasques_pendents}")

#2.11 treu la 2a tasca amb remove()
tasca_a_eliminar = tasques_pendents[1] 
tasques_pendents.remove(tasca_a_eliminar)
print(f"Llista després de remove(): {tasques_pendents}")