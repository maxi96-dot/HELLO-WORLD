from stato import Stato

class Automa():

  def __init__(self):
    self.statoInizialeDefinito = False
    self.statoCorrenteDefinito = False
    self.tabellaStati = dict()

  def aggiungiStato(self, nomeStato):
    self.tabellaStati[nomeStato] = Stato(nomeStato)

  def aggiungiTransizione(self, nomeStatoPartenza, nomeStatoArrivo, nomeTransizione):
    statoPartenza = self.tabellaStati[nomeStatoPartenza]
    statoArrivo   = self.tabellaStati[nomeStatoArrivo]
    statoPartenza.aggiungiTransizione(nomeTransizione, statoArrivo)

  def definisciStatoIniziale(self, nomeStatoInziale):
    self.statoCorrente = self.tabellaStati[nomeStatoInziale]
    self.statoCorrente.inc()
    self.statoInizialeDefinito = True
    self.statoCorrenteDefinito = True

  def aggiornaStato(self, nomeTransizione):
    if self.statoInizialeDefinito & self.statoCorrenteDefinito:

      nuovoStato = self.statoCorrente.nuovoStato(nomeTransizione)
      #print(f'{self.statoCorrente.ritornaStato()} -- {nomeTransizione} --> {nuovoStato.ritornaStato()}')
      self.statoCorrente = nuovoStato

  def statisticheStati(self):
    for nomeStato in self.tabellaStati.keys():
      print(f'NUMERO VISITE NELLO STATO {nomeStato} = {self.tabellaStati[nomeStato].visite()}')


if __name__ == '__main__':
  lampadina = Automa()
  lampadina.aggiungiStato('spenta')
  lampadina.aggiungiStato('accesa')
  lampadina.aggiungiTransizione('accesa', 'accesa', 'accendi')
  lampadina.aggiungiTransizione('accesa', 'spenta', 'spegni')
  lampadina.aggiungiTransizione('spenta', 'accesa', 'accendi')
  lampadina.aggiungiTransizione('spenta', 'spenta', 'spegni')

  lampadina.definisciStatoIniziale('spenta')

  lampadina.aggiornaStato('spegni')
  lampadina.aggiornaStato('accendi')
  lampadina.aggiornaStato('accendi')
  lampadina.aggiornaStato('spegni')
  lampadina.aggiornaStato('spegni')

  lampadina.statisticheStati()