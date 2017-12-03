#from player import player, drafter
from tableimporter import dataTable

class draft:

  #Initiates a new draft with a blank list of drafters if a list is not provided
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

  #Method to add a new drafter to the draft
  def addDrafter(self, drafter):
    
    self.drafters.append(drafter)

  #Method to remove drafters from a draft
  def removeDrafter(self, drafter):
    
    self.drafters.remove(drafter)

  #Method to print all drafters, teams, and records for each in the draft
  def printDraft(self):
    
    for drafter in self.drafters:
	  
      print('\n#########' + drafter.fullName() + '#########\n')
      print(drafter.record())

      print('\n######### TEAM #########\n')
      for member in drafter.team:

        print(member.fullName())
        print(member.record())

  #Method to update records from a URL
  def update(self, url):

    #Sets up translation table to clean winloss data  
    translation_table = dict.fromkeys(map(ord, '][\''), None)
    #Gets a table (actually dataframe) from tableimporter passing the URL
    table = dataTable().getData(url)

    #Must check each drafter's team for updates
    for drafter in self.drafters:

      for member in drafter.team:
        
        #Checks if member name is found in index 1 of the table
        playerData = table[table[1] == (member.lastName + ', ' + member.firstName)]
        
        #If the member name isn't found it will return empty, if it is found it will get the winloss data from the same index
        if not playerData.empty:

          #print(playerData)
          #print('player data 3')
          
          #Gets the winloss data from the correct column
          playerData = str(playerData[3].values)
          
          #Cleans the winloss data of extra characters using the translation table
          playerData = playerData.translate(translation_table)
          #print(playerData)

          #Cleans the winloss data from the match record
          winloss,record = playerData.split()
          
          #Checks the winloss data and adds wins and points if points are awarded
          if winloss == 'Won':

            drafter.win(member.rank)
            member.win()
            print(member.fullName() + ' WON!')

          elif winloss == 'Lost':

            drafter.lose()
            member.lose()
            print(member.fullName() + ' Lost :(')

          elif winloss == 'Draw':

            drafter.draw()
            member.draw()
            print(member.fullName() + ' Drew :/')

          else:

            drafter.win(member.rank)
            member.win()
            print(member.fullName() + ' had a bye')
        
        #Does the same thing as above but for column 5, and inverts the winloss logic because if "Won" is in column 3 the competitor in column 1 won, where as a "Lost" in column 3 means that the player in column 5 won
        else:

          opponentData = table[table[5] == (member.lastName + ', ' + member.firstName)]

          if not opponentData.empty:

            #print(opponentData)
            #print('player data 3')
            opponentData = str(opponentData[3].values)
            opponentData = opponentData.translate(translation_table)
            #print(opponentData)

            winloss,record = opponentData.split()

            if winloss == 'Lost':

              drafter.win(member.rank)
              member.win()
              print(member.fullName() + ' WON!')

            elif winloss == 'Win':

              drafter.lose()
              member.lose()
              print(member.fullName() + ' Lost :(')

            else:

              drafter.draw()
              member.draw()
              print(member.fullName() + ' Drew :/')
          
          #Catch all for if a member is not found in the competition
          else:

            print('No Data Found')
