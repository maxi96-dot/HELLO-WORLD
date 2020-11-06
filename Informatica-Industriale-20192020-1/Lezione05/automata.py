from Lezione05.state import State
from Lezione05.transition import Transition

class Automata:
  def __init__(self, automataName):
    self.name = automataName
    self.numberOfStates = 0
    self.states = dict()
    self.initialized = False
    self.currentState = None

  def addState(self, stateName):
    self.numberOfStates += 1
    self.states[stateName] = State(stateName)

  def addTransition(self, transitionName, parentName, childName):
    parentNode = self.states[parentName]
    childNode  = self.states[childName]
    transition = Transition(transitionName, parentNode, childNode)
    parentNode.addTransition(transition)

  def initialize(self, stateName):
    self.currentState = self.states[stateName]
    self.currentState.newVisit()
    self.initialized = True

  def update(self, transitionName):
    self.currentState = self.currentState.update(transitionName)

  def getStateName(self):
    return self.currentState.getName()

  def getState(self):
    return self.currentState

  def getName(self):
    return self.name

  def getAvailableTransitions(self):
    return list(self.currentState.getTransitions().keys())

  def getStates(self):
    return self.states

  def printReport(self):
    for stateName in self.states.keys():
      print(f'<<{stateName}>> ({self.states[stateName].getNumberOfVisits()})')
      transitions = self.states[stateName].getTransitions()
      for transition in transitions.keys():
        print(f'\t<<{transitions[transition].getParentNode().getName()}>> --> <<{transitions[transition].getChildNode().getName()}>> ({transitions[transition].getNumberOfActivations()})')


if __name__ == '__main__':
  lampadina = Automata('lampadina')
  lampadina.addState('OFF')
  lampadina.addState('ON')

  lampadina.addTransition('accendi', 'OFF', 'ON')
  lampadina.addTransition('spegni', 'ON', 'OFF')
  lampadina.initialize('OFF')

  lampadina.update('accendi')
  lampadina.update('spegni')
  lampadina.update('accendi')
  lampadina.update('spegni')
  lampadina.update('accendi')
  lampadina.update('spegni')
  lampadina.update('accendi')
  lampadina.update('spegni')
  lampadina.update('accendi')
  lampadina.update('spegni')
  lampadina.update('accendi')

  lampadina.printReport()

  ascensore = Automata('ascensore')
  ascensore.addState('0')
  ascensore.addState('1')
  ascensore.addState('2')
  ascensore.addState('3')

  ascensore.addTransition('sali', '0', '1')
  ascensore.addTransition('sali', '1', '2')
  ascensore.addTransition('sali', '2', '3')
  ascensore.addTransition('scendi', '3', '2') 
  ascensore.addTransition('scendi', '2', '1')
  ascensore.addTransition('scendi', '1', '0')

  ascensore.initialize('0')

  import random

  for _ in range(100000):
    #print(f'LO STATO CORRENTE E\' {ascensore.getStateName()}')
    comandi = ascensore.getAvailableTransitions()
    comando = random.choices(comandi)[0]
    ascensore.update(comando)

  ascensore.printReport()