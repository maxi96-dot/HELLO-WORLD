# questo esempio mostra come creare una lista di oggetti eterogenei e gestirli 
# in modo da setacciare e mettere in due liste distinge oggetti tra loro omogenei
#
# In particolare viene creata una lista di interi e stringhe
# Gli elementi della lista vengono successivamente separati in due liste, 
# una per gli interi e l'altra per le stringhe


lista = [1,2,3,'quattro',5,6,'sette']

lista_int = list()
lista_str = list()

for elemento in lista:
  if type(elemento) == type(1):
    lista_int.append(elemento)
  else:
    lista_str.append(elemento)