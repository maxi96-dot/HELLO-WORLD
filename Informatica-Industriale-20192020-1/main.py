from Lezione06.automata import Automata 

alfabeto_transizioni = ('a', 'b', 'c')

L1 = Automata('Linguaggio L1')

L1.addState('S0')
L1.addState('A1')
L1.addState('B1')
L1.addState('B2')

L1.addTransition('a', 'S0',  'A1')
L1.addTransition('a', 'A1', 'A1')
L1.addTransition('a', 'B1', 'A1')
L1.addTransition('a', 'B2', 'B2')

L1.addTransition('b', 'S0', 'S0')
L1.addTransition('b', 'A1', 'B1')
L1.addTransition('b', 'B1', 'B2')
L1.addTransition('b', 'B2', 'S0')

L1.addTransition('c', 'S0',  'S0')
L1.addTransition('c', 'A1', 'S0')
L1.addTransition('c', 'B1', 'S0')
L1.addTransition('c', 'B2', 'S0')

L1.initialize('S0')

L2 = Automata('Linguaggio L2')

L2.addState('P0')
L2.addState('C1')
L2.addState('C2')

L2.addTransition('a','P0','P0')
L2.addTransition('a','C1','P0')
L2.addTransition('a','C2','P0')

L2.addTransition('b','P0','P0')
L2.addTransition('b','C1','P0')
L2.addTransition('b','C2','P0')

L2.addTransition('c','P0','C1')
L2.addTransition('c','C1','C2')
L2.addTransition('c','C2','C2')


L2.initialize('P0')

L1States = L1.getStates()
L2States = L2.getStates()

# Varinte per la ricerca di tutti gli stati irraggiungibili di un automa complesso ottenuto per composizione di più automi elementari

# Generazione della lista degli stati raggiungibili
#
# CAVEAT: per ogni stato deve essere specificata una transizione per ogni possibile ingresso
# CAVEAT: stati_irragiungibili[0] deve essere lo stato di partenza dell'automa da analizzare

stati_irragiungibili = list()
for s1Name in L1States:
  for s2Name in L2States:
    stato = (L1States[s1Name], L2States[s2Name])
    stati_irragiungibili.append(stato)
# stati_irragiungibili è la lista degli stati irragiungibili, inizialmente piena
stati_disponibili = list()
# stati_disponibili è la lista degli stati raggiungibili, inizialmente vuota
stati_da_esplorare = list()
# stati_da_esplorare è la lista temporanea degli stati spostati da stati_irragiungibili a stati_disponibili

stati_disponibili.append(stati_irragiungibili[0])
stati_da_esplorare.append(stati_irragiungibili[0])
stati_irragiungibili.remove(stati_irragiungibili[0])
# per definizione lo stato di partenza è raggiungibile
# stati_da_esplorare è costituito dallo stato di partenza

while(len(stati_da_esplorare) > 0): # ripeti finchè aggiungi nuovi stati raggiungibili
  lista_temporanea_da_esplorare = stati_da_esplorare            # salvo gli stati precedentemente aggiunti e 
  stati_da_esplorare = list()       # azzero stati_da_esplorare
  for stato in lista_temporanea_da_esplorare:  # Cerco tutti gli stati raggiungibili a partire dagli stati              
                   # precedentemente aggiunti
    transizioni_primo_sottostato = stato[0].getTransitions()
    transizioni_secondo_sottostato = stato[1].getTransitions()
    # -- INIZIO CORREZIONE (2019 11 15)
    for transizione in alfabeto_transizioni: 
      transizione1stato = transizioni_primo_sottostato[transizione]
      transizione2stato = transizioni_secondo_sottostato[transizione]
    # -- FINE CORREZIONE   (2019 11 15)
      nuovo_stato = (transizione1stato.getChild(), transizione2stato.getChild())
      # Se lo stato nuovo_stato non appartiene ancora agli stati raggiungibili, lo aggiungo
      if not nuovo_stato in stati_disponibili:
        stati_da_esplorare.append(nuovo_stato)
        stati_disponibili.append(nuovo_stato)
        stati_irragiungibili.remove(nuovo_stato)

print(f'STATI RAGGIUNGIBILI - Tabella delle transizioni')
print(f' STATO  |    a    |    b    |    c    ')
print(f' -------+---------+---------+---------')
for stato in stati_disponibili:
  dizionario_transizioni_1_stato =  stato[0].getTransitions()
  dizionario_transizioni_2_stato =  stato[1].getTransitions()
  outA1 = dizionario_transizioni_1_stato['a'].getChild().getName()
  outA2 = dizionario_transizioni_2_stato['a'].getChild().getName()

  outB1 = dizionario_transizioni_1_stato['b'].getChild().getName()
  outB2 = dizionario_transizioni_2_stato['b'].getChild().getName()

  outC1 = dizionario_transizioni_1_stato['c'].getChild().getName()
  outC2 = dizionario_transizioni_2_stato['c'].getChild().getName()

  print(f'({stato[0].getName()},{stato[1].getName()}) | ({outA1},{outA2}) | ({outB1},{outB2}) | ({outC1},{outC2})')

print(f' -------┴---------┴---------┴---------')

print(f'----')

print(f'STATI IRRAGGIUNGIBILI - Tabella delle transizioni')
print(f' STATO  |    a    |    b    |    c    ')
print(f' -------+---------+---------+---------')
for stato in stati_irragiungibili:
  outA1 = stato[0].getTransitions()['a'].getChild().getName()
  outA2 = stato[1].getTransitions()['a'].getChild().getName()

  outB1 = stato[0].getTransitions()['b'].getChild().getName()
  outB2 = stato[1].getTransitions()['b'].getChild().getName()

  outC1 = stato[0].getTransitions()['c'].getChild().getName()
  outC2 = stato[1].getTransitions()['c'].getChild().getName()

  print(f'({stato[0].getName()},{stato[1].getName()}) | ({outA1},{outA2}) | ({outB1},{outB2}) | ({outC1},{outC2})')

print(f' -------┴---------┴---------┴---------')