import datetime
from draft import draft
from player import player, drafter, competitor

draftList = []

def main():
  
  welcome()

def welcome():
  
  print('__________________________________________________\n')
  print('Welcome! This is the Fantasy Magic Draft homepage.')
  print('__________________________________________________\n')
  yesno = input('Is there a current draft? [y/n]: ')
  
  if yesno.lower() == 'y' or yesno.lower() == 'yes':
	
    yesno = input('Would you like to import current draft? [y/n]: ')
	
    if yesno.lower() == 'y' or yesno.lower() == 'yes':
	  
      file = input('Enter filename of draft you wish to import: ')
      importDraft(file)
  
  else:
  
    yesno = input('Would you like to start a new draft instead? [y/n]: ')
    
    if yesno.lower() == 'y' or yesno.lower() == 'yes':
      
      makeDraft()

def makeDraft():
  
  print('__________________\n')
  print('New Draft Creation')
  print('__________________\n')
  
  name = input('Please enter the name of the tournament you\'ll be drafting: ')
  format = input('Please enter the format of the tournament: ')
  date = str(datetime.date.today())
  
  print('\nCreating new draft')
  
  newDraft = draft(name, format, date, None)
  
  print('\nDraft created!')
  
  numDrafters = int(input('\nHow many people will be drafting?: '))
  
  print('\n____________\n')
  print('Add Drafters')
  print('____________\n')
  
  for x in range(0, numDrafters):
    
    first = input('Enter drafter ' + str(x+1) + '\'s first name: ')
    last = input('Enter drafter ' + str(x+1) + '\'s last name: ')
    print('___________________________________________')
	
    newDrafter = drafter(first, last, None)
    newDraft.addDrafter(newDrafter)

  yesno = input('\n Would you like to save this draft? y/n: ')	
  
  if yesno.lower() == 'y' or yesno.lower() == 'yes':

    saveDraft(newDraft)
  """
  yesno = input('\nAdd players to teams now? [y/n]: ')
  
  if yesno.lower() == 'y' or yesno.lower() == 'yes':
  """  
    

  testDraft(newDraft)
  

#Method to import draft from file
def importDraft(file):
  
  #Opens draft file specified by user
  draftFile = open(file, 'r')
  draftInfo = draftFile.readlines()
  
  #Gets the first line of the file and the date to set up a new draft
  id,name,format = draftInfo[0].split(':')
  date = str(datetime.date.today())
  
  #Instantiates a new draft
  importDraft = draft(name, format, date, None)
  
  #Sends the new draft and draft info to create the list of drafters and competitors
  readPlayers(importDraft, draftInfo)
  
  #Adds the new draft to the master draft list
  draftList.append(importDraft)
  
  draftFile.close()
  
  #This line is just for testing
  testDraft(importDraft)
  
#Method to read players and put them in their appropriate lists 
def readPlayers(dft, data):
  
  #Checks imported draft data line by line
  for line in data:
    
	#Parses data
    id,first,last = line.split(':')
	
	#Checks if a line contains information about a drafter and adds them to the draft list
    if id == 'D':
	  
      newDrafter = drafter(first, last, None)
	  
      dft.addDrafter(newDrafter)
	#Checks if a lline contains information about a competitor and adds them to the current drafters team list
    elif id == 'C':
	  
      newCompetitor = competitor(first, last, None)
      newDrafter.addMember(newCompetitor)
def saveDraft(dft):
  
  file = input('Enter name to save as: ') + '.txt'
  draftFile = open(file, 'w')
  
  draftFile.write('H:' + dft.name + ':' + dft.format +'\n')
  
  for drafter in dft.drafters:
  
    draftFile.write('D:' + drafter.firstName + ':' + drafter.lastName +'\n')
	
    for member in drafter.team:
    
      draftFile.write('C:' + member.firstName + ':' + member.lastName +'\n')
	
  draftFile.close()

#This method is for testing only
def testDraft(dft):
  
  print(dft)
  dft.printDrafters()
  
  #print(dft.drafters[0].team[5].fullName())

main()