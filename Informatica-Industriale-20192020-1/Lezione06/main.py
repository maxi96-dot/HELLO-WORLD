from Lezione06.automata import Automata 
import random

I = ('a', 'b', 'c')
N = 100

L1 = Automata('Linguaggio L1')

print(f'----------------------------------------------------------------------------')
print(f'AUTOMA: {L1.getAutomataName()}')
print(f'----------------------------------------------------------------------------')

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

count = 0
s = ''
for _ in range(N):
  i = random.choices(I)[0]
  L1.update(i)
  s = s + f'-{i}'
  count += 1
  if count % 40 == 0:
    print(s)
    s = ''
    
if s != '':
  print(s)

if L1.getStateName() == 'A2':
  print(f'Complimenti! Ho trovato la stringa!')
else:
  print(f'Sono spiacente, ma la stringa abba non è presente in x')


L2 = Automata('Linguaggio L2')

print(f'----------------------------------------------------------------------------')
print(f'AUTOMA: {L2.getAutomataName()}')
print(f'----------------------------------------------------------------------------')

L2.addState('P')
L2.addState('C1')
L2.addState('C2')

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

count = 0
s = ''
for _ in range(N):
  i = random.choices(I)[0]
  L2.update(i)
  s = s + f'-{i}'
  count += 1
  if count % 40 == 0:
    print(s)
    s = ''
    
if s != '':
  print(s)

if L2.getStateName() == 'C2':
  print(f'Complimenti! Ho trovato la stringa!')
else:
  print(f'Sono spiacente, ma la stringa x non termina con cc')


print(f'----------------------------------------------------------------------------')
print(f'AUTOMA: {L1.getAutomataName()} UNITO {L2.getAutomataName()}')
print(f'----------------------------------------------------------------------------')

L1.resetSoft()
L2.resetSoft()

L1.initialize('S')
L2.initialize('P')

count = 0
s = ''
for _ in range(N):
  i = random.choices(I)[0]
  L1.update(i)
  L2.update(i)
  s = s + f'-{i}'
  count += 1
  if count % 40 == 0:
    print(s)
    s = ''
    
if s != '':
  print(s)

if L2.getStateName() == 'C2' or L1.getStateName() == 'A2':
  print(f'Complimenti! Ho trovato la stringa!')
else:
  print(f'Sono spiacente, ma la stringa x non appartiene al linguaggio')


print(f'----------------------------------------------------------------------------')
print(f'AUTOMA: {L1.getAutomataName()} INTERSECATO {L2.getAutomataName()}')
print(f'----------------------------------------------------------------------------')

L1.resetSoft()
L2.resetSoft()

L1.initialize('S')
L2.initialize('P')

count = 0
s = ''
for _ in range(N):
  i = random.choices(I)[0]
  L1.update(i)
  L2.update(i)
  s = s + f'-{i}'
  count += 1
  if count % 40 == 0:
    print(s)
    s = ''
    
if s != '':
  print(s)

if L2.getStateName() == 'C2' and L1.getStateName() == 'A2':
  print(f'Complimenti! Ho trovato la stringa!')
else:
  print(f'Sono spiacente, ma la stringa x non appartiene al linguaggio')

print(f'----------------------------------------------------------------------------')
print(f'AUTOMA: {L1.getAutomataName()} x {L2.getAutomataName()}')
print(f'----------------------------------------------------------------------------')

L1.resetSoft()
L2.resetSoft()

L1States = L1.getStates()
L2States = L2.getStates()

countOut = dict()
countIn  = dict()

for s1Name in L1States:
  for s2Name in L2States:
    countOut[s1Name, s2Name] = 0
    for i in I:
      s1 = L1States[s1Name]
      s2 = L2States[s2Name]
      countOut[s1Name, s2Name] += 1
      c1Name = s1.getTransitions()[i].getChildName()
      c2Name = s2.getTransitions()[i].getChildName()
      if not (c1Name, c2Name) in countIn.keys():
        countIn[c1Name, c2Name] = 0
      countIn[c1Name, c2Name] += 1
      print(f'({s1Name},{s2Name}) -- {i} --> ({c1Name},{c2Name})')


for s1Name in L1States:
  for s2Name in L2States:
    if (s1Name, s2Name) in countIn.keys():
      print(f'STATO ({s1Name},{s2Name}): Numero di Uscite {countOut[s1Name, s2Name]} Numero di Ingressi {countIn[s1Name, s2Name]}')
    #else:
    #  print(f'STATO ({s1Name},{s2Name}): Numero di Uscite {countOut[s1Name, s2Name]} Numero di Ingressi 0')


LB1 = Automata('Linguaggio LB1')
LB2 = Automata('Linguaggio LB2')

print(f'----------------------------------------------------------------------------')
print(f'AUTOMA: {LB1.getAutomataName()} e {LB2.getAutomataName()}')
print(f'----------------------------------------------------------------------------')

I = ('0', '1')

LB1.addState('S')
LB1.addState('A')
LB1.addState('B')

LB1.addTransition('0','S','S')
LB1.addTransition('1','S','A')
LB1.addTransition('0','A','B')
LB1.addTransition('1','A','A')
LB1.addTransition('0','B','B')
LB1.addTransition('1','B','B')

LB1.initialize('S')

LB2.addState('P')
LB2.addState('Q')
LB2.addState('R')

LB2.addTransition('0','P','Q')
LB2.addTransition('1','P','P')
LB2.addTransition('0','Q','Q')
LB2.addTransition('1','Q','R')
LB2.addTransition('0','R','Q')
LB2.addTransition('1','R','P')

LB2.initialize('P')

count = 0
s = ''
for _ in range(N):
  i = random.choices(I)[0]
  LB1.update(i)
  LB2.update(i)
  s = s + f'{i}'
  count += 1
  if count % 40 == 0:
    print(s)
    s = ''
    
if s != '':
  print(s)

L = LB1
print(f'Stato finale automa {L.getAutomataName()}: {L.getStateName()}')
L = LB2
print(f'Stato finale automa {L.getAutomataName()}: {L.getStateName()}')