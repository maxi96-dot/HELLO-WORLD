import random
import math
import matplotlib.pyplot as plt

from automata import Automata

class Pos:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Source:
  def __init__(self, sourceName, pos, data):
    self.pos = pos
    self.name = sourceName
    self.data = data

  def getPos(self):
    return self.pos
  
  def getName(self):
    return self.name

  def getData(self, pos):
    return (self.data / ( (pos.x - self.pos.x)**2 + (pos.y - self.pos.y)**2) )*(1 + (random.random() - 0.5)/40)

  def setData(self, data):
    self.data = data

class Sensor:
  def __init__(self, sensorName, pos):
   self.pos = pos
   self.name = sensorName

   self.automa = Automata(f'Stato del sensore {sensorName}')
   self.automa.addState('READY')
   self.automa.addState('SLEEP')
   self.automa.addTransition('CAMBIA_STATO', 'SLEEP', 'READY')
   self.automa.addTransition('CAMBIA_STATO', 'READY', 'SLEEP')
   self.automa.initialize('READY')

   self.data = 0

  def getName(self):
    return self.name

  def getStateName(self):
    return self.automa.getStateName()

  def setPos(self, pos):
    self.pos = pos

  def update(self):
    self.automa.update('CAMBIA_STATO')

  def getData(self, sourceList):
    if self.automa.getStateName() == 'READY':
      self.data = 0
      for source in sourceList:
        self.data += source.getData(self.pos)
    return self.data


sourceList = list()

pos = Pos(0,0)
source = Source('sorgente 1', pos, 10.0)
sourceList.append(source)

pos = Pos(0,100)
source = Source('sorgente 2', pos, 10.0)
sourceList.append(source)

pos = Pos(100,0)
source = Source('sorgente 3', pos, 10.0)
sourceList.append(source)

pos = Pos(100,100)
source = Source('sorgente 4', pos, 10.0)
sourceList.append(source)

pos = Pos(50, 50)
sensore = Sensor('sensore di prova', pos)

datoLetto = sensore.getData(sourceList)

print(f'Il valore letto dal sensore {sensore.getName()} è {datoLetto}')

pos = Pos(50, 100)
sensore = Sensor('sensore di prova', pos)

datoLetto = sensore.getData(sourceList)

print(f'Il valore letto dal sensore {sensore.getName()} è {datoLetto}')


sensori = list()
indice = 0

for x in range(25, 100, 25):
  for y in range(25, 100, 25):
    pos = Pos(x, y)
    indice += 1
    sensore = Sensor(f'Sensore {indice}', pos)
    sensori.append( (sensore, list()) )

for tuplaSensore in sensori:
  sensore = tuplaSensore[0]
  print(f'VALORE LETTO DAL SENSORE {sensore.getName()}: {sensore.getData(sourceList)}')


pos = Pos(50, 50)
sensore = Sensor('Sensore Mobile', pos)

tempi = list()
valori = list()
x0 = -50
y0 = 50

x = x0
y = y0
sensore.setPos(Pos(x, y))
for t in range(200):
  tempi.append(t)
  data = sensore.getData(sourceList)
  valori.append(data)
  x += 1
  y += 0
  pos = Pos(x, y)
  sensore.setPos(pos)


fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(tempi, valori)

fig.savefig('graph1.png')
