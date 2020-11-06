from event import Event

class Oracle:
  def __init__(self, interval, env):
    self.actorList = list()
    self.interval = interval
    self.env = env

  def start(self, t0):
    event = Event(t0, self)
    return event

  def addActor(self, actor):
    self.actorList.append(actor)

  def update(self, event):
    for actor in self.actorList:
      actor.update(event, self.env)
    event = Event(event.time + self.interval, self)
    return event