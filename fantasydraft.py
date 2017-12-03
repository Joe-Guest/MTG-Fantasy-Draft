import datetime
from draft import draft
from player import drafter, competitor

draftList = []

def main():
  
  welcome()
  menu()

#Welcome screen to determine if there is already a draft 
def welcome():
  
  print('__________________________________________________\n')
  print('Welcome! This is the Fantasy Magic Draft homepage.')
  print('__________________________________________________\n')
  yesno = input('Is there a current draft? [y/n]: ')
  
  #Checks if there is a current draft
  if yesno.lower() == 'y' or yesno.lower() == 'yes':
	
    yesno = input('Would you like to import current draft? [y/n]: ')
	
    #If there is a current draft, asks to import it from file
    if yesno.lower() == 'y' or yesno.lower() == 'yes':
	  
      #Gets the name of the draft file and sends it to importDraft method
      file = input('Enter filename of draft you wish to import: ')
      importDraft(file)
  
  #If there isn't a current draft, asks if you would like to create one
  else:
  
    yesno = input('Would you like to start a new draft instead? [y/n]: ')
    
    if yesno.lower() == 'y' or yesno.lower() == 'yes':
      
      #Calls the make draft method if user wants to create a new draft
      makeDraft()

#Method to display a menu with options once a draft is established
def menu():

  exitmenu = False

  #Shows the menu until the user decides to quite
  while not exitmenu:

    print('__________________________________________________\n')
    print('#################   MENU   #######################')
    print('__________________________________________________\n')

    print('1) Update')
    print('2) View Draft')
    print('3) Save Draft')
    print('4) Exit')
    selection = input('Make a selection: ')

    #Asks for url to update from and passes it to the current drafts update method
    if selection == '1':

      url = input('Paste URL: ')
      draftList[0].update(url)
    
    #Prints the draft's info
    elif selection == '2':

      print(draftList[0])
      draftList[0].printDraft()

    #Saves the current draft
    elif selection == '3':

      saveDraft(draftList[0])

    #Sets exitmenu to true to break the loop and exit the program
    else:

      exitmenu = True
      
#Method to create a new draft if one doesn't exist
def makeDraft():
  
  print('__________________\n')
  print('New Draft Creation')
  print('__________________\n')
  
  #Asks for the name and format of the new draft and datestamps it
  name = input('Please enter the name of the tournament you\'ll be drafting: ')
  format = input('Please enter the format of the tournament: ')
  date = str(datetime.date.today())
  
  print('\nCreating new draft')
  
  #Creates new draft with inputed parameters and adds it to the master draft list
  newDraft = draft(name, format, date, None)
  draftList.append(newDraft)
  
  print('\nDraft created!')
  
  #Runs method to add drafters to the new draft
  addDrafters(newDraft)
  
  #Prompts user to add competitors to the drafters team now or later  
  yesno = input('\nAdd players to teams now? [y/n]: ')
  
  if yesno.lower() == 'y' or yesno.lower() == 'yes':
  
    #Runs method to add competitors to teams if prompted by user
    addCompetitors(newDraft)

  #Prompts user to save the new draft to file
  yesno = input('\n Would you like to save this draft? y/n: ')	
  
  if yesno.lower() == 'y' or yesno.lower() == 'yes':

    #Runs method to save the draft to file and passes the new draft
    saveDraft(newDraft)

  #testDraft(newDraft)

#Method to add drafters to a new draft  
def addDrafters(dft):
  
  #Asks user total number of people that will be drafting
  numDrafters = int(input('\nHow many people will be drafting?: '))
  
  print('\n____________\n')
  print('Add Drafters')
  print('____________\n')
  
  #Prompts user for the names of each drafter up to the total number of drafters they specified 
  for x in range(0, numDrafters):
    
    first = input('Enter drafter ' + str(x+1) + '\'s first name: ')
    last = input('Enter drafter ' + str(x+1) + '\'s last name: ')
    print('___________________________________________')
	
    #Creates a new drafter with user defined input and adds them to the draft
    newDrafter = drafter(first, last, None)
    dft.addDrafter(newDrafter)

