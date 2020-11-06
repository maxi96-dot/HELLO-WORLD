class State:
    def __init__(self, stateName):
        self.name = stateName
        self.transitions = dict()
        self.numberOfTransitions = 0
        self.numberOfVisits = 0
        
    def resetSoft(self):
        self.numberOfTransitions = 0
        self.numberOfVisits = 0
        
    def resetHard(self):
        self.transitions = dict()
        self.numberOfTransitions = 0
        self.numberOfVisits = 0
        
    def addTransition(self, transition):
        self.transitions[transition.getName()] = transition
        
    def update(self, transition):
        return self.transitions[transition].update()
    
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
    
    def getAvailableTransitions(self):
        return self.transitions