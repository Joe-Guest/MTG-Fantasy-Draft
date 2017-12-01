from player import player, drafter

class draft:

  def __init__(self, name, format, date, drafters = None):
    
    self.name = name
    self.format = format
    self.date = date
	
    if drafters is None:
	  
      self.drafters = []
	
    else:
	  
      self.drafters = drafters

  def __str__(self):
    
    return ('{} - {}').format(self.name, self.format)

  def addDrafter(self, drafter):
    
    self.drafters.append(drafter)

  #Method to remove drafters from a draft
  def removeDrafter(self, drafter):
    
    self.drafters.remove(drafter)

  def printDrafters(self):
    
    for drafter in self.drafters:
	  
      print(drafter.fullName())
      drafter.printTeam()