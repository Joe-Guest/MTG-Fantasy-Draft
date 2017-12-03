import config as stng

#Parent class definition
class player:
  
  matches = 0
  wins = 0
  draws = 0
  losses = 0
  points = 0

  #All players must have a first name, last name, and team 
  def __init__(self, firstName, lastName, team=None):
    
    self.firstName = firstName
    self.lastName = lastName
	
    self.winPoints = 3
    self.drawPoints = 1
    
    if team is None:
	  
      self.team = []
    
    else:
	  
      self.team = team
  
  #Returns the first and last name of the player
  def fullName(self):
    
    return '{} {}'.format(self.firstName, self.lastName)
  
  #Returns the individual record of the player
  def record(self):
    
    return '{} - {} - {} Total Points: {}'.format(self.wins, self.draws, self.losses, self.points)

  #Adds a win to individual wins
  def win(self):
    
    self.matches += 1
    self.wins += 1
    self.addPoints(winPoints)

  #Adds a draw to individual draws
  def draw(self):
    
    self.matches += 1
    self.draws += 1
    self.addPoints(drawPoints)

  #Adds a loss to individual losses	
  def lose(self):
    
    self.matches += 1
    self.losses += 1
  
  def addPoints(self, points):
    
    self.points += points

#Subclass for those in the fantasy draft 
class drafter(player):

  #Sets variables for total combined record of team
  winsTotal = 0
  drawsTotal = 0
  lossesTotal = 0

  def calcRecord(self):
  
    for member in self.team:
	  
      self.matches += member.matches
      self.winsTotal += member.wins
      self.drawsTotal += member.draws
      self.lossesTotal += member.losses

#Method to calculate points based on rank of team members instead of using default point values
  def calcPoints(self, rank):
	
	#Platinum or gold hall of famers
    if rank >= 3:
	  
      self.addPoints(stng.platinumWinPoints)
	
    #Gold or other hall of famers	
    elif rank == 2:
	  
      self.addPoints(stng.goldWinPoints)
	
    #Everyone else	
    else:
	
      self.addPoints(stng.otherWinPoints)

  #Method to add members to a team
  def addMember(self, member):
  
    self.team.append(member)

  #Method to remove members from a team	
  def removeMember(self, member):
  
    self.team.remove(member)

  #Overrides default win method so that correct point value can be added
  def win(self, rank):
    
    self.wins += 1
    self.calcPoints(rank)
	
  def printTeam(self):
    
    for member in self.team:
	  
      print('-->' + member.fullName())

#Subclass for those competeing in the tournament
class competitor(player):
  
  def __init__(self, firstName, lastName, team=None, rank=0, isHoF=False):
    
    super().__init__(firstName, lastName, team)
    
    if rank == 0:
    
      self.rank = 0
    
    else:
      
      self.rank = rank
      
    if isHoF == False:
    
      self.isHoF = False
      
    else:
    
      self.isHoF = isHoF
      rank += 1
  
	
