import datetime
from draft import draft
from player import player, drafter, competitor

numDrafts = 0

def main():
  
  yesno = raw_input('Is there a current draft? [y/n]: ').lower()
  
  if yesno.lower() == 'y':
    
	yesno = raw_input('Would you like to import current draft? [y/n]: ').lower()
	
	if yesno.lower() == 'y':
	  
	  file = raw_input('Enter filename of draft you wish to import: ')
	  
	  importDraft(file)

def importDraft(file):
  
  draftFile = open(file, 'r')
  draftInfo = draftFile.readlines()
  
  #print(draftInfo)
  
  id,name,format = draftInfo[0].split(':')
  
  date = str(datetime.date.today())
  
  print(name + ' - ' + format + ' - ' + date)
  
  importDraft = draft(name, format, date, None)
  
  readDrafters(importDraft, draftInfo)
  
  importDraft.printDrafters()
 
def readDrafters(dft, data):
  
  for line in data:
    
	id,first,last = line.split(':')
	
	if id == 'D':
	  
	  newDrafter = drafter(first, last, None)
	  
	  dft.drafters.append(newDrafter)
	
	elif id == 'C':
	  
	  newCompetitor = competitor(first, last, None)
	  newDrafter.team.append(newCompetitor)

main()