#Method to add competitors to individual drafters' team    
def addCompetitors(dft):
  
  #Asks user total number of competitors on each team and displays default
  numMembers = int(input('\nHow many members are on a team? [Default 8]: '))
  
  print('\n____________\n')
  print('Create Teams')
  print('____________\n')
  
  #Selects each drafter in the draft to set up individual teams
  for drafter in dft.drafters:
    
    #Displays the name of the drafter whos team is being created
    print('Creating team for ' + drafter.fullName() + ':\n')
    
    #Prompts user for competitor information for each competitor up to the team size they specified
    for x in range(0, numMembers):
      
      first = input('Enter competitor ' + str(x+1) + '\'s first name: ')
      last = input('Enter competitor ' + str(x+1) + '\'s last name: ')
      team = input('Enter ' + first + ' ' + last + '\'s team name: ')
      rank = input('Enter  ' + first + ' ' + last + '\'s rank [Platinum = 3, Gold = 2, Other = 1: ')
      yesno = input('Is  ' + first + ' ' + last + ' in the Hall of Fame? [y/n]: ')
        
      if yesno.lower() == 'y' or yesno.lower() == 'yes':
        
        HoF = True  

      else:

        HoF = False  
        
      print('___________________________________________')
      
      #Creates a new competitor with user defined input and adds them to the selected drafter's team      
      newCompetitor = competitor(first, last, team, int(rank), HoF)
      drafter.addMember(newCompetitor)

#Method to import draft from file
def importDraft(file):
  
  #Opens draft file specified by user
  draftFile = open(file, 'r')
  draftInfo = draftFile.readlines()
  
  #Gets the first line of the file and the date to set up a new draft
  name,format,date,line = draftInfo[0].split(':')

  #Instantiates a new draft
  importDraft = draft(name, format, date, None)
  
  #Sends the new draft and draft info to create the list of drafters and competitors
  del draftInfo[0]
  readPlayers(importDraft, draftInfo)
  
  #Adds the new draft to the master draft list
  draftList.append(importDraft)
  
  draftFile.close()
  
  #This line is just for testing
  #testDraft(importDraft)
  
#Method to read players and put them in their appropriate lists 
def readPlayers(dft, data):
  
  #Checks imported draft data line by line
  for line in data:
    
    #Parses data
    id,first,last,line = line.split(':')

    #Checks if a line contains information about a drafter and adds them to the draft list
    if id == 'D':

      newDrafter = drafter(first, last, None)
	  
      dft.addDrafter(newDrafter)
    #Checks if a lline contains information about a competitor and adds them to the current drafters team list
    elif id == 'C':

      readTeam(newDrafter)

#Method to read each drafter's team from file
def readTeam(dftr):

  filename = dftr.firstName + dftr.lastName + '.txt'
  #recordname = dftr.firstName + dftr.lastName + 'records.txt'
  print(filename)

  #recordFile = open(recordname, 'r')
  with open(filename, 'r') as teamFile:

    for line in teamFile:

      # Parses data
      first, last, team, rank, isHoF, line = line.split(':')

      newCompetitor = competitor(first, last, team, int(rank), bool(isHoF))
      dftr.addMember(newCompetitor)

#Method to save draft to a file for later import
#TODO: Add functionality to save stats
def saveDraft(dft):
  
  #Prompts user for file name and opens specified file
  file = input('Enter name to save as: ') + '.txt'
  draftFile = open(file, 'w')
  
  #Writes draft information to the first line
  draftFile.write(dft.name + ':' + dft.format + ':' + dft.date + ':\n')
  
  #Finds each drafter and writes their information to the next line
  for drafter in dft.drafters:

    draftFile.write('D:' + drafter.firstName + ':' + drafter.lastName +':\n')
	
    #Checks to see if selected drafter has a team
    if drafter.team is not None:
    
      #If the drafter has a team, writes a line to the file and calls saveTeam method passing the selected drafter
      draftFile.write('C:' + drafter.firstName + ':' + drafter.lastName +':\n')
      saveTeam(drafter)
	
  #Closes the file when complete
  draftFile.close()

#Method to save each team to its own file for later import
def saveTeam(dftr):

  #File name saved as drafters first and last name
  filename = dftr.firstName + dftr.lastName + '.txt'
  #recordname = dftr.firstName + dftr.lastName + 'records.txt'

  #recordFile = open(recordname, 'w')
  #recordFile.write(dftr.wins + ':' + dftr.draws + ':' + dftr.losses)
  
  #Opens team file with 'with' to automatically close when all members of the team are written
  with open(filename, 'w') as teamFile:
    
    #Writes infromation about each competitor in passed drafter's team to a new line
    for member in dftr.team:

      teamFile.write(member.firstName + ':' + member.lastName  + ':' + member.team + ':' + str(member.rank) + ':' + str(member.isHoF) + ':\n')
      #recordFile.write(member.wins + ':' + member.draws + ':' + member.losses)

  #recordFile.close()

#This method is for testing only
"""
def testDraft(dft):
  
  print(dft)
  dft.printDraft()
  print(dft.drafters[0].team[0].record())
  dft.update()
  print(dft.drafters[0].team[0].record())
  #print(dft.drafters[0].team[5].fullName())
"""
main()