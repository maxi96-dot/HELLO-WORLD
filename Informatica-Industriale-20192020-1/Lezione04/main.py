from automa import Automa

coda = Automa()

coda.aggiungiStato('0')
coda.aggiungiStato('1')
coda.aggiungiStato('2')
coda.aggiungiStato('3')
coda.aggiungiStato('4')
coda.aggiungiStato('5')

coda.aggiungiTransizione('0', '1', 'arrivoSingolo')
coda.aggiungiTransizione('1', '2', 'arrivoSingolo')
coda.aggiungiTransizione('2', '3', 'arrivoSingolo')
coda.aggiungiTransizione('3', '4', 'arrivoSingolo')
coda.aggiungiTransizione('4', '5', 'arrivoSingolo')
coda.aggiungiTransizione('5', '5', 'arrivoSingolo')

coda.aggiungiTransizione('0', '2', 'arrivoDoppio')
coda.aggiungiTransizione('1', '3', 'arrivoDoppio')
coda.aggiungiTransizione('2', '4', 'arrivoDoppio')
coda.aggiungiTransizione('3', '5', 'arrivoDoppio')
coda.aggiungiTransizione('4', '5', 'arrivoDoppio')
coda.aggiungiTransizione('5', '5', 'arrivoDoppio')

coda.aggiungiTransizione('5', '4', 'servito')
coda.aggiungiTransizione('4', '3', 'servito')
coda.aggiungiTransizione('3', '2', 'servito')
coda.aggiungiTransizione('2', '1', 'servito')
coda.aggiungiTransizione('1', '0', 'servito')
coda.aggiungiTransizione('0', '0', 'servito')

coda.definisciStatoIniziale('0')

import random
eventi = ('arrivoSingolo', 'arrivoDoppio', 'servito')
for _ in range(1000000):
  evento = random.choices(eventi)[0]
  coda.aggiornaStato(evento)

coda.statisticheStati()