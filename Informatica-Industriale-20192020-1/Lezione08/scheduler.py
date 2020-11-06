class Scheduler:
  def __init__(self):
    self.eventList = list()

  def addEvent(self, event):
    self.eventList.append(event)

  def nextEvent(self):
    firstEvent = None
    for event in self.eventList:
      if firstEvent == None:
        firstEvent = event
      else:
        if event.time < firstEvent.time:
          firstEvent = event

    self.eventList.remove(firstEvent)
    return firstEvent