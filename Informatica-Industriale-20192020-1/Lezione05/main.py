from Lezione05.automata import Automata
import random

numeroCasse = 1
casse = list()

rateDiArrivo = 2.0
rateDiServizio = 2.0/(numeroCasse**1.12)

tempoNuovoArrivo    = random.expovariate(rateDiArrivo)
tempoEventoAttuale  = tempoNuovoArrivo
tempoNuovoServizio  = list()

for idxCassa in range(numeroCasse):
  cassa = Automata('cassa ' + str(idxCassa))

  cassa.addState('vuota')
  cassa.addState('1')
  cassa.addState('2')
  cassa.addState('3')
  cassa.addState('4')
  cassa.addState('5')

  cassa.addTransition('arrivo', 'vuota', '1')
  cassa.addTransition('arrivo', '1', '2')
  cassa.addTransition('arrivo', '2', '3')
  cassa.addTransition('arrivo', '3', '4')
  cassa.addTransition('arrivo', '4', '5')
  cassa.addTransition('arrivo', '5', '5')

  cassa.addTransition('servito', '5', '4')
  cassa.addTransition('servito', '4', '3')
  cassa.addTransition('servito', '3', '2')
  cassa.addTransition('servito', '2', '1')
  cassa.addTransition('servito', '1', 'vuota')

  cassa.initialize('vuota')
  casse.append(cassa)
  tempoNuovoServizio.append(0)

totaleArrivi = 0
for _ in range(100000):

  for idxCassa in range(numeroCasse):
    cassa = casse[idxCassa]
    if tempoEventoAttuale == tempoNuovoServizio[idxCassa]:
      cassa.update('servito')
      if cassa.getStateName() != 'vuota':
        tempoNuovoServizio[idxCassa] = tempoEventoAttuale + random.expovariate(rateDiServizio)

  if tempoEventoAttuale == tempoNuovoArrivo:
    totaleArrivi += 1
    idxCassa = random.choices([idx for idx in range(numeroCasse)])[0]
    cassa = casse[idxCassa]
    if cassa.getStateName() == 'vuota':
      tempoNuovoServizio[idxCassa] = tempoEventoAttuale + random.expovariate(rateDiServizio)
    cassa.update('arrivo')
    tempoNuovoArrivo += random.expovariate(rateDiArrivo)

  tempoEventoAttuale = tempoNuovoArrivo

  for idxCassa in range(numeroCasse):
    cassa = casse[idxCassa]
    if cassa.getStateName() != 'vuota':
      tempoEventoAttuale = min(tempoEventoAttuale, tempoNuovoServizio[idxCassa])

#for idxCassa in range(numeroCasse):
 # cassa = casse[idxCassa]
  #cassa.printReport()

totaleDrop = 0
for idxCassa in range(numeroCasse):
  cassa = casse[idxCassa]
  totaleDrop += cassa.getStates()['5'].getTransitions()['arrivo'].getNumberOfActivations()

print(f'Percantuale di drop = {100.0*totaleDrop/totaleArrivi}')