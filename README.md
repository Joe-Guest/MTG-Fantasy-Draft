# MTG-Fantasy-Draft
Python program to create and organize fantasy drafts for magic the gathering tournaments

Any text file other than the readme is most likely for testing purposes only and can be ignored

The main method is in fantasydraft.py, this is the main file that manipulated the objects that actually make up the draft.

draft.py creates a draft object that contains a list of all drafters in the tournament. It also contains the method with the update logic for round results and will calculate wins, losses, and points by reading the results table from a WotC results URL. 

player.py creates a player object and contains two subclasses: drafter and competitor. A drafter has a team which is a list containing all of the competitors they've drafted. A competitor has a rank and a hall of fame status which affects how many points are awarded to a drafter for having that competitor on their team.
