# In questo esempio viene trattata un'altra importante struttura dati, il dizionario
#
# Il dizionario è una lista ad accesso associativo, ad ogni valore (oggetto) presente
# nel dizionario è associata una stringa (chiave).
# Per accedere a un oggetto del dizionario è sufficiente indicare il nome del
# dizionario seguito, tra parentesi quadre, dalla chiave dell'elemento che si desidera
# accedere. 

# Di seguito viene creato un dizionario le cui chiavi sono i nomi dei concorrenti di
# una gara di Kart.
# A ogni concorrente è associata una lista con i tempi di percorrenza dei singoli giri
# della gara.
# Il codice che segue ha l'obiettivo di 
# -- calcolare per ogni pilota il tempo totale di gara
# -- determinare il pilota vincitore  

giri = {
  'carlo': [66, 72, 64, 67, 66, 85],
  'piero': [65, 73, 66, 66, 66, 72],
  'marco': [66, 74, 67, 67, 67, 64]
  }

concorrenti = list(giri.keys())
tempi = list()
tempo_minimo = 100000

for concorrente in concorrenti:
  lista_giri = giri[concorrente]
  tempo_concorrente = sum(lista_giri)
  tempi.append(tempo_concorrente)
  if tempo_concorrente < tempo_minimo:
    tempo_minimo = tempo_concorrente
    vincitore = concorrente 

# Di seguito vengono presentate tre modalità completamente equivalenti di comporre una stringa con variabili

print(f'Complimenti al vincitore {vincitore}! ha realizzato il tempo {tempo_minimo}!')

print('Complementi al vincitore ' + vincitore + '! ha realizzato il tempo ' + str(tempo_minimo))

print('Complimenti al vincitore {0}! ha realizzato il tempo {1}!'.format(vincitore, tempo_minimo))