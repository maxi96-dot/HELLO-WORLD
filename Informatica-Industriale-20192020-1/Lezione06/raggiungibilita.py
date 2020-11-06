from Lezione06.automata import Automata 

I = ('a', 'b', 'c')

L1 = Automata('Linguaggio L1')

L1.addState('S')
L1.addState('A1')
L1.addState('B1')
L1.addState('B2')
L1.addState('A2')

L1.addTransition('a', 'S',  'A1')
L1.addTransition('a', 'A1', 'A1')
L1.addTransition('a', 'B1', 'A1')
L1.addTransition('a', 'B2', 'A2')
L1.addTransition('a', 'A2', 'A2')

L1.addTransition('b', 'S',  'S')
L1.addTransition('b', 'A1', 'B1')
L1.addTransition('b', 'B1', 'B2')
L1.addTransition('b', 'B2', 'S')
L1.addTransition('b', 'A2', 'A2')

L1.addTransition('c', 'S',  'S')
L1.addTransition('c', 'A1', 'S')
L1.addTransition('c', 'B1', 'S')
L1.addTransition('c', 'B2', 'S')
L1.addTransition('c', 'A2', 'A2')

L1.initialize('S')

L2 = Automata('Linguaggio L2')

L2.addState('P')
L2.addState('C1')
L2.addState('C2')
L2.addState('C4')

L2.addTransition('a','P', 'P')
L2.addTransition('a','C1','P')
L2.addTransition('a','C2','P')

L2.addTransition('b','P', 'P')
L2.addTransition('b','C1','P')
L2.addTransition('b','C2','P')

L2.addTransition('c','P', 'C1')
L2.addTransition('c','C1','C2')
L2.addTransition('c','C2','C2')

L2.initialize('P')

L1States = L1.getStates()
L2States = L2.getStates()

# Varinte per la ricerca di tutti gli stati irraggiungibili di un automa complesso ottenuto per composizione di più automi elementari

# Generazione della lista degli stati possibili

S = list()
for s1Name in L1States:
  for s2Name in L2States:
    stato = (L1States[s1Name], L2States[s2Name])
    S.append(stato)
# S è la lista degli stati irragiungibili, inizialmente piena
R = list()
# R è la lista degli stati raggiungibili, inizialmente vuota
A = list()
# A è la lista temporanea degli stati spostati da S a R

R.append(S[0])
A.append(S[0])
S.remove(S[0])
# per definizione lo stato di partenza è raggiungibile
# A è costituito dallo stato di partenza

while(len(A) > 0): # ripeti finchè aggiungi nuovi stati raggiungibili
  B = A            # salvo gli stati precedentemente aggiunti e 
  A = list()       # azzero A
  for stato in B:  # Cerco tutti gli stati raggiungibili a partire dagli stati precedentemente
                   # aggiunti
    transitions1 = stato[0].getTransitions()
    transitions2 = stato[1].getTransitions() 
    for t1 in transitions1.values():
      for t2 in transitions2.values():
        candidato = (t1.getChild(), t2.getChild())
        # Se lo stato candidato non appartiene ancora agli stati raggiungibili, lo aggiungo
        if not (candidato in R):
          A.append(candidato)
          R.append(candidato)
          S.remove(candidato)

for s in R:
  print(f'STATO RAGGIUNGIBILE ({s[0].getName()},{s[1].getName()})')

print(f'----')

for s in S:
  print(f'STATO NON RAGGIUNGIBILE ({s[0].getName()},{s[1].getName()})')