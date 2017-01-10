class Todo:
  def __init__(self, name, id=None):
    self.id = id
    self.name = name
    
  def updateName(self, new_name):
    self.name = new_name
    