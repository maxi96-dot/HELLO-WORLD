from event import Event

class Clock:
  def __init__(self, name, T):
    self.name = name
    self.T    = T

  def start(self, T0):
    event = Event(T0, self)
    return event

  def update(self, event):
    print(f'TIK TOK {self.name}: {event.time}')
    event = Event(event.time + self.T, self)
    return event