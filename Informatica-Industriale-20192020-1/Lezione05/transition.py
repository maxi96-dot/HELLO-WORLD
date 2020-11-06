class Transition:
  def __init__(self, transitionName, parentNode, childNode):
    self.name = transitionName
    self.parentNode = parentNode
    self.childNode  = childNode
    self.numberOfActivations = 0

  def update(self):
    self.childNode.newVisit()
    self.numberOfActivations += 1
    return self.childNode

  def getNumberOfActivations(self):
    return self.numberOfActivations

  def getName(self):
    return self.name
  
  def getParentNode(self):
    return self.parentNode

  def getChildNode(self):
    return self.childNode

if __name__ == '__main__':
  from stato import Stato
  
  acceso = Stato('acceso')
  spento = Stato('spento')

  accendi = Transition('accendi', spento, acceso)
  spegni  = Transition('spegni', acceso, spento)

  acceso.addTransition(spegni)
  spento.addTransition(accendi) 

  statoCorrente = spento
  statoCorrente.newVisit()
  print(f'LO STACO CORRENTE E\' {statoCorrente.getName()}  - {statoCorrente.getNumberOfVisits()}')
  statoCorrente = statoCorrente.update('accendi')
  print(f'LO STACO CORRENTE E\' {statoCorrente.getName()} - {statoCorrente.getNumberOfVisits()}')
  statoCorrente = statoCorrente.update('spegni')
  print(f'LO STACO CORRENTE E\' {statoCorrente.getName()} - {statoCorrente.getNumberOfVisits()}')