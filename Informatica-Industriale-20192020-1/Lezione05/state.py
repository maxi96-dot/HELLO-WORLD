class State:
  def __init__(self, stateName):
    self.name = stateName
    self.transitions = dict()
    self.numberOfTransitions = 0
    self.numberOfVisits = 0

  def addTransition(self, transition):
    self.numberOfTransitions += 1
    self.transitions[transition.getName()] = transition

  def update(self, transitionName):
    return self.transitions[transitionName].update()

  def getTransitions(self):
    return self.transitions

  def getNumberOfTransitions(self):
    return self.numberOfTransitions

  def getNumberOfVisits(self):
    return self.numberOfVisits

  def newVisit(self):
    self.numberOfVisits += 1

  def getName(self):
    return self.name

if __name__ == '__main__':
  stato = State('prova')
  print(f'HO CREATO LO STATO {stato.getName()}')
  print(f'Numero di transizioni {stato.getNumberOfTransitions()}')
  print(f'Numero di visite {stato.getNumberOfVisits()}')