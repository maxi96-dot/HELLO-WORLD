class Transition:
    def __init__(self, name, parentNode, childNode):
        self.name = name
        self.parentNode = parentNode
        self.childNode = childNode
        self.numberOfActivations = 0
        
    def resetSoft(self):
        self.numberOfActivations = 0
        
    def resetHard(self, parentNode, childNode):
        self.parentNode = parentNode
        self.childNode = childNode
        self.numberOfActivations = 0
        
    def update(self):
        self.numberOfActivations += 1
        self.childNode.newVisit()
        return self.childNode
    
    def getNumberOfActivations(self):
        return self.numberOfActivations
    
    def getName(self):
        return self.name
    
    def getParentName(self):
        return self.parentNode.getName()
    
    def getChildName(self):
        return self.childNode.getName()

    def getChild(self):
        return self.childNode