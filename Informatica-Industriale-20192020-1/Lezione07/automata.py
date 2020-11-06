from Lezione07.transition import Transition
from Lezione07.state import State

class Automata:
    def __init__(self, automataName):
        self.name = automataName
        self.numberOfStates = 0
        self.states = dict()
        self.initialized = False
        self.currentState = None

    def getAutomataName(self):
      return self.name

    def resetSoft(self):
        for stateName in self.states:
            state = self.states[stateName]
            state.resetSoft()
            transitions = state.getTransitions()
            for transitionName in transitions:
                transition = transitions[transitionName]
                transition.resetSoft()
        self.initialized = False
        self.currentState = None
                
    def resetHard(self):
        self.numberOfStates = 0
        self.states = dict()
        self.initialized = False
        self.currentState = None
        
    def addState(self, stateName):
        self.states[stateName] = State(stateName)
        
    def addTransition(self, transitionName, parentName, childName):
        self.states[parentName].addTransition(Transition(transitionName, self.states[parentName], self.states[childName]))
        
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
        return list(self.currentState.getAvailableTransitions().keys())
    
    def getStates(self):
        return self.states
    
    def printReport(self):
        for state in self.states.keys():
            print(f'STATO <<{state}>>: numero visite = {self.states[state].getNumberOfVisits()}')
            transitions = self.states[state].getTransitions()
            for transition in self.states[state].getAvailableTransitions():
                print(f' TRANSIZIONE: verso lo stato <<{transitions[transition].getChildName()}>> numero di attivazioni <<{transitions[transition].getNumberOfActivations()}>>')