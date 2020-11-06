STATO = ('PIANO 0', 'PIANO 1', 'PIANO 2')

class Ascensore:
    def __init__(self, id_):
        self.id = id_
        self.STATO = 0
        print(f'L\'ascensore {self.id} viene acceso per la prima volta')
        print(f'L\'ascensore {self.id} si trova al piano {STATO[self.STATO]}')

    def sali(self):
        self.STATO += 1
        if self.STATO > 2:
            self.STATO = 2
        #print(f'L\'ascensore {self.id} si trova al piano {STATO[self.STATO]}')

    def scendi(self):
        self.STATO -= 1
        if self.STATO < 0:
            self.STATO = 0
        #print(f'L\'ascensore {self.id} si trova al piano {STATO[self.STATO]}')

    def print_stato_corrente(self):
        print(f'L\'ascensore {self.id} si trova al piano {STATO[self.STATO]}')

    def ritorna_stato_corrente(self):
        return self.STATO

    def ritorna_id(self):
        return self.id

    def processa_sequenza(self, comandi):
        if len(comandi) > 0:
            if comandi[0] == 'su':
                self.sali()
            else:
                self.scendi()
            self.processa_sequenza(comandi[1:])

if __name__ == '__main__':
  ascensore1 = Ascensore(1)
  ascensore2 = Ascensore(2)
  ascensore1.processa_sequenza(['su', 'su', 'su', 'giù'])
  ascensore2.processa_sequenza(['giù', 'su', 'su', 'giù'])
  
  import random
  
  tupla_comandi = ('su', 'giù')
  comandi = list()
  for _ in range(20):
    comandi.extend(random.choices(tupla_comandi))
    ascensore1.processa_sequenza(comandi)
