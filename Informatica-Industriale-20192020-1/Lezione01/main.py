from fattoriale import fattorialeIterativo
from fattoriale import fattorialeRicorsivo 
from fibonacci import fibonacci

#from Lezione01.fattoriale import fattorialeIterativo
#from Lezione01.fattoriale import fattorialeRicorsivo 
#from Lezione01.fibonacci import fibonacci

print('Inserisci il numero di cui vuoi calcolare il fattoriale:')
n = int(input())

print('Calcolo del Fattoriale con funzione Iterativa:')
print(fattorialeIterativo(n))
print('Calcolo del Fattoriale con funzione Ricorsiva:')
print(fattorialeRicorsivo(n))

#indice = 0
#while(indice < 4):
#  indice = indice + 1
#  assert(fattorialeSemplice(indice) == fattorialeRicorsivo(indice)), 'PROBLEMA CON IL VALORE: ' + str(indice)


for indice in range(1,10):
  assert(fattorialeIterativo(indice) == fattorialeRicorsivo(indice)), 'PROBLEMA CON IL VALORE: ' + str(indice)

print('Inserisci il valore di cui vuoi calcolare il numero di Fibonacci:')
n = int(input())

print('Il valore calcolato è:')
print(fibonacci(n))