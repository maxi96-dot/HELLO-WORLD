from ascensore import Ascensore

class CoppiaAscensori:
    def __init__(self, id1, id2):
        self.ascensore1 = Ascensore(id1)
        self.ascensore2 = Ascensore(id2)

    def sali(self, id_):
        if id_ == self.ascensore1.ritorna_id():
            self.ascensore1.sali()
        else:
            self.ascensore2.sali()

    def scendi(self, id_):
        if id_ == self.ascensore1.ritorna_id():
            self.ascensore1.scendi()
        else:
            self.ascensore2.scendi()

    def print_stato(self):
        print(
            f'Lo stato della coppia è {self.ascensore1.ritorna_stato_corrente()} - {self.ascensore2.ritorna_stato_corrente()}'
        )

    def processa_sequenza(self, comandi):
        if len(comandi) > 0:
            if comandi[0]['id'] == self.ascensore1.ritorna_id():
                if comandi[0]['comando'] == 'su':
                    self.ascensore1.sali()
                else:
                    self.ascensore1.scendi()
            else:
                if comandi[0]['comando'] == 'su':
                    self.ascensore2.sali()
                else:
                    self.ascensore2.scendi()
            self.processa_sequenza(comandi[1:])


edificio = CoppiaAscensori(1, 2)

comandi = [{'id': 1, 'comando': 'su'}, {'id': 1, 'comando': 'su'}]

edificio.processa_sequenza(comandi)
edificio.print_stato()

import random

tupla_comandi = ('su', 'giù')
tupla_id = (1, 2)
comandi = list()
for _ in range(20):
    comando = dict()
    comando['id'] = (random.choices(tupla_id))[0]
    comando['comando'] = (random.choices(tupla_comandi))[0]
    comandi.append(comando)

edificio.processa_sequenza(comandi)
edificio.print_stato()