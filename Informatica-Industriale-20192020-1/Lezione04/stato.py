class Stato:

  def __init__(self, nome):
    self.nomeStato = nome
    self.numeroVisite = 0
    self.tabellaTransizioni = dict()

  def inc(self):
    self.numeroVisite += 1

  def visite(self):
    return self.numeroVisite

  def nuovoStato(self, nomeTransizione):
    if nomeTransizione in self.tabellaTransizioni.keys():
      nuovoStato = self.tabellaTransizioni[nomeTransizione]
      nuovoStato.inc()
      return nuovoStato
    else:
      print(f'ERROR: TRANSIZIONE {nomeTransizione} NON PRESENTE')
      exit(0)

  def aggiungiTransizione(self, nomeTransizione, nuovoStato):
    if nomeTransizione in self.tabellaTransizioni.keys():
      return
    self.tabellaTransizioni[nomeTransizione] = nuovoStato

  def ritornaStato(self):
    return self.nomeStato

if __name__ == '__main__':

  statoAcceso = Stato('acceso')
  statoSpento = Stato('spento')

  statoSpento.aggiungiTransizione('accendi', statoAcceso)
  statoSpento.aggiungiTransizione('spegni', statoSpento)
  statoAcceso.aggiungiTransizione('spegni', statoSpento)
  statoAcceso.aggiungiTransizione('accendi', statoAcceso)

  Interruttore = statoSpento
  Interruttore.inc()

  print(f'STATO CORRENTE: {Interruttore.ritornaStato()}')

  Interruttore = Interruttore.nuovoStato('accendi')

  print(f'STATO CORRENTE: {Interruttore.ritornaStato()}')

  Interruttore = Interruttore.nuovoStato('accendi')
  Interruttore = Interruttore.nuovoStato('spegni')
  Interruttore = Interruttore.nuovoStato('spegni')
  Interruttore = Interruttore.nuovoStato('accendi')
  Interruttore = Interruttore.nuovoStato('accendi')

  print(f'STATO CORRENTE: {Interruttore.ritornaStato()}')

  print(f'NUMERO VISITE STATO ACCESO {statoAcceso.visite()}')
  print(f'NUMERO VISITE STATO SPENTO {statoSpento.visite()}')